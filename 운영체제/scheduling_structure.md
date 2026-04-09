# 

# Multi-Level Feedback Queue

## Pseudo Code

```python 
# MLFQ 스케줄링 알고리즘 예시
def mlfq_scheduler(processes):
    # Q0, Q1, Q2는 RR / Q3는 FCFS
    time_quantum = [2, 4, 8, None]
    boost_interval = 100  # 주기적으로 전체 우선순위 부스팅
    queues = [Queue() for _ in range(4)]
    now = 0

    # 모든 프로세스는 최상위 큐에서 시작
    for p in processes:
        p.level = 0
        p.used_in_level = 0  # Time Accounting 누적 시간
        queues[0].enqueue(p)

    while has_runnable_or_waiting_process(processes):
        # Priority Boosting: 장기 대기 방지
        if now > 0 and now % boost_interval == 0:
            for p in all_ready_processes_in_any_queue(queues):
                p.level = 0
                p.used_in_level = 0
                queues[0].enqueue(p)

        # 가장 높은 우선순위의 비어있지 않은 큐 선택
        level = highest_non_empty_queue_index(queues)
        if level is None:
            now += 1
            continue

        p = queues[level].dequeue()

        if level < 3:
            # RR 레벨: 해당 큐 퀀텀만큼 실행
            ran, event = run_process_for_quantum(p, time_quantum[level])
        else:
            # 최하위 큐: FCFS (종료 또는 I/O까지 연속 실행)
            ran, event = run_process_fcfs(p)

        now += ran

        if event == "FINISHED":
            continue

        if event == "IO_BLOCK":
            # I/O 이후 같은 우선순위로 복귀
            p.level = level
            p.used_in_level += ran  # Time Accounting: 부분 사용 시간도 누적
            enqueue_after_io_completion(p, queues[p.level])
        else:  # event == "QUANTUM_EXPIRED"
            p.used_in_level += ran
            # 누적 사용 시간이 현재 레벨 예산을 넘으면 강등
            if level < 3 and p.used_in_level >= time_quantum[level]:
                p.level = level + 1
                p.used_in_level = 0
            else:
                p.level = level
            queues[p.level].enqueue(p)
```

## 설명

다단계 피드백 큐(Multi-Level Feedback Queue, MLFQ)는 여러 개의 큐를 사용하여 프로세스의 우선순위를 동적으로 조정하는 스케줄링 알고리즘입니다. 각 큐는 서로 다른 타임 퀀텀을 가지며, 프로세스는 실행 시간에 따라 큐 사이를 이동할 수 있습니다.
- 프로세스는 처음에 최상위 큐에서 시작하며, 타임 퀀텀을 다 사용하면 다음 큐로 이동합니다.
- 프로세스가 타임 퀀텀을 다 사용하지 않고 종료되지 않으면, 같은 큐에 재할당됩니다.
- 이 알고리즘은 CPU 바운드 프로세스와 I/O 바운드 프로세스를 효과적으로 처리할 수 있도록 설계되었습니다. CPU 바운드 프로세스는 낮은 우선순위 큐로 이동하여 CPU 시간을 더 많이 사용하게 되고, I/O 바운드 프로세스는 높은 우선순위 큐에 남아 빠르게 처리됩니다.

## Case Study

```mermaid
flowchart TD
    S([프로세스 도착]) -->|최상위 큐 진입| Q0[Q0: RR / Quantum 2ms]

    subgraph L1[상위 우선순위 큐]
        Q0
    end

    subgraph L2[중간 우선순위 큐]
        Q1[Q1: RR / Quantum 4ms]
    end

    subgraph L3[하위 우선순위 큐]
        Q2[Q2: RR / Quantum 8ms]
        Q3[Q3: FCFS]
    end

    Q0 -->|Quantum 내 종료| DONE([프로세스 완료])
    Q0 -->|Quantum 내 I/O 발생| IO0[I/O 대기 후 복귀]
    IO0 -->|우선순위 유지| Q0
    Q0 -->|Quantum 전부 사용| Q1

    Q1 -->|Quantum 내 종료| DONE
    Q1 -->|Quantum 내 I/O 발생| IO1[I/O 대기 후 복귀]
    IO1 -->|우선순위 유지| Q1
    Q1 -->|Quantum 전부 사용| Q2

    Q2 -->|Quantum 내 종료| DONE
    Q2 -->|Quantum 내 I/O 발생| IO2[I/O 대기 후 복귀]
    IO2 -->|우선순위 유지| Q2
    Q2 -->|Quantum 전부 사용| Q3

    Q3 -->|CPU 작업 완료| DONE

    BOOST{{Priority Boosting 주기 도달}}
    BOOST -.->|장기 대기 프로세스 상향| Q0
    BOOST -.-> Q1
    BOOST -.-> Q2
    BOOST -.-> Q3
```

## 사례 설명 및 분석

이 다이어그램은 MLFQ 스케줄링 알고리즘의 프로세스 흐름을 보여줍니다. 프로세스는 처음에 최상위 큐에 진입하며, 타임 퀀텀을 다 사용하지 않고 I/O 작업을 수행하는 경우에 하위 큐로 강등되지 않고 현재 큐의 우선순위를 유지합니다. 타임 퀀텀을 다 사용하면 다음 큐로 이동(강등)하며, 최하위 큐에서는 FCFS(First-Come, First-Served) 방식으로 처리됩니다.
타임 퀀텀을 다 사용하지 않고 I/O 작업을 수행하고 다시 큐로 들어왔을 경우, 배정된 시간 합산제(Time Accounting)를 사용하여 Gaming the Scheduler 문제를 방지합니다.
또한 주기적으로 우선순위 부스팅이 발생하여, 장기간 대기한 프로세스가 최상위 큐로 이동하여 빠르게 처리될 수 있도록 합니다. 이를 통해 시스템 전체의 공정성을 유지하고, 장기 대기 프로세스가 무한 대기 상태에 빠지는 것을 방지할 수 있습니다.

### 용어 설명

- Gaming the Scheduler 문제 : 사용자가 악용하는 사레로, 프로세스가 타임 퀀텀을 다 사용하지 않고 I/O 작업을 수행하여 계속해서 높은 우선순위 큐에 머무르는 경우입니다. 
- 배정된 시간 합산제(Time Accounting) : 프로세스가 타임 퀀텀을 다 사용하지 않고 I/O 작업을 수행할 때, 사용한 시간만큼을 누적하여 다음에 큐로 돌아왔을 때 그 누적된 시간을 고려하여 우선순위를 조정하는 방법입니다. 이를 통해 프로세스가 계속해서 높은 우선순위 큐에 머무르는 것을 방지할 수 있습니다.

## 장점
- CPU 바운드와 I/O 바운드 프로세스를 효과적으로 구분하여 처리할 수 있습니다.
- 프로세스의 실행 시간에 따라 동적으로 우선순위를 조정하여 공정한 CPU 시간을 보장합니다.
- 우선순위 부스팅을 통해 장기 대기 프로세스가 무한 대기 상태에 빠지는 것을 방지할 수 있습니다.
- 다양한 유형의 프로세스를 효율적으로 처리할 수 있습니다.

## 단점
- 구현이 복잡하며, 여러 큐와 타임 퀀텀을 관리해야 합니다.
- 프로세스의 실행 시간 예측이 어려울 수 있으며, 잘못된 타임 퀀텀 설정은 성능 저하를 초래할 수 있습니다.
- 우선순위 부스팅이 너무 자주 발생하면 시스템 전체의 성능이 저하될 수 있습니다.
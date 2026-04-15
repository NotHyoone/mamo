# 1. First-Come, First-Served (FCFS) 

## Pseudo Code

```python
# FCFS 스케줄링 알고리즘 예시
def fcfs_scheduler(processes):
    # 프로세스는 도착 순서대로 정렬되어 있다고 가정
    now = 0
    for p in processes:
        if now < p.arrival_time:
            now = p.arrival_time  # CPU가 유휴 상태인 경우, 프로세스 도착 시간까지 대기
        run_process(p)  # 프로세스 실행
        now += p.burst_time  # 현재 시간 업데이트
```

## 설명

First-Come, First-Served (FCFS) 스케줄링 알고리즘은 가장 간단한 형태의 스케줄링 알고리즘으로, 프로세스가 도착한 순서대로 CPU를 할당하는 방식입니다. 동시에 도착했다면 누가 먼저 도착했는지에 따라 처리 순서가 결정됩니다. 이 알고리즘은 비선점형 정책을 사용합니다.

## Case Study

| Process | Arrival Time | Burst Time |
|---------|-------------|------------|
| P1      | 0           | 15         |
| P2      | 0           | 7          |
| P3      | 0           | 11         |
| P4      | 0           | 20         |

> 모든 프로세스가 t=0에 동시 도착. 동착 시 tie-break는 등록(입력) 순서이며, 이 예제에서는 P3 → P4 → P1 → P2 순으로 등록되었다.

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td colspan="2" align="center"><b>P3</b></td>
        <td colspan="4" align="center"><b>P4</b></td>
        <td colspan="3" align="center"><b>P1</b></td>
        <td align="center"><b>P2</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">11</td>
        <td></td>
        <td></td>
        <td></td>
        <td align="right">31</td>
        <td></td>
        <td></td>
        <td align="right">46</td>
        <td align="right">53</td>
    </tr>
</table>

## 사례 설명 및 분석

이 간트차트는 FCFS 스케줄링 알고리즘에서 네 개의 프로세스가 모두 t=0에 도착하여 CPU를 할당받아 실행되는 과정을 보여줍니다. 비선점형 정책이므로 한 번 CPU를 점유한 프로세스는 자신의 버스트 타임이 끝날 때까지 실행됩니다.

**실행 흐름**

| 구간  | 실행 프로세스 | 사유                          |
|-------|------------|------------------------------|
| 0~11  | P3         | 등록 순서 1번 (burst=11)       |
| 11~31 | P4         | 등록 순서 2번 (burst=20)       |
| 31~46 | P1         | 등록 순서 3번 (burst=15)       |
| 46~53 | P2         | 등록 순서 4번 (burst=7)        |

**결과 요약**

| Process | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|-------|---------|---------------|----------|
| P3      | 11    | 11      | 11            | 0        |
| P4      | 20    | 31      | 31            | 11       |
| P1      | 15    | 46      | 46            | 31       |
| P2      | 7     | 53      | 53            | 46       |

버스트 타임이 가장 짧은 P2(burst=7)가 가장 마지막에 실행되어 대기 시간이 46ms에 달합니다. 이는 FCFS의 대표적인 문제인 **Convoy Effect**로, 긴 작업들이 앞에 배치되면 짧은 작업들이 뒤에서 길게 대기하게 됩니다. 모든 프로세스의 도착 시간이 같다면 실행 순서가 성능에 결정적인 영향을 미치며, 짧은 작업이 먼저 실행되는 케이스(P2→P3→P1→P4)가 최적이고, 긴 작업이 먼저 실행되는 케이스(P4→P1→P3→P2)가 최악입니다.

이 사례는 FCFS가 구현은 단순하지만 응답 시간 측면에서는 매우 비효율적일 수 있음을 보여 줍니다. 특히 긴 작업이 먼저 도착하는 순간 뒤따르는 짧은 작업들이 함께 지연되므로, 대화형 시스템이나 빠른 응답이 필요한 환경에는 부적합하다는 점을 과제에서 분명히 지적할 수 있습니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`, 동시 도착 시 tie-break 기준(예: 입력 순서)이 필요합니다.
- 독특한 동작 방식 혹은 현상: 도착 순서대로 비선점 실행되므로 긴 작업이 앞에 오면 뒤의 짧은 작업들이 함께 지연되는 Convoy Effect가 발생할 수 있습니다.
- 구현 시, 특징적 고려사항 등: 준비 큐를 도착 순으로 안정 정렬해야 하며, CPU 유휴 시 현재 시간을 다음 도착 시각으로 점프시키는 처리가 필요합니다.

## 장점

- 구현이 매우 간단하며, 이해하기 쉽습니다.
- 프로세스가 도착한 순서대로 처리되므로 공정한 스케줄링이 가능합니다.

## 단점

- CPU 바운드 프로세스가 먼저 도착하면, I/O 바운드 프로세스가 긴 시간 동안 대기해야 하는 문제(Convoy Effect)가 발생할 수 있습니다.
- 프로세스의 실행 시간이 길면, 다른 프로세스가 대기하는 시간이 길어질 수 있습니다.

# 2. Shortest Job First (SJF)

## Pseudo Code

```python
# SJF 스케줄링 알고리즘 예시
def sjf_scheduler(processes):
    # 프로세스는 도착 시간과 버스트 타임이 주어졌다고 가정
    now = 0
    while processes:
        # 현재 시간까지 도착한 프로세스 중에서 버스트 타임이 가장 짧은 프로세스 선택
        available_processes = [p for p in processes if p.arrival_time <= now]
        if not available_processes:
            now += 1  # CPU가 유휴 상태인 경우, 다음 시간으로 이동
            continue
        next_process = min(available_processes, key=lambda p: p.burst_time)
        run_process(next_process)  # 프로세스 실행
        now += next_process.burst_time  # 현재 시간 업데이트
        processes.remove(next_process)  # 실행된 프로세스 제거
```

## 설명

Shortest Job First (SJF) 스케줄링 알고리즘은 현재 시간까지 도착한 프로세스 중에서 버스트 타임이 가장 짧은 프로세스를 선택하여 CPU를 할당하는 방식입니다. 이 알고리즘은 비선점형 정책을 사용합니다.

## Case Study

| Process | Arrival Time | Burst Time |
|---------|-------------|------------|
| P1      | 0           | 10         |
| P2      | 4           | 13         |
| P3      | 8           | 7          |
| P4      | 10          | 5          |

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td colspan="3" align="center"><b>P1</b></td>
        <td align="center"><b>P4</b></td>
        <td colspan="2" align="center"><b>P3</b></td>
        <td colspan="4" align="center"><b>P2</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td></td>
        <td align="right">10</td>
        <td align="right">15</td>
        <td></td>
        <td align="right">22</td>
        <td></td>
        <td></td>
        <td align="right">35</td>
    </tr>
</table>

## 사례 설명 및 분석

이 간트차트는 SJF 스케줄링 알고리즘에서 네 개의 프로세스가 도착 시간과 버스트 타임에 따라 CPU를 할당받아 실행되는 과정을 보여줍니다.

**실행 흐름**

- **t=0**: P1만 도착해 있으므로 P1(burst=10)이 실행됩니다.
- **t=10**: P1 완료. 현재 도착한 프로세스: P2(arr=4, burst=13), P3(arr=8, burst=7), P4(arr=10, burst=5). SJF는 가장 짧은 P4(burst=5)를 선택합니다.
- **t=15**: P4 완료. 남은 P2(burst=13), P3(burst=7). P3(burst=7)이 더 짧으므로 P3을 선택합니다.
- **t=22**: P3 완료. P2(burst=13)만 남아 실행됩니다.

**결과 요약**

| Process | Arrival | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|---------|-------|---------|---------------|----------|
| P1      | 0       | 10    | 10      | 10            | 0        |
| P4      | 10      | 5     | 15      | 5             | 0        |
| P3      | 8       | 7     | 22      | 14            | 7        |
| P2      | 4       | 13    | 35      | 31            | 18       |

P4는 도착과 동시에 CPU를 할당받아 대기 시간이 0입니다. 반면 가장 긴 P2(burst=13)는 짧은 작업들이 모두 소진된 후에야 실행되어 대기 시간(18ms)이 가장 깁니다. 이처럼 SJF는 평균 대기 시간을 줄이는 데 효과적이지만, 긴 작업에 대한 **Starvation** 위험이 존재합니다.

즉, SJF는 전체 평균 성능을 개선하는 데는 강점을 가지지만, 모든 프로세스를 공정하게 대우하는 방식은 아닙니다. 보고서에서는 "평균 대기 시간 최소화"와 "긴 작업의 불리함"을 함께 적는 것이 핵심입니다.

## 특징
- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`이 필수이며, 비선점형 SJF인지 선점형 SRTF인지 정책 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 현재 시점에 도착한 작업 중 가장 짧은 버스트를 우선 선택해 평균 대기 시간을 줄이지만, 긴 작업은 기아(Starvation) 위험이 있습니다.
- 구현 시, 특징적 고려사항 등: 버스트 시간 예측 정확도가 성능을 좌우하므로 추정식(예: 지수평활)을 함께 설계하고, 동률 처리 규칙 및 에이징 정책을 두는 것이 좋습니다.

## 장점

- 평균 대기 시간을 최소화할 수 있습니다.
- CPU 바운드 프로세스가 짧은 경우, 빠르게 처리할 수 있습니다.

## 단점

- 프로세스의 버스트 타임을 정확히 예측하기 어렵습니다.
- 긴 버스트 타임을 가진 프로세스가 계속해서 대기하는 문제(Starvation)가 발생할 수 있습니다.

# 3. Shortest Remaining Time First (SRTF)

## Pseudo Code

```python
# SRTF 스케줄링 알고리즘 예시
def srtf_scheduler(processes):
    # 프로세스는 도착 시간과 버스트 타임이 주어졌다고 가정
    now = 0
    while processes:
        # 현재 시간까지 도착한 프로세스 중에서 남은 버스트 타임이 가장 짧은 프로세스 선택
        available_processes = [p for p in processes if p.arrival_time <= now]
        if not available_processes:
            now += 1  # CPU가 유휴 상태인 경우, 다음 시간으로 이동
            continue
        next_process = min(available_processes, key=lambda p: p.remaining_time)
        run_process(next_process)  # 프로세스 실행
        now += next_process.remaining_time  # 현재 시간 업데이트
        processes.remove(next_process)  # 실행된 프로세스 제거
```

## 설명

Shortest Remaining Time First (SRTF) 스케줄링 알고리즘은 현재 시간까지 도착한 프로세스 중에서 남은 버스트 타임이 가장 짧은 프로세스를 선택하여 CPU를 할당하는 방식입니다. 이 알고리즘은 선점형 정책을 사용합니다.

## Case Study

| Process | Arrival Time | Burst Time |
|---------|-------------|------------|
| P1      | 0           | 20         |
| P2      | 3           | 5          |
| P3      | 7           | 11         |
| P4      | 12          | 2          |

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td align="center"><b>P1</b></td>
        <td colspan="2" align="center"><b>P2</b></td>
        <td align="center"><b>P3</b></td>
        <td align="center"><b>P4</b></td>
        <td colspan="2" align="center"><b>P3</b></td>
        <td colspan="5" align="center"><b>P1</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">3</td>
        <td align="right">8</td>
        <td align="right">12</td>
        <td align="right">14</td>
        <td></td>
        <td align="right">21</td>
        <td></td>
        <td></td>
        <td></td>
        <td align="right">38</td>
    </tr>
</table>

## 사례 설명 및 분석

이 간트차트는 SRTF 스케줄링 알고리즘에서 네 개의 프로세스가 도착 시간과 남은 버스트 타임에 따라 선점이 발생하는 과정을 보여줍니다.

**선점 발생 흐름**

| 시점  | 이벤트                                              | 선점 여부 |
|-------|----------------------------------------------------|---------|
| t=0   | P1(rem=20)만 존재 → P1 실행                          | -       |
| t=3   | P2(burst=5) 도착. P2(5) < P1(rem=17) → **P2가 선점** | 선점 ✓  |
| t=7   | P3(burst=11) 도착. P2(rem=1) < P3(11) → P2 계속    | 유지     |
| t=8   | P2 완료. P1(rem=17), P3(rem=11). P3(11) < P1(17) → P3 실행 | -  |
| t=12  | P4(burst=2) 도착. P4(2) < P3(rem=7) → **P4가 선점** | 선점 ✓  |
| t=14  | P4 완료. P1(rem=17), P3(rem=7). P3(7) < P1(17) → P3 재개 | - |
| t=21  | P3 완료. P1(rem=17)만 남아 실행 → t=38 완료          | -       |

**결과 요약**

| Process | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|-------|---------|---------------|----------|
| P2      | 5     | 8       | 5             | 0        |
| P4      | 2     | 14      | 2             | 0        |
| P3      | 11    | 21      | 14            | 3        |
| P1      | 20    | 38      | 38            | 18       |

SRTF는 총 두 번의 선점(t=3, t=12)이 발생했습니다. 짧은 작업인 P2, P4는 도착 즉시 CPU를 확보해 대기 시간이 0이지만, 가장 긴 P1(burst=20)은 두 번이나 중단되어 대기 시간이 18ms에 달합니다. SRTF는 SJF의 선점형 버전으로 평균 대기 시간 최소화에 최적이지만, P1과 같은 긴 작업의 **Starvation** 위험이 SJF보다 더 큽니다.

이 사례는 선점형 알고리즘이 짧은 작업의 응답성을 얼마나 크게 향상시키는지를 보여 주는 동시에, 긴 작업이 계속 뒤로 밀릴 수 있다는 문제도 드러냅니다. 따라서 SRTF는 효율성은 높지만 공정성 측면에서는 보완이 필요한 알고리즘으로 정리할 수 있습니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`이 필수이며, 선점형 정책 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 새로운 작업이 도착할 때마다 가장 짧은 남은 시간을 가진 작업으로 선점하여 평균 대기 시간을 줄이지만, 긴 작업은 기아(Starvation) 위험이 있습니다.
- 구현 시, 특징적 고려사항 등: 버스트 시간 예측 정확도가 성능을 좌우하므로 추정식(예: 지수평활)을 함께 설계하고, 동률 처리 규칙 및 에이징 정책을 두는 것이 좋습니다.

## 장점

- 평균 대기 시간을 최소화할 수 있습니다.
- 새로운 프로세스가 도착하여 현재 실행 중인 프로세스보다 짧은 버스트 타임을 가지면, 현재 프로세스를 선점하여 새로운 프로세스를 빠르게 처리할 수 있습니다.

## 단점

- 프로세스의 버스트 타임을 정확히 예측하기 어렵습니다.
- 긴 버스트 타임을 가진 프로세스가 계속해서 대기하는 문제(Starvation)가 발생할 수 있습니다.

# 4. Priority Scheduling

## Pseudo Code

```python
# Priority Scheduling 알고리즘 예시
def priority_scheduler(processes):
    # 프로세스는 도착 시간과 우선순위가 주어졌다고 가정
    now = 0
    while processes:
        # 현재 시간까지 도착한 프로세스 중에서 우선순위가 가장 높은 프로세스 선택
        available_processes = [p for p in processes if p.arrival_time <= now]
        if not available_processes:
            now += 1  # CPU가 유휴 상태인 경우, 다음 시간으로 이동
            continue
        next_process = max(available_processes, key=lambda p: p.priority)
        run_process(next_process)  # 프로세스 실행
        now += next_process.burst_time  # 현재 시간 업데이트
        processes.remove(next_process)  # 실행된 프로세스 제거
```

## 설명

Priority Scheduling 알고리즘은 현재 시간까지 도착한 프로세스 중에서 우선순위가 가장 높은 프로세스를 선택하여 CPU를 할당하는 방식입니다. 이 알고리즘은 비선점형 정책을 사용합니다.

## Case Study

| Process | Arrival Time | Burst Time | Priority |
|---------|-------------|------------|----------|
| P1      | 0           | 5          | 4        |
| P2      | 2           | 12         | 1        |
| P3      | 3           | 18         | 3        |
| P4      | 5           | 9          | 2        |

> **Priority 1 = 최고 우선순위** (숫자가 낮을수록 우선순위 높음). 선점형 정책 적용.

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td align="center"><b>P1</b></td>
        <td colspan="4" align="center"><b>P2</b></td>
        <td colspan="2" align="center"><b>P4</b></td>
        <td colspan="5" align="center"><b>P3</b></td>
        <td align="center"><b>P1</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">2</td>
        <td></td>
        <td></td>
        <td align="right">14</td>
        <td></td>
        <td align="right">23</td>
        <td></td>
        <td></td>
        <td></td>
        <td align="right">41</td>
        <td align="right">44</td>
    </tr>
</table>

## 사례 설명 및 분석

이 간트차트는 선점형 Priority Scheduling 알고리즘에서 네 개의 프로세스가 도착 시간과 우선순위에 따라 CPU를 할당받아 실행되는 과정을 보여줍니다.

**선점 발생 흐름**

| 시점  | 이벤트                                                    | 선점 여부 |
|-------|----------------------------------------------------------|---------|
| t=0   | P1(prio=4)만 존재 → P1 실행                               | -       |
| t=2   | P2(prio=1) 도착. prio 1 < 4 → **P2가 P1 선점** (P1 rem=3) | 선점 ✓  |
| t=3   | P3(prio=3) 도착. P2(prio=1)가 여전히 최고 → P2 계속       | 유지     |
| t=5   | P4(prio=2) 도착. P2(prio=1)가 여전히 최고 → P2 계속       | 유지     |
| t=14  | P2 완료. 대기 중: P1(prio=4), P3(prio=3), P4(prio=2). P4(prio=2) 선택 | -  |
| t=23  | P4 완료. P3(prio=3) > P1(prio=4). P3 실행                 | -       |
| t=41  | P3 완료. P1(rem=3) 실행 → t=44 완료                       | -       |

**결과 요약**

| Process | Priority | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|----------|-------|---------|---------------|----------|
| P2      | 1 (최고)  | 12    | 14      | 12            | 0        |
| P4      | 2        | 9     | 23      | 18            | 9        |
| P3      | 3        | 18    | 41      | 38            | 20       |
| P1      | 4 (최저)  | 5     | 44      | 44            | 39       |

P2는 t=2에 도착하자마자 최고 우선순위(prio=1)로 P1을 선점하여 이후 방해 없이 완료됩니다. 반면 P1은 우선순위가 가장 낮아(prio=4) 선점당한 뒤 다른 모든 프로세스가 끝날 때까지 기다려야 하며, 반환 시간이 44ms로 실제 버스트(5ms)의 거의 9배에 달합니다. 이는 선점형 Priority Scheduling에서 낮은 우선순위 프로세스가 겪는 **Starvation** 문제를 잘 보여줍니다.

Priority Scheduling은 중요한 작업을 우선 처리해야 하는 운영체제 환경에서 유용하지만, 우선순위 기준이 고정되어 있으면 낮은 우선순위 작업이 사실상 배제될 수 있습니다. 따라서 에이징과 같은 보완책이 실제 구현에서 왜 필요한지도 함께 설명하는 것이 바람직합니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`, `priority`가 필수이며, 비선점형 정책 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 우선순위가 높은 작업이 먼저 실행되지만, 낮은 우선순위 작업이 무한 대기 상태에 빠지는 Starvation 문제가 발생할 수 있습니다.
- 구현 시, 특징적 고려사항 등: 우선순위가 동일한 경우의 처리 규칙과 Starvation 완화를 위한 에이징 정책을 설계하는 것이 중요합니다.

## 장점

- 중요한 작업이 빠르게 처리될 수 있습니다.
- 새로운 프로세스가 도착하여 현재 실행 중인 프로세스보다 높은 우선순위를 가지면, 현재 프로세스를 선점하여 새로운 프로세스를 빠르게 처리할 수 있습니다.

## 단점

- 낮은 우선순위 작업이 무한 대기 상태에 빠지는 문제(Starvation)가 발생할 수 있습니다.
- 우선순위가 동일한 경우의 처리 규칙이 필요합니다.

# 5. HRRN (Highest Response Ratio Next)

## Pseudo Code

```python
# HRRN 스케줄링 알고리즘 예시
def hrrn_scheduler(processes):
    # 프로세스는 도착 시간과 버스트 타임이 주어졌다고 가정
    now = 0
    while processes:
        # 현재 시간까지 도착한 프로세스 중에서 응답 비율이 가장 높은 프로세스 선택
        available_processes = [p for p in processes if p.arrival_time <= now]
        if not available_processes:
            now += 1  # CPU가 유휴 상태인 경우, 다음 시간으로 이동
            continue
        next_process = max(available_processes, key=lambda p: (now - p.arrival_time + p.burst_time) / p.burst_time)
        run_process(next_process)  # 프로세스 실행
        now += next_process.burst_time  # 현재 시간 업데이트
        processes.remove(next_process)  # 실행된 프로세스 제거
```

## 설명

HRRN (Highest Response Ratio Next) 스케줄링 알고리즘은 현재 시간까지 도착한 프로세스 중에서 응답 비율이 가장 높은 프로세스를 선택하여 CPU를 할당하는 방식입니다. 응답 비율은 (대기 시간 + 버스트 타임) / 버스트 타임으로 계산됩니다. 이 알고리즘은 비선점형 정책을 사용합니다.

## Case Study

| Process | Arrival Time | Burst Time |
|---------|-------------|------------|
| P1      | 0           | 10         |
| P2      | 1           | 28         |
| P3      | 2           | 6          |
| P4      | 3           | 4          |

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td colspan="2" align="center"><b>P1</b></td>
        <td align="center"><b>P4</b></td>
        <td align="center"><b>P3</b></td>
        <td colspan="6" align="center"><b>P2</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">10</td>
        <td align="right">14</td>
        <td align="right">20</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td align="right">48</td>
    </tr>
</table>

## 사례 설명 및 분석

이 간트차트는 HRRN 스케줄링 알고리즘에서 네 개의 프로세스가 응답 비율(HRR)을 기준으로 CPU를 할당받아 실행되는 과정을 보여줍니다. 응답 비율 = (대기 시간 + 버스트 타임) / 버스트 타임.

**t=0**: P1 혼자 도착 → P1(burst=10) 실행, t=10 완료.

**t=10 — HRRN 계산 (P2, P3, P4 대기 중)**

| Process | 대기 시간     | Burst | 응답 비율 = (대기 + Burst) / Burst      |
|---------|-------------|-------|----------------------------------------|
| P2      | 10 − 1 = 9  | 28    | (9 + 28) / 28 = 37/28 ≈ **1.32**      |
| P3      | 10 − 2 = 8  | 6     | (8 + 6) / 6 = 14/6 ≈ **2.33**         |
| P4      | 10 − 3 = 7  | 4     | (7 + 4) / 4 = 11/4 = **2.75** ← 최고  |

→ P4 선택, t=10~14 실행. P4 완료.

**t=14 — HRRN 재계산 (P2, P3 대기 중)**

| Process | 대기 시간      | Burst | 응답 비율                               |
|---------|--------------|-------|----------------------------------------|
| P2      | 14 − 1 = 13  | 28    | (13 + 28) / 28 = 41/28 ≈ **1.46**     |
| P3      | 14 − 2 = 12  | 6     | (12 + 6) / 6 = 18/6 = **3.0** ← 최고  |

→ P3 선택, t=14~20 실행. P3 완료. 이후 P2만 남아 t=20~48 실행.

**결과 요약**

| Process | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|-------|---------|---------------|----------|
| P1      | 10    | 10      | 10            | 0        |
| P4      | 4     | 14      | 11            | 7        |
| P3      | 6     | 20      | 18            | 12       |
| P2      | 28    | 48      | 47            | 19       |

HRRN은 대기 시간이 길수록 응답 비율이 높아지는 구조를 통해 Starvation을 방지합니다. P2는 burst=28으로 가장 길지만, 대기하는 동안 응답 비율이 꾸준히 상승하여 결국 t=20에 CPU를 할당받습니다. 만약 SJF였다면 짧은 작업이 계속 도착할 경우 P2는 무한정 대기했을 것이지만, HRRN에서는 누적 대기 시간이 안전망 역할을 합니다.

따라서 HRRN은 짧은 작업 우선 원칙과 오래 기다린 작업에 대한 보상을 결합한 절충형 알고리즘으로 이해할 수 있습니다. 과제에서는 SJF보다 공정성이 보완되었다는 점을 강조하면 설명이 더 설득력 있어집니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`이 필수이며, 비선점형 정책 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 응답 비율이 높은 작업이 먼저 실행되므로, 긴 작업도 일정 시간이 지나면 우선순위가 높아져 처리될 수 있어 Starvation 문제를 완화할 수 있습니다.
- 구현 시, 특징적 고려사항 등: 응답 비율 계산 시 대기 시간과 버스트 타임을 정확히 관리하는 것이 중요하며, 동률 처리 규칙을 설계하는 것이 좋습니다.

## 장점

- 긴 버스트 타임을 가진 프로세스도 일정 시간이 지나면 우선순위가 높아져 처리될 수 있어 Starvation 문제를 완화할 수 있습니다.
- 응답 비율이 높은 프로세스가 먼저 실행되므로, 효율적인 스케줄링이 가능합니다.

## 단점

- 응답 비율 계산이 복잡할 수 있으며, 대기 시간과 버스트 타임을 정확히 관리해야 합니다.
- 우선순위가 동일한 경우의 처리 규칙이 필요합니다.

# 6. Round Robin (RR)

## Pseudo Code

```python
# RR 스케줄링 알고리즘 예시
def rr_scheduler(processes, time_quantum):
    # 프로세스는 도착 시간과 버스트 타임이 주어졌다고 가정
    now = 0
    queue = []
    while processes or queue:
        # 현재 시간까지 도착한 프로세스 큐에 추가
        for p in processes:
            if p.arrival_time <= now:
                queue.append(p)
        processes = [p for p in processes if p.arrival_time > now]

        if not queue:
            now += 1  # CPU가 유휴 상태인 경우, 다음 시간으로 이동
            continue

        current_process = queue.pop(0)  # 큐에서 첫 번째 프로세스 선택
        run_time = min(time_quantum, current_process.remaining_time)
        run_process(current_process, run_time)  # 프로세스 실행
        now += run_time  # 현재 시간 업데이트
        current_process.remaining_time -= run_time  # 남은 버스트 타임 업데이트

        if current_process.remaining_time > 0:
            queue.append(current_process)  # 아직 실행이 필요한 경우 큐에 재추가
```

## 설명

Round Robin (RR) 스케줄링 알고리즘은 각 프로세스에 일정한 시간 단위(타임 퀀텀)를 할당하여 CPU를 순환적으로 할당하는 방식입니다. 이 알고리즘은 선점형 정책을 사용합니다.

## Case Study

| Process | Arrival Time | Burst Time |
|---------|-------------|------------|
| P1      | 0           | 10         |
| P2      | 1           | 28         |
| P3      | 2           | 6          |
| P4      | 3           | 4          |

> Time Quantum = 5ms

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td align="center"><b>P1</b></td>
        <td align="center"><b>P2</b></td>
        <td align="center"><b>P3</b></td>
        <td align="center"><b>P4</b></td>
        <td align="center"><b>P1</b></td>
        <td align="center"><b>P2</b></td>
        <td align="center"><b>P3</b></td>
        <td align="center"><b>P2</b></td>
        <td align="center"><b>P2</b></td>
        <td align="center"><b>P2</b></td>
        <td align="center"><b>P2</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">5</td>
        <td align="right">10</td>
        <td align="right">15</td>
        <td align="right">19</td>
        <td align="right">24</td>
        <td align="right">29</td>
        <td align="right">30</td>
        <td align="right">35</td>
        <td align="right">40</td>
        <td align="right">45</td>
        <td align="right">48</td>
    </tr>
</table>

## 사례 설명 및 분석

이 간트차트는 RR 스케줄링 알고리즘에서 타임 퀀텀(q=5)을 기준으로 네 개의 프로세스가 순환 실행되는 과정을 보여줍니다.

**큐 추적**

| 구간    | 실행  | 남은 버스트  | 큐 상태 (실행 후)                    |
|---------|-------|------------|-------------------------------------|
| 0~5     | P1    | P1: rem=5  | [P2(28), P3(6), P4(4), P1(5)]       |
| 5~10    | P2    | P2: rem=23 | [P3(6), P4(4), P1(5), P2(23)]       |
| 10~15   | P3    | P3: rem=1  | [P4(4), P1(5), P2(23), P3(1)]       |
| 15~19   | P4    | P4: 완료   | [P1(5), P2(23), P3(1)]              |
| 19~24   | P1    | P1: 완료   | [P2(23), P3(1)]                     |
| 24~29   | P2    | P2: rem=18 | [P3(1), P2(18)]                     |
| 29~30   | P3    | P3: 완료   | [P2(18)]                            |
| 30~48   | P2    | P2: rem=0  | [] (5+5+5+3 → 완료)                 |

> t=0~5 사이에 P2(arr=1), P3(arr=2), P4(arr=3)가 모두 도착하여 P1 타임 퀀텀 종료 시 한꺼번에 큐에 추가됩니다.

**결과 요약**

| Process | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|-------|---------|---------------|----------|
| P4      | 4     | 19      | 16            | 12       |
| P1      | 10    | 24      | 24            | 14       |
| P3      | 6     | 30      | 28            | 22       |
| P2      | 28    | 48      | 47            | 19       |

RR은 모든 프로세스에 공평한 CPU 시간을 보장합니다. P2(burst=28)는 가장 많은 CPU를 필요로 하지만 6번의 슬롯으로 나뉘어 실행됩니다. 타임 퀀텀(5ms)이 P4(burst=4)보다 크기 때문에 P4는 한 번의 슬롯에서 완료되었고, P3(burst=6)는 첫 슬롯에 5ms를 사용하고 2라운드에서 나머지 1ms로 완료됩니다. 타임 퀀텀이 크면 클수록 RR은 FCFS에 가까워지고, 작을수록 문맥 교환 오버헤드가 증가합니다.

이 알고리즘의 핵심은 효율성보다 공정성에 있습니다. 따라서 보고서에서는 "모든 프로세스가 일정 시간 안에 CPU를 다시 받을 수 있다"는 장점과 함께, 타임 퀀텀 설정이 너무 작으면 오버헤드가 급증한다는 한계를 함께 제시하는 것이 좋습니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`, `time quantum`이 필수이며, 선점형 정책 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 각 프로세스가 타임 퀀텀만큼 CPU를 사용하고, 남은 버스트 타임이 있는 경우 큐에 재추가되어 다음 차례에 다시 실행됩니다.
- 구현 시, 특징적 고려사항 등: 타임 퀀텀의 적절한 설정이 중요하며, 너무 짧으면 문맥 교환 오버헤드가 증가하고, 너무 길면 RR의 공정성이 저하될 수 있습니다.

## 장점

- 공정한 CPU 시간을 보장할 수 있습니다.
- 프로세스가 도착한 순서대로 CPU를 할당하므로, 간단한 스케줄링이 가능합니다.

## 단점

- 타임 퀀텀이 너무 짧으면 문맥 교환 오버헤드가 증가하여 성능이 저하될 수 있습니다.
- 타임 퀀텀이 너무 길면 RR의 공정성이 저하되어 긴 프로세스가 CPU를 독점할 수 있습니다.

# 7. Multilevel Queue

## Pseudo Code

```python
# Multilevel Queue 스케줄링 알고리즘 예시
def multilevel_queue_scheduler(processes):
    # Q0, Q1, Q2는 RR / Q3는 FCFS
    time_quantum = [2, 4, 8, None]
    queues = [Queue() for _ in range(4)]
    now = 0

    # 프로세스 초기 배치: 예시에서는 우선순위에 따라 큐에 배치
    for p in processes:
        if p.priority == 0:
            queues[0].enqueue(p)
        elif p.priority == 1:
            queues[1].enqueue(p)
        elif p.priority == 2:
            queues[2].enqueue(p)
        else:
            queues[3].enqueue(p)

    while has_runnable_or_waiting_process(processes):
        # 가장 높은 우선순위의 비어있지 않은 큐 선택
        level = highest_non_empty_queue_index(queues)
        if level is None:
            now += 1
            continue

        p = queues[level].dequeue()

        if level < 3:
            # RR 레벨: 해당 큐 퀀텀만큼 실행
            run_process_for_quantum(p, time_quantum[level])
        else:
            # 최하위 큐: FCFS (종료 또는 I/O까지 연속 실행)
            run_process_fcfs(p)

        now += p.burst_time  # 현재 시간 업데이트
```

## 설명

다단계 큐(Multilevel Queue) 스케줄링 알고리즘은 여러 개의 큐를 사용하여 프로세스의 우선순위를 고정적으로 분류하는 방식입니다. 각 큐는 서로 다른 스케줄링 알고리즘을 사용할 수 있으며, 프로세스는 초기 배치에 따라 특정 큐에 할당됩니다. 이 알고리즘은 선점형 또는 비선점형 정책을 사용할 수 있습니다.

## Case Study

| Process | Arrival Time | Burst Time | Queue              |
|---------|-------------|------------|--------------------|
| P1      | 0           | 8          | Q0 (SRTF, 고우선순위) |
| P2      | 1           | 4          | Q0 (SRTF, 고우선순위) |
| P3      | 0           | 6          | Q1 (HRRN, 저우선순위) |
| P4      | 2           | 4          | Q1 (HRRN, 저우선순위) |

> Q0이 비어 있을 때만 Q1이 CPU를 점유한다. Q0은 선점형 SRTF, Q1은 비선점형 HRRN을 사용한다.

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td align="center"><b>Q0:P1</b></td>
        <td colspan="2" align="center"><b>Q0:P2</b></td>
        <td colspan="3" align="center"><b>Q0:P1</b></td>
        <td colspan="2" align="center"><b>Q1:P4</b></td>
        <td colspan="2" align="center"><b>Q1:P3</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">1</td>
        <td></td>
        <td></td>
        <td align="right">5</td>
        <td align="right">12</td>
        <td></td>
        <td align="right">16</td>
        <td></td>
        <td align="right">22</td>
    </tr>
</table>

<table>
    <tr><th>Queue</th><th>Execution Order</th><th>Time Marks</th></tr>
    <tr><td>Q0</td><td>P1 → P2 → P1</td><td>0, 1, 5, 12</td></tr>
    <tr><td>Q1</td><td>P4 → P3</td><td>12, 16, 22</td></tr>
</table>

## 사례 설명 및 분석

이 간트차트는 Multilevel Queue 스케줄링 알고리즘에서 두 개의 큐(Q0: SRTF, Q1: HRRN)를 사용하여 네 개의 프로세스가 CPU를 할당받아 실행되는 과정을 보여줍니다.

**Q0 (SRTF) 실행 과정**

- **t=0**: Q0에 P1(rem=8)만 존재하므로 P1이 실행됩니다.
- **t=1**: P2(rem=4)가 Q0에 도착합니다. SRTF 원칙에 따라 남은 버스트 타임이 더 짧은 P2(rem=4 < P1 rem=7)가 P1을 선점합니다.
- **t=5**: P2가 완료(burst=4 소진)됩니다. Q0에 P1(rem=7)만 남아 P1이 재개됩니다.
- **t=12**: P1이 완료됩니다. Q0이 비어 있으므로 Q1이 CPU를 점유합니다.

**Q1 (HRRN) 실행 과정**

Q0이 비워진 t=12 시점에서 HRRN 응답 비율을 계산합니다.

| Process | 대기 시간 (t=12 기준) | Burst Time | 응답 비율 = (대기 + Burst) / Burst |
|---------|---------------------|------------|----------------------------------|
| P3      | 12 − 0 = 12         | 6          | (12 + 6) / 6 = **3.0**           |
| P4      | 12 − 2 = 10         | 4          | (10 + 4) / 4 = **3.5**           |

응답 비율이 더 높은 P4(3.5)가 먼저 선택됩니다.

- **t=12 ~ t=16**: P4 실행 (burst=4), 완료.
- **t=16 ~ t=22**: P3 실행 (burst=6), 완료.

**결과 요약**

| Process | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|---------|--------------|---------|
| P1      | 12      | 12 − 0 = 12  | 12 − 8 = 4  |
| P2      | 5       | 5 − 1 = 4    | 4 − 4 = 0   |
| P3      | 22      | 22 − 0 = 22  | 22 − 6 = 16 |
| P4      | 16      | 16 − 2 = 14  | 14 − 4 = 10 |

Q0 프로세스(P1, P2)는 SRTF의 선점형 특성 덕분에 빠르게 처리된 반면, Q1 프로세스(P3, P4)는 Q0이 완전히 비워질 때까지 대기하므로 대기 시간이 크게 늘어납니다. Q1 내부에서는 HRRN이 도착 순서가 아닌 응답 비율을 기준으로 P4를 P3보다 먼저 실행함으로써, 단순 FCFS 대비 P4의 대기 시간을 줄이고 Starvation을 완화합니다.

이 사례는 다단계 큐가 단순한 우선순위 분류를 넘어서, 서로 다른 정책을 계층적으로 결합할 수 있다는 점을 보여 줍니다. 즉, 상위 큐에는 빠른 응답이 필요한 작업을, 하위 큐에는 상대적으로 덜 긴급한 작업을 두어 시스템 전체의 정책을 세분화할 수 있습니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`, `priority`가 필수이며, 각 큐의 스케줄링 알고리즘과 초기 배치 규칙이 필요합니다.
- 독특한 동작 방식 혹은 현상: 프로세스가 초기 배치에 따라 특정 큐에 할당되고, 각 큐는 서로 다른 스케줄링 알고리즘을 사용하여 프로세스를 처리합니다.
- 구현 시, 특징적 고려사항 등: 프로세스의 초기 배치 규칙과 각 큐의 스케줄링 알고리즘을 신중하게 설계해야 하며, 특정 큐에 프로세스가 몰리는 것을 방지하기 위한 조치가 필요할 수 있습니다.

## 장점

- 프로세스의 우선순위를 고정적으로 분류하여 특정 유형의 프로세스가 항상 높은 우선순위를 가지게 할 수 있습니다.
- 각 큐에 서로 다른 스케줄링 알고리즘을 적용하여 다양한 유형의 프로세스를 효율적으로 처리할 수 있습니다.

## 단점

- 프로세스의 초기 배치에 따라 특정 큐에 프로세스가 몰리는 문제가 발생할 수 있습니다.
- 프로세스의 우선순위를 고정적으로 분류하므로, 특정 유형의 프로세스가 항상 낮은 우선순위를 가지게 되어 Starvation 문제가 발생할 수 있습니다.

# 8. Multi-Level Feedback Queue

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

| Process | Arrival Time | Total CPU Burst | 특성 |
|---------|-------------|-----------------|------|
| P1      | 0           | 12              | CPU-bound, 긴 작업 |
| P2      | 1           | 1               | 매우 짧은 interactive 작업 |
| P3      | 2           | 6               | 중간 길이 작업 |

> 큐 정책: Q0는 RR(2ms), Q1은 RR(4ms), Q2는 RR(8ms), Q3는 FCFS. 모든 프로세스는 Q0에서 시작한다.
> 이 예제는 CPU burst 기준으로만 설명하며, I/O 복귀와 Priority Boosting은 동작 원리 설명에서 별도로 다룬다.

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td colspan="2" align="center"><b>Q0:P1</b></td>
        <td align="center"><b>Q0:P2</b></td>
        <td colspan="2" align="center"><b>Q0:P3</b></td>
        <td colspan="3" align="center"><b>Q1:P1</b></td>
        <td colspan="2" align="center"><b>Q1:P3</b></td>
        <td colspan="4" align="center"><b>Q2:P1</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">2</td>
        <td align="right">3</td>
        <td align="right">5</td>
        <td></td>
        <td align="right">9</td>
        <td></td>
        <td align="right">13</td>
        <td></td>
        <td></td>
        <td></td>
        <td align="right">19</td>
    </tr>
</table>

<table>
    <tr><th>Queue</th><th>Execution Order</th><th>Time Marks</th></tr>
    <tr><td>Q0</td><td>P1 → P2 → P3</td><td>0, 2, 3, 5</td></tr>
    <tr><td>Q1</td><td>P1 → P3</td><td>5, 9, 13</td></tr>
    <tr><td>Q2</td><td>P1</td><td>13, 19</td></tr>
</table>

## 사례 설명 및 분석

이 간트차트는 MLFQ에서 짧은 작업은 상위 큐에서 빠르게 끝나고, 긴 작업은 점차 하위 큐로 내려가 더 긴 타임 퀀텀을 받는 과정을 보여줍니다. 이 예제에서는 I/O 없이 CPU burst만으로 큐 이동을 관찰할 수 있도록 단순화했습니다.

**실행 흐름**

| 구간  | 실행 프로세스 | 실행 큐 | 결과 |
|-------|------------|--------|------|
| 0~2   | P1         | Q0     | 2ms 모두 사용, rem=10 → Q1으로 강등 |
| 2~3   | P2         | Q0     | 1ms만 사용하고 종료, 상위 큐에서 즉시 완료 |
| 3~5   | P3         | Q0     | 2ms 모두 사용, rem=4 → Q1으로 강등 |
| 5~9   | P1         | Q1     | 4ms 모두 사용, rem=6 → Q2로 강등 |
| 9~13  | P3         | Q1     | 4ms 사용 후 종료 |
| 13~19 | P1         | Q2     | 6ms 연속 실행 후 종료 |

**결과 요약**

| Process | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|---------|--------------|---------|
| P2      | 3       | 3 − 1 = 2    | 2 − 1 = 1 |
| P3      | 13      | 13 − 2 = 11  | 11 − 6 = 5 |
| P1      | 19      | 19 − 0 = 19  | 19 − 12 = 7 |

짧은 작업인 P2는 최상위 큐 Q0에서 바로 끝나므로 매우 빠른 응답성을 얻습니다. 반면 CPU를 오래 사용하는 P1은 Q0, Q1, Q2로 점차 내려가며 실행됩니다. 이것이 MLFQ의 핵심으로, interactive 작업에는 빠른 응답성을 주고 CPU-bound 작업에는 점차 긴 실행 구간을 배정합니다.

이 예제에는 나타나지 않았지만, 실제 MLFQ에서는 타임 퀀텀을 다 쓰기 전에 I/O로 빠져나간 작업은 같은 우선순위를 유지하도록 설계할 수 있고, 장기 대기를 방지하기 위해 주기적 Priority Boosting을 적용합니다. 또한 Time Accounting을 사용하면 짧게 실행하고 반복적으로 I/O를 요청해 상위 큐에 계속 머무르려는 Gaming the Scheduler 문제를 완화할 수 있습니다.

따라서 MLFQ는 정적인 우선순위 방식보다 훨씬 유연하며, 실제 운영체제에서 다양한 성격의 작업을 동시에 처리할 때 매우 실용적인 알고리즘입니다. 보고서에서는 동적 우선순위 조정, 부스팅, 타임 어카운팅이라는 세 가지 핵심 요소를 중심으로 설명하면 구조가 분명해집니다.

### 용어 설명

- Gaming the Scheduler 문제 : 사용자가 악용하는 사례로, 프로세스가 타임 퀀텀을 다 사용하지 않고 I/O 작업을 수행하여 계속해서 높은 우선순위 큐에 머무르는 경우입니다. 
- 배정된 시간 합산제(Time Accounting) : 프로세스가 타임 퀀텀을 다 사용하지 않고 I/O 작업을 수행할 때, 사용한 시간만큼을 누적하여 다음에 큐로 돌아왔을 때 그 누적된 시간을 고려하여 우선순위를 조정하는 방법입니다. 이를 통해 프로세스가 계속해서 높은 우선순위 큐에 머무르는 것을 방지할 수 있습니다.

## 특징
- 특정 알고리즘별 개별 입력 요소: 큐 개수, 각 큐의 타임 퀀텀, 초기 배치 규칙, 우선순위 부스팅 주기, I/O 복귀 시 재배치 규칙이 필요합니다.
- 독특한 동작 방식 혹은 현상: 짧고 상호작용적인 작업은 상위 큐에서 빠르게 처리되고, CPU 바운드 작업은 하위 큐로 점진 강등되는 동적 피드백이 핵심입니다.
- 구현 시, 특징적 고려사항 등: Time Accounting으로 Gaming을 방지하고, Starvation 완화를 위한 주기적 Priority Boosting 및 큐 간 이동 시점의 정확한 시간 회계가 중요합니다.

## 장점
- CPU 바운드와 I/O 바운드 프로세스를 효과적으로 구분하여 처리할 수 있습니다.
- 프로세스의 실행 시간에 따라 동적으로 우선순위를 조정하여 공정한 CPU 시간을 보장합니다.
- 우선순위 부스팅을 통해 장기 대기 프로세스가 무한 대기 상태에 빠지는 것을 방지할 수 있습니다.
- 다양한 유형의 프로세스를 효율적으로 처리할 수 있습니다.

## 단점
- 구현이 복잡하며, 여러 큐와 타임 퀀텀을 관리해야 합니다.
- 프로세스의 실행 시간 예측이 어려울 수 있으며, 잘못된 타임 퀀텀 설정은 성능 저하를 초래할 수 있습니다.
- 우선순위 부스팅이 너무 자주 발생하면 시스템 전체의 성능이 저하될 수 있습니다.

# 9. Fair Share Scheduling

## Pseudo Code

```python
# Fair Share Scheduling 알고리즘 예시
def fair_share_scheduler(processes, user_limits):
    # user_limits: {user_id: max_cpu_share}
    now = 0
    while has_runnable_or_waiting_process(processes):
        # 각 사용자별 CPU 사용량 계산
        user_usage = calculate_user_cpu_usage(processes)

        # CPU 할당 가능한 프로세스 중에서 공정하게 선택
        available_processes = [p for p in processes if p.arrival_time <= now and user_usage[p.user_id] < user_limits[p.user_id]]
        
        if not available_processes:
            now += 1  # CPU가 유휴 상태인 경우, 다음 시간으로 이동
            continue

        next_process = select_fair_process(available_processes, user_usage, user_limits)
        run_process(next_process)  # 프로세스 실행
        now += next_process.burst_time  # 현재 시간 업데이트
```

## 설명

Fair Share Scheduling 알고리즘은 시스템 자원을 사용자별로 공정하게 분배하는 스케줄링 알고리즘입니다. 각 사용자에게 최대 CPU 점유율을 설정하여, 특정 사용자가 시스템 자원을 과도하게 사용하는 것을 방지합니다. 이 알고리즘은 선점형 정책을 사용할 수 있습니다.

## Case Study

| Process | User  | Arrival Time | Burst Time |
|---------|-------|-------------|------------|
| P1      | UserA | 0           | 6          |
| P2      | UserA | 0           | 4          |
| P3      | UserB | 0           | 3          |
| P4      | UserB | 0           | 5          |

> CPU 할당 비율: UserA 60%, UserB 40% (비율 3:2) / Time Quantum = 2ms  
> 사이클마다 UserA에게 3슬롯(6ms), UserB에게 2슬롯(4ms)을 가중치 RR 방식으로 배분한다.  
> 각 사용자 내부에서는 RR 방식으로 프로세스를 순환 실행한다.

**Gantt Chart for the Schedule**

<table>
    <tr>
        <td align="center"><b>UA:P1</b></td>
        <td align="center"><b>UA:P2</b></td>
        <td align="center"><b>UB:P3</b></td>
        <td align="center"><b>UA:P1</b></td>
        <td align="center"><b>UB:P4</b></td>
        <td align="center"><b>UA:P2</b></td>
        <td align="center"><b>UA:P1</b></td>
        <td align="center"><b>UB:P3</b></td>
        <td colspan="2" align="center"><b>UB:P4</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">2</td>
        <td align="right">4</td>
        <td align="right">6</td>
        <td align="right">8</td>
        <td align="right">10</td>
        <td align="right">12</td>
        <td align="right">14</td>
        <td align="right">15</td>
        <td align="right">18</td>
    </tr>
</table>

<table>
    <tr><th>User</th><th>Execution Order</th><th>Time Marks</th></tr>
    <tr><td>UserA</td><td>P1 → P2 → P1 → P2 → P1</td><td>0, 2, 6, 10, 12, 14</td></tr>
    <tr><td>UserB</td><td>P3 → P4 → P3 → P4</td><td>4, 8, 14, 15, 18</td></tr>
</table>

## 사례 설명 및 분석

이 간트차트는 Fair Share Scheduling에서 CPU를 프로세스 개수가 아니라 사용자 단위의 점유율로 배분하는 과정을 보여줍니다. 이 예제에서는 UserA가 60%, UserB가 40%의 CPU 비율을 보장받으며, 각 사용자 내부에서는 Round Robin 방식으로 자신의 프로세스를 순환 실행합니다.

**실행 흐름**

가중치 비율 3:2를 반영하여 한 사이클마다 UserA는 3슬롯(총 6ms), UserB는 2슬롯(총 4ms)을 배분받습니다. 각 사용자 내부에서는 자기 차례가 왔을 때 RR로 다음 프로세스를 선택합니다.

**사이클 1 (t=0 ~ t=10)**

| 구간  | 실행 프로세스 | 사용자 | 사유                             |
|-------|------------|--------|----------------------------------|
| 0~2   | P1         | UserA  | UserA 첫 번째 슬롯                |
| 2~4   | P2         | UserA  | UserA 두 번째 슬롯 (UserA 내 RR) |
| 4~6   | P3         | UserB  | UserB 첫 번째 슬롯                |
| 6~8   | P1         | UserA  | UserA 세 번째 슬롯 (UserA 내 RR) |
| 8~10  | P4         | UserB  | UserB 두 번째 슬롯 (UserB 내 RR) |

→ t=10 시점 누적 사용량은 UserA 6ms, UserB 4ms로 정확히 60% : 40%를 만족합니다.

**사이클 2 (t=10 ~ t=14)**

| 구간  | 실행 프로세스 | 잔여량     | 비고         |
|-------|------------|----------|-------------|
| 10~12 | P2         | rem: 2→0 | P2 완료      |
| 12~14 | P1         | rem: 2→0 | P1 완료      |

→ t=14 시점에 UserA의 모든 프로세스가 종료되므로, 이후 남은 CPU는 UserB가 사용합니다.

**UserB 잔여 처리 (t=14 ~ t=18)**

| 구간  | 실행 프로세스 | 잔여       | 비고   |
|-------|------------|----------|--------|
| 14~15 | P3         | rem: 1→0 | P3 완료 |
| 15~18 | P4         | rem: 3→0 | P4 완료 |

**결과 요약**

| Process | User  | Burst | 완료 시간 | 반환 시간 (TAT) | 대기 시간 |
|---------|-------|-------|---------|---------------|---------|
| P1      | UserA | 6     | 14      | 14            | 8       |
| P2      | UserA | 4     | 12      | 12            | 8       |
| P3      | UserB | 3     | 15      | 15            | 12      |
| P4      | UserB | 5     | 18      | 18            | 13      |

평균 반환 시간은 14.75ms, 평균 대기 시간은 10.25ms입니다. UserA와 UserB는 각각 프로세스를 2개씩 보유하지만, 할당된 CPU 점유율이 다르기 때문에 UserA의 프로세스가 전체적으로 더 빨리 완료됩니다. UserA의 작업이 t=14에 모두 끝난 뒤에는 남은 CPU를 UserB가 연속해서 사용합니다. 이처럼 Fair Share Scheduling은 프로세스 수가 아니라 **사용자 단위의 CPU 점유율**을 기준으로 자원을 분배하므로, 한 사용자가 많은 프로세스를 생성하더라도 다른 사용자의 CPU 접근권을 보장할 수 있습니다.

즉, Fair Share Scheduling의 핵심은 개별 프로세스의 우선순위보다도 사용자 그룹의 자원 배분 비율을 먼저 고려한다는 점입니다. 이런 특성 때문에 공용 서버, 교육용 실습 서버, 기업용 다중 사용자 환경에서 특히 의미가 큽니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`, `user_id`, 사용자별 할당 비율 또는 quota 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 프로세스가 아닌 사용자 또는 그룹 단위로 CPU 사용량을 관리하므로, 동일 사용자가 많은 프로세스를 생성해도 전체 점유율이 제한됩니다.
- 구현 시, 특징적 고려사항 등: 사용자별 누적 사용량을 주기적으로 추적해야 하며, 사용자 간 quota와 사용자 내부 스케줄링 정책(RR, Priority 등)을 함께 설계해야 합니다.

## 장점

- 시스템 자원을 사용자별로 공정하게 분배할 수 있습니다.
- 특정 사용자가 과도한 수의 프로세스를 생성해도 전체 시스템을 독점하기 어렵습니다.
- 다중 사용자 환경에서 정책 기반의 자원 배분이 가능하므로 서버 운영에 적합합니다.

## 단점

- 구현이 복잡하며, 사용자별 CPU 사용량과 quota를 지속적으로 계산해야 합니다.
- 사용자 간 공정성과 개별 프로세스의 응답 시간 사이에서 trade-off가 발생할 수 있습니다.
- 잘못된 quota 설정은 특정 사용자에게 과도한 지연이나 불필요한 자원 낭비를 유발할 수 있습니다.

# 10. Multiple-Processor Scheduling

## Pseudo Code

```python
// Multiple-Processor(다중 프로세서) 스케줄링의 개략 로직
// - 범위: 단일 칩 멀티코어 + 멀티소켓/멀티칩 시스템 모두 포함
while (System_Is_Running):
    for each Processor in Processors:
        if (Processor.is_idle()):
            // 1) 우선 로컬 런큐에서 선택 (Affinity 유지)
            task = Processor.local_runqueue.pop_front()

            // 2) 로컬 큐가 비면 전역/원격 큐에서 pull
            if (task == null):
                source = Select_Source_Processor_By_Load_And_NUMA()
                task = source.local_runqueue.pop_back()

            // 3) 원격 실행 비용(NUMa/캐시 손실)을 감안해 배치
            if (task != null):
                Processor.dispatch(task)

    // 4) 주기적 부하 균형 (push/pull migration)
    Periodic_Load_Balance()
``` 

## 설명

Multiple-Processor Scheduling은 여러 실행 유닛(코어/프로세서)을 가진 시스템 전체를 대상으로 하는 상위 개념입니다. 즉, 단일 CPU 패키지의 멀티코어뿐 아니라 멀티소켓 서버까지 포함합니다. 핵심은 다음과 같습니다.

- 전역 큐 vs 프로세서별 로컬 큐 전략 선택
- Affinity를 유지하면서도 과부하 코어를 완화하는 마이그레이션 정책
- 멀티소켓 환경에서 NUMA 원격 메모리 접근 비용을 최소화하는 배치

## Case Study

| Task | Arrival | CPU Burst | 메모리 지역성(선호) | 비고 |
|------|---------|-----------|----------------------|------|
| T1   | 0       | 18        | Socket 0             | 메모리 집약 |
| T2   | 0       | 6         | Any                  | 짧은 작업 |
| T3   | 1       | 12        | Socket 1             | 메모리 집약 |
| T4   | 2       | 4         | Any                  | 짧은 작업 |

> 2소켓(S0, S1) 시스템. 각 소켓은 로컬 런큐를 가지며, 유휴 상태일 때만 원격 소켓에서 work stealing을 수행한다.

**배치 흐름도**

```text
시각  이벤트
0     T1, T2가 S0 런큐에 배치됨. T1 실행 시작
1     T3가 S1에 배치되어 즉시 실행 시작
2     T4가 S0 런큐 뒤에 추가됨
13    S1이 유휴 상태가 되자 S0의 뒤쪽 작업 T4를 work stealing
13~17 S1에서 T4 실행 및 완료
18~24 S0에서는 T1 완료 후 T2 실행
```

## 사례 설명 및 분석

이 사례의 핵심은 "전체 시스템 부하 균형"과 "원격 실행 비용" 사이의 균형입니다.

**실행 흐름**

| 시점 | 상태 | 해석 |
|------|------|------|
| t=0  | T1, T2가 S0에 배치되고 T1 실행 시작 | S0에 작업이 몰려 초기 불균형 발생 |
| t=1  | T3가 S1에서 실행 시작 | T3는 Socket 1 선호를 유지하며 locality 확보 |
| t=2  | T4가 S0 런큐 뒤에 추가 | S0 대기열이 더 길어짐 |
| t=13 | S1이 유휴가 됨 | 남는 실행 자원을 활용할 수 있는 시점 |
| t=13 | S1이 S0에서 T4를 steal | 원격 실행 1회를 감수하고 T4 대기시간 감소 |

**결과 요약**

| 항목 | 의미 |
|------|------|
| locality 유지 | T1은 S0, T3는 S1에 남아 메모리 지역성을 유지 |
| work stealing 효과 | T4를 S1로 이동시켜 전체 대기시간을 단축 |
| trade-off | 원격 실행 비용은 증가하지만 시스템 유휴 시간을 줄임 |

즉, 이 수준의 스케줄링에서는 단순히 작업을 고르게 나누는 것보다, NUMA locality를 최대한 보존하면서도 한 소켓이 놀지 않도록 work stealing을 적절히 사용하는 것이 중요합니다.

## 특징

- 개별 입력 요소: `arrival time`, `CPU burst time`, `processor/socket affinity`, `NUMA node`, 마이그레이션 비용 모델
- 동작 포인트: 시스템 전체 균형을 위해 push/pull migration, work stealing, load balancing 주기를 조절
- 구현 포인트: 원격 메모리 접근 비용과 공정성 사이의 균형, 과도한 migration 억제

## 장점

- 대규모 시스템(멀티소켓 포함)에서 전체 처리량을 높이기 유리합니다.
- 특정 프로세서 과부하를 완화해 tail latency를 줄일 수 있습니다.
- NUMA-aware 정책과 결합하면 메모리 성능을 개선할 수 있습니다.

## 단점

- 정책이 복잡하며, 토폴로지(소켓/NUMA) 인지 없이는 성능 변동이 큽니다.
- 원격 실행/빈번한 migration은 캐시 재적재 비용을 유발합니다.
- 튜닝 실패 시 공정성/처리량/응답시간이 동시에 악화될 수 있습니다.

# 11. Multicore Processor Scheduling

## Pseudo Code

```python
// Multicore(단일 칩 내 코어) 스케줄링 개략 로직
// - 핵심: 공유 LLC, SMT 형제 코어, 전력/열 제약까지 고려
def multicore_scheduler(tasks, cores, topology):
    # topology: L3 공유 그룹, SMT sibling 정보 포함
    while has_runnable(tasks):
        for task in ready_queue(tasks):
            # 1) 최근 실행 코어 우선(캐시 warm)
            candidate = task.last_core

            # 2) 같은 LLC 그룹 내 유휴 코어 우선 선택
            if not is_eligible(candidate):
                candidate = pick_idle_core_same_llc(task, topology)

            # 3) SMT sibling 과충돌 회피(두 CPU-bound task 동시 배치 억제)
            candidate = avoid_heavy_smt_pair(candidate, task, topology)

            dispatch(task, candidate)
``` 

## 설명

Multicore Processor Scheduling은 Multiple-Processor의 하위 범주로, "하나의 CPU 패키지 안의 여러 코어" 배치 최적화에 초점을 둡니다. 핵심은 다음과 같습니다.

- 공유 캐시(LLC) 재사용 극대화
- SMT(하이퍼스레딩) sibling 간 자원 충돌 완화
- 코어 packing/spreading 전략으로 성능-전력 균형

## Case Study

| Task | Type | Burst | 특성 |
|------|------|-------|------|
| A    | CPU-bound | 20 | 연산 집중 |
| B    | CPU-bound | 18 | 연산 집중 |
| C    | Cache-sensitive | 10 | L3 재사용 중요 |
| D    | I/O-mixed | 8 | 간헐적 대기 |

> 1소켓 4코어(2개 SMT 쌍) 가정: (C0,C1), (C2,C3)

**배치 흐름도**

```text
코어 토폴로지: (C0, C1) 한 쌍, (C2, C3) 한 쌍

초기 배치
- A -> C0
- B -> C2

추가 배치
- C -> C1  (A와 같은 LLC 그룹 활용)
- D -> C3  (I/O 혼합 작업이라 간섭 부담이 상대적으로 작음)

핵심 결과
- CPU-bound 작업 A, B를 서로 다른 SMT 쌍에 분리
- Cache-sensitive 작업 C는 기존 캐시 지역성을 최대한 재사용
```

## 사례 설명 및 분석

Multicore 관점에서는 "칩 내부 자원 간섭"과 "캐시 재사용"이 성능을 좌우합니다.

**실행 흐름**

| 배치 대상 | 선택 코어 | 이유 |
|-----------|-----------|------|
| A | C0 | CPU-bound 작업을 우선 독립 코어에 배치 |
| B | C2 | A와 다른 SMT 쌍에 배치해 연산 자원 충돌 완화 |
| C | C1 | A가 사용하던 LLC 그룹을 공유해 캐시 재사용 기대 |
| D | C3 | I/O 혼합 작업이므로 sibling 간섭 영향이 상대적으로 작음 |

**결과 요약**

| 항목 | 의미 |
|------|------|
| SMT 충돌 회피 | A와 B를 서로 다른 쌍에 두어 연산 경쟁 완화 |
| LLC 재사용 | C를 C0/C1 그룹에 두어 캐시 miss 감소 기대 |
| 정책 포인트 | 균등 분산보다 토폴로지 인식 배치가 더 중요 |

따라서 멀티코어 스케줄링은 단순 부하 분산이 아니라, 같은 칩 내부에서 어떤 코어가 어떤 자원을 공유하는지까지 고려해 배치해야 성능을 안정적으로 확보할 수 있습니다.

## 특징

- 개별 입력 요소: `arrival time`, `CPU burst time`, `core topology(LLC/SMT)`, `affinity`, `task class`
- 동작 포인트: 같은 칩 내부에서 cache locality와 sibling contention을 동시에 최적화
- 구현 포인트: 코어 packing/spreading 정책, thermal/power 제약 반영

## 장점

- 공유 캐시 재사용으로 IPC 개선 가능
- SMT 간섭을 줄여 지터(jitter)와 tail latency 완화 가능
- 단일 소켓 환경에서 전력 효율적 스케줄링이 가능

## 단점

- 코어 토폴로지 정보를 모르면 오히려 간섭을 키울 수 있습니다.
- 캐시 최적화와 공정성 사이에 충돌이 발생할 수 있습니다.
- 전력/열 제약까지 고려하면 정책 튜닝이 어려워집니다.

## Multiple-Processor vs Multicore 비교 정리

| 구분 | Multiple-Processor Scheduling | Multicore Processor Scheduling |
|------|-------------------------------|--------------------------------|
| 개념 범위 | 상위 개념(멀티소켓/멀티칩 포함) | 하위 개념(단일 칩 내부 코어 중심) |
| 주요 병목 | 소켓 간 이동, NUMA 원격 접근 | SMT 간섭, 공유 캐시(LLC) 충돌 |
| 최적화 초점 | 시스템 전체 부하 균형 | 칩 내부 토폴로지 최적 배치 |
| migration 판단 | 원격 비용 vs 대기시간 | 캐시 warm 유지 vs sibling 충돌 |
| 대표 전략 | work stealing, NUMA-aware balancing | core packing/spreading, LLC-aware placement |
| 주 사용 환경 | 서버/클러스터 노드, 멀티소켓 머신 | 데스크톱/노트북/단일 소켓 서버 |

요약하면, Multicore Scheduling은 Multiple-Processor Scheduling 안에 포함되는 특수 케이스입니다. 전자는 "시스템 전체 분산"이 중심이고, 후자는 "한 칩 내부 미세 배치"가 중심입니다.

# 12. Real-Time Scheduling

## Pseudo Code

```python
// Real-Time Scheduling 알고리즘 예시 (Rate Monotonic Scheduling)
def rate_monotonic_scheduler(processes):
    # 프로세스들을 주기(period)에 따라 우선순위 정렬 (주기가 짧을수록 높은 우선순위)
    processes.sort(key=lambda p: p.period)

    while has_runnable_or_waiting_process(processes):
        now = current_time()
        # 실행 가능한 프로세스 중에서 가장 높은 우선순위를 가진 프로세스 선택
        runnable_processes = [p for p in processes if p.arrival_time <= now and not p.is_completed()]
        if runnable_processes:
            next_process = min(runnable_processes, key=lambda p: p.period)  # 주기가 짧은 프로세스 선택
            execute(next_process)  # 프로세스 실행
``` 

```python
// Real-Time Scheduling 알고리즘 예시 (Earliest Deadline First)
def edf_scheduler(processes):
    while has_runnable_or_waiting_process(processes):
        now = current_time()
        # 실행 가능한 프로세스 중에서 가장 가까운 데드라인을 가진 프로세스 선택
        runnable_processes = [p for p in processes if p.arrival_time <= now and not p.is_completed()]
        if runnable_processes:
            next_process = min(runnable_processes, key=lambda p: p.deadline)  # 데드라인이 가장 가까운 프로세스 선택
            execute(next_process)  # 프로세스 실행
``` 

## 설명

Real-Time Scheduling은 실시간 시스템에서 프로세스 스케줄링을 관리하는 알고리즘입니다. 이 알고리즘은 프로세스의 주기(period)나 데드라인(deadline)을 기반으로 우선순위를 정하여, 시간 제약이 있는 작업이 제때 완료될 수 있도록 보장합니다. 대표적인 Real-Time Scheduling 알고리즘으로는 Rate Monotonic Scheduling과 Earliest Deadline First가 있습니다.
- Rate Monotonic Scheduling은 주기가 짧은 프로세스에게 높은 우선순위를 부여하는 알고리즘입니다. 주기가 짧은 프로세스는 더 자주 실행되어야 하므로, 높은 우선순위를 갖게 됩니다.
- Earliest Deadline First는 데드라인이 가장 가까운 프로세스에게 높은 우선순위를 부여하는 알고리즘입니다. 데드라인이 가까운 프로세스는 더 긴급하게 처리되어야 하므로, 높은 우선순위를 갖게 됩니다.
- 이러한 알고리즘은 실시간 시스템에서 시간 제약이 있는 작업이 제때 완료될 수 있도록 보장하는 데 사용됩니다.

## Case Study

| Process | Arrival Time | Burst Time | Period | Deadline |
|---------|-------------|------------|--------|----------|
| P1      | 0           | 3          | 8      | 8        |
| P2      | 0           | 2          | 5      | 5        |
| P3      | 1           | 2          | 10     | 10       |
| P4      | 2           | 1          | 4      | 4        |

> 시스템에 네 개의 프로세스(P1, P2, P3, P4)가 존재합니다. 각 프로세스는 서로 다른 주기(Period)와 데드라인(Deadline)을 가지고 있습니다. 실시간 시스템에서는 이러한 주기와 데드라인을 만족시켜야 하므로, Rate Monotonic Scheduling(RMS)과 Earliest Deadline First(EDF) 알고리즘을 적용하여 어떻게 다른 스케줄이 생성되는지 비교해보겠습니다.

### Pseudo Execution Timeline Analysis

**시간별 준비 프로세스 상태**

| 시점 | 준비 상태 | 비고 |
|------|---------|------|
| t=0  | P1, P2 준비 | P1, P2 모두 도착 |
| t=1  | P1(실행중), P2(대기), P3 준비 | P3 도착 |
| t=2  | P1(실행중), P2(대기), P3(대기), P4 준비 | P4 도착 |
| t=3  | P2 시작 가능 | P1 완료, P2 대기 중 |
| t=5  | P2, P4 영향 | 주기 갱신 포인트 |

---

## RMS (Rate Monotonic Scheduling) - 정적 우선순위 기반

**우선순위 결정: 주기가 짧을수록 높은 우선순위**

| Process | Period | RMS Priority |
|---------|--------|-------------|
| P4      | 4      | 1 (최고)     |
| P2      | 5      | 2           |
| P1      | 8      | 3           |
| P3      | 10     | 4 (최저)     |

**Gantt Chart for RMS Schedule**

<table>
    <tr>
        <td align="center" style="width:30px"><b>P2</b></td>
        <td align="center" style="width:30px"><b>P4</b></td>
        <td align="center" style="width:60px"><b>P1</b></td>
        <td align="center" style="width:30px"><b>P4</b></td>
        <td align="center" style="width:30px"><b>P2</b></td>
        <td align="center" style="width:30px"><b>P4</b></td>
        <td align="center" style="width:60px"><b>P3</b></td>
        <td align="center" style="width:60px"><b>P1</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">2</td>
        <td align="right">3</td>
        <td align="right">6</td>
        <td align="right">7</td>
        <td align="right">9</td>
        <td align="right">10</td>
        <td align="right">12</td>
        <td align="right">15</td>
    </tr>
</table>

**RMS 실행 흐름 상세**

| 구간 | 실행 | 우선순위 판단 | 상태 |
|------|------|---------|------|
| 0~2  | P2   | P1(period=8), P2(period=5) 준비 → P2 선택 | P2 실행 |
| 2~3  | P4   | P4(period=4) 도착 → P2 선점 | P4 선점, P2 대기 |
| 3~6  | P1   | P4 완료 후, 남은 프로세스 중 period 최단 P2(rem=3) 완료될 때까지 P1 실행 | P1 실행 (P2 완료 t=5) |
| 6~7  | P4   | P4 주기 갱신(t=4,8→다음), 현재 P4(period=4, 2nd instance) 준비 | P4 재진입 |
| 7~9  | P2   | P2 주기 갱신(t=5,10), P2(period=5, 2nd instance) 준비 | P2 재진입 |
| 9~10 | P4   | P4(period=4, 3rd instance) 준비 | P4 3번째 인스턴스 |
| 10~12| P3   | P3(period=10) 준비 → period가 가장 길지만 다른 프로세스 완료 후 실행 | P3 실행 |
| 12~15| P1   | P1(period=8, 2nd instance) 준비 → 2번째 주기의 P1 실행 | P1 2번째 주기 |

**RMS 완료 및 데드라인 충족 여부**

| Process | 완료 시간 | Deadline | Deadline Miss? | 비고 |
|---------|----------|----------|---|------|
| P1 (1st) | 6        | 8        | ✓ 만족 | t=6 ≤ 8 |
| P2 (1st) | 5        | 5        | ✓ 만족 | t=5 = 5 (직전 완료) |
| P3 (1st) | 12       | 10       | ✗ 위반 | t=12 > 10 (Deadline Miss!) |
| P4 (1st) | 3        | 4        | ✓ 만족 | t=3 ≤ 4 |
| P4 (2nd) | 7        | 8        | ✓ 만족 | t=7 ≤ 8 |
| P4 (3rd) | 10       | 12       | ✓ 만족 | t=10 ≤ 12 |

---

## EDF (Earliest Deadline First) - 동적 우선순위 기반

**우선순위 결정: 데드라인이 가까울수록 높은 우선순위 (매 시점에 재계산)**

**Gantt Chart for EDF Schedule**

<table>
    <tr>
        <td align="center" style="width:30px"><b>P2</b></td>
        <td align="center" style="width:30px"><b>P1</b></td>
        <td align="center" style="width:30px"><b>P4</b></td>
        <td align="center" style="width:30px"><b>P1</b></td>
        <td align="center" style="width:30px"><b>P2</b></td>
        <td align="center" style="width:60px"><b>P3</b></td>
        <td align="center" style="width:30px"><b>P4</b></td>
        <td align="center" style="width:30px"><b>P1</b></td>
        <td align="center" style="width:30px"><b>P4</b></td>
    </tr>
    <tr>
        <td align="left">0</td>
        <td align="right">2</td>
        <td align="right">4</td>
        <td align="right">5</td>
        <td align="right">7</td>
        <td align="right">9</td>
        <td align="right">11</td>
        <td align="right">12</td>
        <td align="right">14</td>
        <td align="right">15</td>
    </tr>
</table>

**EDF 실행 흐름 상세**

| 구간 | 실행 | 데드라인 판단 | 상태 |
|------|------|---------|------|
| 0~2  | P2   | P1 deadline=8, P2 deadline=5 → P2 선택 (더 급함) | P2 우선 |
| 2~4  | P1   | P2 완료 후, P1 deadline=8, P3 deadline=10 → P1 선택 | P1 실행 |
| 4~5  | P4   | P4 도착 deadline=4 → 현재 가장 긴급 | P4 선점 |
| 5~7  | P1   | P4 완료 후, P1 deadline=8, P3 deadline=10 → P1 계속 | P1 재개 |
| 7~9  | P2   | P2 주기 갱신 deadline=10 (2nd), P1 deadline=8 강제 휴지→P2 진입, P1 남은 1ms | P2 재진입 |
| 9~11 | P3   | P3 deadline=10 (가장 긴급하지는 않으나 준비) → P1 완료 깁보 보류, P2 완료 후 P3 선택 | P3 실행 |
| 11~12| P4   | P4 주기 갱신 deadline=8 (2nd, t=2+4=6 경과하면 8) → 데드라인 재계산 시 상위 우선순위 변경 가능 | P4 재진입 |
| 12~14| P1   | P1 주기 갱신 deadline=16 (2nd) → 데드라인 충분히 멀음 | P1 2번째 주기 |
| 14~15| P4   | P4 deadline (3rd instance) 계산 필요 | P4 인스턴스 |

**EDF 완료 및 데드라인 충족 여부**

| Process | 완료 시간 | Deadline | Deadline Miss? | 비고 |
|---------|----------|----------|---|------|
| P1 (1st) | 7        | 8        | ✓ 만족 | t=7 ≤ 8 |
| P2 (1st) | 2        | 5        | ✓ 만족 | t=2 ≤ 5 |
| P3 (1st) | 11       | 10       | ✗ 위반 | t=11 > 10 (Deadline Miss!) |
| P4 (1st) | 5        | 4        | ✗ 위반 | t=5 > 4 (Deadline Miss!) |
| P4 (2nd) | 12       | 8        | ✗ 위반 | t=12 > 8 (Deadline Miss!) |
| P4 (3rd) | 15       | 12       | ✗ 위반 | t=15 > 12 (Deadline Miss!) |

## 사례 설명 및 분석

이 사례는 4개의 프로세스가 서로 다른 주기와 데드라인을 가질 때, **RMS와 EDF가 서로 다른 스케줄을 생성**하고 **Deadline Miss 발생 여부가 달라지는** 실제 시나리오를 보여줍니다.

### 핵심 비교: RMS vs EDF

#### 1. **우선순위 결정 방식의 차이**

| 측면 | RMS | EDF |
|------|-----|-----|
| 우선순위 유형 | **정적(Static)** - 변경 불가 | **동적(Dynamic)** - 매 시점 재계산 |
| 결정 기준 | 프로세스 주기(Period) | 현재 데드라인(Deadline) |
| 계산 시점 | 프로세스 생성 시 1회만 | 매 스케줄링 시점마다 갱신 |
| 유연성 | 낮음 (고정됨) | 높음 (상황 반응적) |

#### 2. **스케줄 결과 분석**

**RMS 스케줄:**
- t=0~2: P2 실행 (Period 5 < Period 8)
- t=2~3: P4 도착 (Period 4 < Period 5, 선점 발생)
- t=3~6: P1 실행 (P2 완료 후, Period 8)
- t=6~7: P4 재진입 (2nd instance, Period 4 갱신)
- t=7~9: P2 재진입 (2nd instance, Period 5 갱신)
- t=9~10: P4 재진입 (3rd instance)
- t=10~12: P3 실행 (Period 10, 가장 우선순위 낮음)
- t=12~15: P1 재진입 (2nd instance)

**결과: Deadline Miss 1건** (P3: deadline 10 > 완료 12)

**EDF 스케줄:**
- t=0~2: P2 실행 (Deadline 5 < Deadline 8)
- t=2~4: P1 실행 (Deadline 8 < Deadline 10)
- t=4~5: P4 도착 선점 (Deadline 4 가장 긴급)
- t=5~7: P1 계속 (Deadline 8)
- t=7~9: P2 재진입 (2nd deadline 10)
- t=9~11: P3 실행 (준비 프로세스 중 상대적으로 긴급)
- t=11~12: P4 재진입 (2nd deadline 재계산)
- t=12~14: P1 재진입 (2nd deadline 16)
- t=14~15: P4 재진입 (3rd instance)

**결과: Deadline Miss 4건** (P3, P4 multiple instances)

#### 3. **스케줄 특성 해석**

| 항목 | RMS | EDF |
|------|-----|-----|
| 주기 기반 정렬 | P4(4) > P2(5) > P1(8) > P3(10) | 매 시점 동적 재계산 |
| 우선순위 안정성 | 고정, 예측 가능 | 변동, 적응적 |
| Deadline Miss 건수 | 1건 | 4건 |
| 적응성 | 낮음 (주기만 고려) | 높음 (deadline 직접 반영) |

이 역설적 결과는 **우선순위 역위(Priority Inversion) 현상**이 데드라인 완화에 도움이 될 수 있음을 시사합니다. RMS는 짧은 주기의 P4를 우선시하여 반복 수행하므로, 누적 이행 시간이 상대적으로 짧습니다. 반면 EDF는 매 시점 가장 긴급한 작업을 선택하지만, 이것이 전체 시스템의 주기적 갱신 사이클에 최적화되지 않으면 **나중에 도착한 프로세스의 인스턴스가 누적되어 Deadline Miss가 증가**할 수 있습니다.

#### 4. **실제 적용 가이드라인**

- **RMS 선택:** 주기가 일정하고 예측 가능한 산업용/임베디드 시스템 (주기 갱신 패턴이 규칙적)
- **EDF 선택:** 데드라인이 명확하고 주기 변동이 있는 멀티미디어/데이터센터 워크로드 (deadline-driven 요구사항)
- **하이브리드:** 주기와 deadline을 모두 추적하여, 동적으로 알고리즘 전환

**핵심 교훈:** 이 사례에서는 RMS가 더 나은 결과를 보였지만, 실제 시스템에서는 프로세스 특성(주기 규칙성, deadline 분포)에 따라 결과가 뒤바뀔 수 있습니다. 따라서 시스템 요구사항을 정확히 분석한 후 알고리즘을 선택하는 것이 중요합니다.

## 특징

- 특정 알고리즘별 개별 입력 요소: `arrival time`, `CPU burst time`, `period`, `deadline`이 필수이며, 선점형 정책 정보가 필요합니다.
- 독특한 동작 방식 혹은 현상: 프로세스의 주기(period)나 데드라인(deadline)을 기반으로 우선순위를 정하여, 시간 제약이 있는 작업이 제때 완료될 수 있도록 보장합니다.
- 구현 시, 특징적 고려사항 등: 실시간 시스템에서 시간 제약이 있는 작업이 제때 완료될 수 있도록 보장하는 것이 중요합니다. 또한, 프로세스의 주기나 데드라인을 정확히 관리하여 스케줄링이 올바르게 이루어지도록 해야 합니다.

## 장점

- 실시간 시스템에서 시간 제약이 있는 작업이 제때 완료될 수 있도록 보장할 수 있습니다.
- 프로세스의 주기나 데드라인을 기반으로 우선순위를 정하여 스케줄링할 수 있습니다.
- 다양한 실시간 스케줄링 알고리즘을 적용하여 시스템 요구사항에 맞게 스케줄링할 수 있습니다.

## 단점

- 구현이 복잡하며, 프로세스의 주기나 데드라인을 정확히 관리해야 합니다.
- 실시간 시스템에서 시간 제약이 있는 작업이 제때 완료되지 않는 경우, 시스템 전체의 안정성이 저하될 수 있습니다.
- 특정 알고리즘이 모든 실시간 시스템에 적합하지 않을 수 있으며, 시스템 요구사항에 맞는 알고리즘을 선택하는 것이 중요합니다.
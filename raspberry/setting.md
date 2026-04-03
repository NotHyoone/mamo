# 라즈베리 파이 설정

## 기본 명령어 Alias (`~/.bashrc`)

```bash
# vi ~/.bashrc 열어서 아래 내용 추가

# 파일 목록
alias ls='ls --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# 실수 방지 (삭제/이동 시 확인 메시지)
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# 자주 쓰는 명령어
alias update='sudo apt update && sudo apt upgrade -y'
alias cls='clear'
alias myip='hostname -I'
```

---

## 고정 IP 설정

설정 파일 열기:
```bash
sudo vi /etc/dhcpcd.conf
```

아래 내용 추가:
```
interface wlan0
static ip_address=165.229.229.117/24
static routers=165.229.228.117
static domain_name_servers=8.8.8.8
```

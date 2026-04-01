# 라즈베리 파이 설정

# 기본 명령어 보강
" vi ~/.bashrc
alias ls='ls --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# 실수 방지 (삭제/이동 시 확인 메시지)
" vi ~/.bashrc
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# 라즈베리 파이 전용/자주 쓰는 명령
" vi ~/.bashrc
alias update='sudo apt update && sudo apt upgrade -y'
alias cls='clear'
alias myip='hostname -I'

# 고정 IP 설정
" 설정 파일 sudo vi /etc/dhcpcd.conf
interface wlan0
static ip_address=165.229.229.117/24
static routers=165.229.228.117
static domain_name_servers=8.8.8.8

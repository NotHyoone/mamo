" --- vim-tiny version ---
" vi ~/.vimrc 입력 후 아래 내용 복사 붙여넣기
set number          " 왼쪽 줄 번호 표시
set ai              " 자동 들여쓰기 (Auto Indent)
set si              " 스마트 들여쓰기 (Smart Indent)
set cindent         " C언어 스타일 들여쓰기 (컴공 필수!)
set shiftwidth=4    " 자동 들여쓰기 너비 4칸
set tabstop=4       " 탭 간격 4칸
set ignorecase      " 검색 시 대소문자 무시
set hlsearch        " 검색 결과 강조 (하이라이트)
set nocompatible    " 방향키 문제 해결 (중요)
set bs=indent,eol,start  " 백스페이스 정상 작동 설정
set ruler           " 커서 위치 표시
set laststatus=2    " 상태 표시줄 항상 표시
syntax on           " 코드 구문 강조 (Syntax Highlighting)
filetype indent on  " 파일 종류에 따른 들여쓰기 활성화

" 한글 주석 깨질 때
set encoding=utf-8
set fileencodings=utf-8,cp949

" --- vim ~/.vimrc 버전 ---
" 문법 강조 및 색상 테마
syntax on
colorscheme desert  " 기본 내장 테마 중 하나인 desert 적용

" 인터페이스 설정
set number           " 줄 번호 표시
set cursorline       " 현재 줄 강조
set laststatus=2     " 상태 표시줄 활성화
set showcmd          " 입력 중인 명령어 표시

" 편집 및 들여쓰기
set autoindent
set cindent
set tabstop=4
set shiftwidth=4
set expandtab        " 탭을 공백으로 변환

" 검색 설정
set hlsearch         " 검색 결과 하이라이트
set ignorecase       " 대소문자 무시
set smartcase        " 대문자 포함 시 대소문자 구분

" 기타
set history=1000     " 명령어 기록 저장 개수
set clipboard=unnamedplus " 시스템 클립보드 공유 (지원되는 경우)
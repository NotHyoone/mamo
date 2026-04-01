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
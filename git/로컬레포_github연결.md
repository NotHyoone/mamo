# GitHub에서 새로운 레포지토리 생성 후 로컬 저장소와 연결하는 방법입니다.

# A. 첫 커밋 후 연결할 경우

# 1. 초기화 (이미 했으면 생략 가능)
git init

# 2. 파일 스테이징 및 커밋
git add .
git commit -m "first commit"

# 3. 기본 브랜치 이름을 main으로 설정 (선택 사항, 권장)
git branch -M main

# 4. GitHub 저장소와 로컬 연결 (생성한 URL 복사해서 넣기)
git remote add origin https://github.com

# 5. 원격 저장소로 푸시
git push -u origin main


# B. GitHub 저장소가 이미 존재하는 경우 (README 등으로 인해 충돌이 발생할 수 있음)

# 1. 원격 저장소 연결
git remote add origin https://github.com

# 2. 원격 저장소의 내용을 가져와서 합치기 (README 등 존재 시)
git pull origin main --allow-unrelated-histories

# 3. 푸시
git push -u origin main

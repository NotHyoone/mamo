# 로컬 저장소 ↔ GitHub 연결 방법

## A. 로컬에서 시작하는 경우 (새 프로젝트)

```bash
# 1. 초기화 (이미 했으면 생략)
git init

# 2. 파일 추가 및 커밋
git add .           # 모든 파일 추가
git add <file>      # 특정 파일 추가
git add -p          # 변경된 부분만 선택적으로 추가

git commit -m "커밋 메시지"

# 3. 기본 브랜치 이름을 main으로 설정 (권장)
git branch -M main

# 4. GitHub 원격 저장소 연결
git remote add origin https://github.com/<username>/<repo>.git

# 5. 원격 저장소로 푸시
git push -u origin main
git push origin main
```

---

## B. GitHub 저장소가 이미 존재하는 경우

> README 등이 이미 있어 충돌이 발생할 수 있을 때 사용

```bash
# 1. 원격 저장소 연결
git remote add origin https://github.com/<username>/<repo>.git

# 2. 원격 내용 가져오기 (히스토리가 다를 때)
git pull origin main --allow-unrelated-histories

# 3. 푸시
git push -u origin main
git push origin main
```

---

## C. 이미 존재하는 레포지토리 클론

```bash
git clone https://github.com/<username>/<repo>.git
```

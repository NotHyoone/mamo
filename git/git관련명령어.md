# Git 관련 명령어

## 기본 설정

```bash
git config --global user.name "새로운 이름"
git config --global user.email "새로운 이메일"
```

---

## 기본 커밋

```bash
git add .
git commit -m "커밋 메시지"
```

---

## 커밋 메시지 수정

```bash
git commit --amend -m "수정된 커밋 메시지"
git push origin main
```

---

## 파일 이동 및 이름 변경

```bash
git mv <현재_파일명> <새로운_경로/파일명>
git commit -m "파일 이동 및 이름 변경"
git push origin main
```

---

## Alias 설정

```bash
git config --global alias.<별명> "<실제 명령어>"   # alias 설정
git config --global alias.st status               # 예시: git st → git status

git config --unset alias.<별명>                    # alias 제거 (로컬)
git config --global --unset alias.<별명>           # alias 제거 (글로벌)

git config --global --get-regexp alias             # 설정된 alias 전체 확인
git config --global --edit                         # alias 설정 파일 직접 편집
```

```bash
vi ~/.bashrc  # alias 설정을 .bashrc에 추가하여 영구적으로 사용
source ~/.bashrc  # 변경 사항 적용
// 예시: alias gs='git status' → 터미널에서 gs 입력 시 git status 실행
```

## Merge 충돌 해결

```bash
git merge <브랜치명> # 충돌 발생 시, 충돌된 파일을 열어 수정 후
git add <수정된_파일>
git commit -m "Merge 충돌 해결"
```

# Git 캐시 제거
```bash 
git rm -r --cached .
git add .
git commit -m "캐시 제거 및 재추가"
git push origin main
```

# Git 브랜치에서 main에 병합
```bash
git checkout main
git merge <브랜치명>
git push origin main
```

# Git 브랜치 삭제
```bash
git branch -d <브랜치명>  # 로컬 브랜치 삭제
git push origin --delete <브랜치명>  # 원격 브랜치 삭제
```

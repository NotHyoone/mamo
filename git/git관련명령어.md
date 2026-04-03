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
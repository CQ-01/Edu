# Github 2일차
## Github 프로필 만들기
1. Github에서 유저명으로 repo 생성
2. 홈폴더에서 유저명 폴더 생성
3. 유저명 폴더에서 `git init`
4. README.md 파일에 자기소개 작성
5. 커밋하여 변경사항 기록

## 원격저장소 내용 가져오기
### Clone
`git clone <원격저장소 주소>`
- 원격저장소 복제해 로컬에 생성
- 처음 한번만 실행
### Pull
`git pull <저장소이름> <브랜치이름>`
- 원격저장소의 변경사항 가져오기

## Gitignore
- 특정 파일/폴더에 대해 버전관리 제외 하는 것
- 파일명 .gitignore로 작성
- .git 폴더와 동일한 위치에 생성
- 반드시 git add 전에 .gitignore에 작성
- [gitignore.io](https://gitignore.io/)
- [gitignore 저장소](https://github.com/github/gitignore)

## Branch
- 원본(master)에 독립된 공간
### git branch
```bash
git branch
# 브랜치 목록 확인
git branch-r
# 원격 저장소의 브랜치 목록 확인
git branch <이름>
# 새로운 브랜치 생성
git branch <이름> <커밋ID>
# 특정 커밋 기준으로 브랜치 생성
git branch -d <이름>
# 병합된 브랜치만 삭제
git branch -D <이름>
# 모든 브랜치 강제 삭제
```
### git switch
```bash
git switch <이름>
# 다른 브랜치로 이동
git switch -c <이름>
# 새 브런치 생성 및 이동
git switch -c <이름> <커밋ID>
# 특정 커밋 기준으로 브런치 생성 및 이동
```
## Brunch-merge
### git merge
- 분기된 브랜치 합치기
- `git merge <합칠 브랜치>`
- 합치려는 main 브랜치로 switch 후 `git merge`
### merge conflict
- 두 브런치에서 동일 파일의 동일 위치를 수정한 경우 발생하는 충돌
- 사용자가 선택 후 문제해결
## Git Workflow
### 원격저장소 소유권이 있는 경우

- 원격저장소를 로컬로 clone

`git clone <원격주소>`

- 브런치를 생성하고 기능 구현
`git switch -c <브런치명>`

- 원격저장소에 해당 브런치 push
`git push origin <브런치명>`

- pull request를 통해 master에 반영 요청

- 병합이 완료된 브랜치는 원격저장소에서 삭제

- 각 사용자는 로컬의 master 브랜치 이동

`git switch master`
- 변경된 내용 로컬에 받기

`git pull origin master`
- 기존의 로컬 브랜치 삭제

`git branch -d <브런치명>`

### 원격저장소 소유권이 없는 경우
- 소유권이 없는 원격저장소를 fork를 통해 내 원격저장소로 복제
- 복제된 내 원격 저장소를 로컬 저장소에 clone
  
`git clone <내 원격저장소 주소>`
- 로컬저장소와 원본 원격저장소 동기화

`git remote add upstream <원격저장소 주소>`
- 브랜치 생성 후 기능구현

`git switch -c <브랜치명>`
- 복제 원격 저장소에 push

`git push origin <브랜치명>`
- pull request를 통해 원본 원격 저장소 master에 반영요청
- 원본에 병합되면 복제 원격저장소의 브런치는 삭제 후 master브런치로 이동

`git switch master`
- 변경내용 원본 원격저장소에서 로컬에 받기

`git pull upstream master`
- 기존 로컬 브랜치 삭제
`git branch -d <브랜치명>`
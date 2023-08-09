## Git 초기 설정
- 이름과 이메일 설정/재설정
```bash
$ git config --global user.name "이름"
$ git config --global user.email "메일 주소"
```
- 설정 상태 확인
```bash
$ git config --global --list
```

## Git 기본 명령어
1. 로컬저장소
   - Working Directory : 사용자의 일반적인 작업이 일어나는 곳
   - Staging Area : 커밋을 위한 파일 및 폴더가 추가되는 곳
   - Repository : Staaging area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳
   - Working Directory → Staging Area → Repository의 과정으로 버전관리 수행

2. git init
- 작업중인 디렉토리를 git으로 관리
- 터미널에 (master) 표시
- 이미 Git저장소인 폴더 내에 또 다른 Git 저장소 만들지 않기
- 홈 디렉토리에서 git init 절대 하지 않기
3. git status
- Working Directory와 Staging Area에 있는 파일의 현재 상태 확인
- Untracked : Git이 관리하지 않는 파일
- Tracked : Git이 관리하는 파일
  - Unmodified : 최신상태
  - Modified : 수정되었지만 아직 Staging Area에는 반영하지 않는 상태
  - Staged : Staging Area에 올라간 상태

4. git add
```bash
# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add my_folder/

# 현재 디렉토리에 속한 파일/폴더 전부
$ git add . 
```
- Working Directory의 파일을 Staging Area로 업로드
- Untracked, Modified → Staged로 변경

5. git commit
```bash
$ git commit -m "first commit"
 ```
- Staging Area에 올라온 파일의 변경사항을 하나의 커밋으로 저장
- 커밋메시지는 변경사항을 잘 나태낼 수 있도록 의미있게 작성

6. git log
- 커밋의 내역을 조회
  - -oneline : 한줄로 축약
  - -graph : 브랜치와 머지내역을 그래프로 표현
  - -all : 모든 브랜치 내역
  - -reverse : 커밋내역 역순으로 표현
  - -p : 파일의 변경내용도 포함
  - -2 : 임의의 갯수만큼 내역 표시

# Github
## 원격저장소 (Remote Repository)
1. Github에서 원격저장소 생성
   (New Repository)
2. git init
- 폴더를 로컬저장소 지정
3. git remote
- 로컬저장소에 원격저장소를 등록, 조회, 삭제 가능
  - 등록 : git remote add 이름(origin) (원격주소)
  - 조회 : git remote -v
  - 삭제 : git remote rm 이름
  `* 로컬과 연결을 끊는 것, 원격저장소 삭제 X`

4. 원격저장소 업로드
   - 로컬저장소에서 커밋 생성
  ```bash
  $ git status
  $ git add day1.md
  $ git commit -m "설명"
  $ git log --oneline
  ```

   - 생성된 커밋 업로드하기
  ```bash
  $ git push origin master
  $ git push
  ```

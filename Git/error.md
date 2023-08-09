### 다른 변경사항과의 충돌 오류
- bash창에서 linux 커맨드를 이용하여 적용할 branch 선택하여 해결
- 먼저 git pull로 원격 저장소 파일을 내려받아 해결

### push, commit등 동작이 없는 오류
```bash
Another git process seems to be running in this repository
```
- git process가 다른 곳에서 동작하고 있어서 안됨
- process를 강제종료 시키면 해결
  - cmd : `rm -f ./.git/index.lock` 
  - powershell : `Remove-Item -Path "./.git/index.lock" -Force`

### 용량 제한 오류
- 100mb 이상의 파일 push 할때 깃허브 에러 발생
- Git LFS 기능 활용 시도 결과 성공
  - Git LFS 다운로드
  - 대용량 파일 .gitignore에 입력
  - `git lfs track "폴더경로"`

### 로컬에 없는 데이터를 push 하려는 오류
- 로컬 파일 및 커밋 내의 파일 삭제 커맨드 입력결과 실패
- git 파일을 삭제했다가 새로 remote연결하여 해결

### 원격저장소에 파일이 있을때 로컬저장소 연결하기
- master가 아닌 main이 default 브랜치로 설정되어 있음
- 깃로그에선 바꾼 날짜로 나오나 깃허브에서는 두 브랜치 모두 본래 날짜로 나옴
  - 날짜 바꾼 깃로그가 코드나 정보가 들어간게 아니라 레포 수정이라 적용이 안된듯?
- 깃허브 계정 기본 브랜치 이름 설정이 main으로 되어 있음
- 평소에는 직접 git bash에 master로 입력했기에 master로 저장된 듯
- 기본 설정 master로 하고 pull 땡기니 이상없음
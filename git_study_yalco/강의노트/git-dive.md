## 깃 깊이 알기

**snapshot 방식을 사용**
svn 등은 델타 방식

델타: 변경점만 저장
snapshot: 지금 현재시점의 최종상태를 저장

델타 방식은 관리 역사가 길어질수록 여태까지의 모든 변경사항을 더해야 해서 느려짐

**분산 버전 관리**
중앙집중식이면 버전정보는 원격 서버에만 저장됨
분산버전 : 모든 구성원이 버전정보를 로컬에도 가지고있음


## 깃의 3가지 공간
working directory: untracked / tracked 데이터들
staging area: 커밋 될 항목이 존재 (add한 것)
repository: 커밋 된 항목이 존재

### 파일의 삭제와 이동

그냥 삭제하면 파일의 삭제가 working directory에 있음
git rm으로 삭제하면 staging area에 있음
그냥 이름변경/이동하면 working directory에 있고, 삭제 - 추가로 인식
git mv로 하면 바로 staging area에 renamed

### staging area 에서 다시 working directory로
git restore --staged (파일명)
--staged 옵션을 빼면 working directory에서도 변경이 제거됨
(이전: git reset HEAD 파일명)


### reset의 세 가지 옵션
working directory에서도 삭제: --hard
working directory에는 남김: --mixed(default) 
staging area까지 남김: --soft 

## git head

* head: 현재 속한 브랜치의 가장 최신 커밋
switch하면 head로 간다

**checkout**
히스토리 내용은 그대로 두고, 파일 상태만 이전으로

git checkout HEAD^ 등으로 돌아갈 수 있음
git checkout - 는 실행취소
이건 익명 브랜치를 만들어 사용하는 것처럼 동작함

이전 시점에서 분기되는 branch 제작 등에 사용

## fetch vs pull
fetch: 원격 저장소의 최신 커밋을 로컬로 가져오기만 함
pull: fetch한 후 merge or rebase

-> fetch해서 미리 가져온 후 checkout origin/main으로 확인 가능

새 브랜치도 비슷하게 확인할 수 있음
fetch -> checkout으로 확인 이후에 git switch -t origin/~ 하면 됨
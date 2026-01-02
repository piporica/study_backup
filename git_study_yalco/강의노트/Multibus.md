## 차원 넘기
* branch 

- 프로젝트를 하나 이상의 모습으로 관리하기
- 여러 작업이 각각 독립적으로 진행될 때

checkout이 switch와 restore로 분리됨
switch : 브랜치간 이동

생성과 동시에 이동하기
git switch -c (브랜치이름)

삭제: git branch -d 브랜치명
강제삭제 -D
이름바꾸기 -m 


전체 로그 보기 
git log --all --decorate --oneline --graph


## Merge vs Rebase
Merge: 두 브랜치를 이어붙임
-> 브랜치의 사용내역이 남음

Rebase: 다른 브랜치에 이어붙이기
-> 히스토리가 한줄로 정리됨
-> 이미 팀원에게 공유한 커밋에 대해서는 사용하지 말 것!

### Merge 병합
: 합쳐져서 주 대상이 될 브랜치로 이동
git merge (합칠 대상 브랜치)
머지하면 머지된 브랜치는 머지 직전이 head인 상태로 남음
(다썼고 필요없으면 지울 것)


### Rebase (재배치)
: 재배치할 브랜치로 이동 
git rebase (주 브랜치)
주 브랜치의 head는 재배치된 commit들 이전에 있음
-> 이걸 끌고오려면 주 브랜치로 이동해서 앞의 브랜치를 머지함
그럼 head가 같아짐
이후 서브 브랜치를 삭제


## 충돌 해결하기
파일의 같은 위치에 다른 내용이 입력된 경우

### Merge
병합 시도하면 MERGING 상태로 들어가고 두 상태가 >>>> 등으로 표시됨
이상태에서 git merge --abort 하면 취소
충돌 해결 후에는 git add . 후 git commit (커밋메시지 자동입력됨)


### Rebase
-> 머지처럼 한번에 모든 충돌을 해결하는 게 아니라 커밋마다 해결해야함
 안되겠으면 git rebase --abort로 취소
 해결하면 git add . -> 커밋이 아니라 rebase --continue
 (이 때 current 선택하면 그 마디는 커밋으로 추가 안 됨)
 이후 일반 rebase처럼 merge 후 쓸데없는 브랜치 삭제


 rebase 충돌해결은 에지간하면 cli로 하자!
 (버전마다 약간씩 달라지기 때문)
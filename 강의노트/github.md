# github

토큰 만들어서 윈도우 자격증명에 넣기
맥은 키체인에 넣으면됨

클래식 쓰느게 마음이 편하네용

push -u
: 원격 저장소 

기존 폴더를 git에 올리기 -> origin 추가 후 push
기존 레포를 로컬에 받기 -> git clone


## push & pull

push -> 내 변경사항 밀어넣기
pull -> 원격 변경사항 당겨오기

### pull의 두 가지 방법
1. git pull --no-rebase : merge 방식 
2. git pull --rebase : rebase 방식
: 원격의 main에 내 작업들을 재배치시킴
* 기본 git pull => git fetch + git merge


충돌 발생 시 rebase / merge 다 사용가능하지만
rebase의 경우 필요없는 커밋이 없어지며 수가 달라질 수 있음


pull 받는 상황의 rebase는 협업 시에도 상관없음

* 강제push 
--force 
-> 걍 밀어버림 
: 협업 시에는 주의하기

### 원격 branch  관리
새 브랜치를 만들면 어디로 올려야할 지 몰라서 못올림
세팅해줘야함
--set-upstream 
-u

git branch --all
git branch -a
로 확인가능

원격의 브랜치 변화(및 다른 변화)를 확인 -> git fetch
원격의 브랜치 받아오기
git switch -t origin/from-remote


원격 브랜치 삭제
git push (원격 이름) --delete (브랜치명)

원격 여러개 가능함
(하나는 깃헙, 하나는 깃랩...등)

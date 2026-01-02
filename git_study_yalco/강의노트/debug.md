## log

git log -p :상세내역
git log -숫자 : n개만 보기
--stat : 통계와 함께
--shortstat :짧게
--oneline : 개짧게
-S (검색어) -> 변경사항 내 검색
git log --grep (검색어) -> 커밋 메시지 내 검색


git log --all --decorate --oneline --graph
-> 그래픽으로 보여주기

포맷
git log --graph --all --pretty=format:'%C(yellow) %h  %C(reset)%C(blue)%ad%C(reset) : %C(white)%s %C(bold green)-- %an%C(reset) %C(bold red)%d%C(reset)' --date=short

## diff
git diff : **워킹 디렉토리**의 변경사항 확인
파일명만 => --name-only

stage 올라가면 diff로는 안나옴 -> --staged (=--cached)

커밋간 변경사항 비교
git diff 커밋id 커밋id
git diff HEAD~ HEAD~15
git diff 브랜치1 브랜치2 

## 누가 코딩했는지 확인하기
git blame 파일명
-> 각 라인을 누가 썼는지 확인가능

특정 부분만 확인하기
git blame -L (시작줄) (끝줄, 또는 +줄수) (파일명)

gitLens 확장 써보기

## 오류가 발생한 시점 찾아내기
git bisect
이진탐색 알고리즘으로 어디가 문젠지 찾아냄
어느 커밋부터 문제인지?

git bisect start로 시작
checkoit으로 의심지점으로 이동
문제없으면 good 
오류 날 시 bad
반복 -> 문제지점 확인되면 해당 커밋 내용 보여줌
끝나면 git bisect reset


## 시간여행하기

- git add . 
(*로 하면 .gitignore가 씹힘. 왤까)


* Vi 입력 모드로 진입 - Vim 강좌 (https://www.yalco.kr/10_vim/)
작업	Vi 명령어	상세
입력 시작	i	명령어 입력 모드에서 텍스트 입력 모드로 전환
입력 종료	ESC	텍스트 입력 모드에서 명령어 입력 모드로 전환
저장 없이 종료	:q	
저장 없이 강제 종료	:q!	입력한 것이 있을 때 사용
저장하고 종료	:wq	입력한 것이 있을 때 사용
위로 스크롤	k	git log등에서 내역이 길 때 사용
아래로 스크롤	j	git log등에서 내역이 길 때 사용


git commit -am "메시지"
-> 커밋과 함께 add (Untracked 없을 경우 한정)


## reset vs revert 
* reset: 이후의 행적을 삭제
* revert: 이후의 행적을 반대로 수행하는 커밋을 추가

revert: 
- 기록을 남겨야 하는 때
- 직전이 아닌 더 이전 코드를 실행취소 할 때

한번 원격에 push한 코드를 reset하면 안됨!


### reset
git reset --hard (돌아갈 커밋의 해시)
: 입력하지 않을 경우 head로


### revert 
: 돌이킬 커밋의 해시를 찾아야됨
메시지는 기본으로 적혀있긴함
이후 변화를 유지
협업할 때에는 revert!

이후 변화와 충돌이 있다면 reverting으로 들어감
삭제하거나 add하여 --continue 하면됨

만약 다른 변경사항을 추가하고 싶으면
git revert --no-commit 을 추가

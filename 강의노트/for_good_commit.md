# 커밋 잘 하기

커밋 권장사항
:하나의 커밋에는 한 단위의 작업을 넣도록 하기
- 한 작업을 여러 버전에 걸쳐 커밋하지 않기
- 여러 작업을 한 버전에 커밋하지 않기

## 커밋 메시지 컨벤션 
type: subject

body (optional)
...
...
...

footer (optional)

EX)
feat: 압축파일 미리보기 기능 추가

사용자의 편의를 위해 압축을 풀기 전에
다음과 같이 압축파일 미리보기를 할 수 있도록 함
 - 마우스 오른쪽 클릭
 - 윈도우 탐색기 또는 맥 파인더의 미리보기 창

Closes #125


## 타입
타입	설명
feat	새로운 기능 추가
fix	    버그 수정
docs	문서 수정
style	공백, 세미콜론 등 스타일 수정
refactor	코드 리팩토링
perf	성능 개선
test	테스트 추가
chore	빌드 과정 또는 보조 기능(문서 생성기능 등) 수정

breaking point가 있거나 이슈의 해결 작업이면 푸터에 작성

이모지 쓰려면->
gitmoji 사이트에서 가이드 확인

-----

## 좀 더 세심한 스테이징

내용 확인하며 hunk별로 스테이징하기
git add -p

git commit -v : 상세 추가
상세만 미리 보려면 git diff --staged

## STASH
커밋하기 애매한 변화 stash하기
stash -> stash pop

골라서 할 수도 있음 
stash -p

메시지도 남길 수 있음

목록 보기 stahsh list

목록에서 하나씩 적용할 수도 있음
apply + drop = pop

브랜치에 전부 치우기
git stash branch (브랜치명)

다 지우기
clear


## 커밋 수정

### 현재 커밋 수정
git commit --amend 
: 커밋메시지 변경가능

빼먹은 커밋 추가도 가능
(add -> amend)
amend 뒤에 메시지 추가할수도있음

아예 한줄로하려면
git commit --amend -m 'Add members to Panthers and Pumas'

### 과거 커밋 수정

git rebase -i (대상 바로 이전 커밋)


명령어	설명
p, pick	커밋 그대로 두기
r, reword	커밋 메시지 변경
e, edit	수정을 위해 정지
d, drop	커밋 삭제
s, squash	이전 커밋에 합치기

edit 이후에 rebase --continue함

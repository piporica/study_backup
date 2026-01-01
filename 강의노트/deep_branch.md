# branch

fast foward vs 3way merge

fast-foward
브랜치 남기려면 --no-ff 해서 머지커밋 만들 것


## cherry pick
다른 브랜치에서 원하는 커밋만 가져오기

git cherry-pick (커밋)
-> merge나 rebase와 달리 '특정 커밋만' '복제' 임

## 잔가지만 떼오기
보조 기능만 떼와야 할 때...

rebase --onto (도착브랜치) (출발브랜치) (이동브랙치)

## 다른 커밋들을 하나로 묶어서 가져오기 

git merge --squash (커밋)
-> 한번에 모아서 스테이징해줌
이것도 '복사'임


## 협업을 위한 브랜치 사용법
Gitflow
-> 협업을 위한 브랜칭 전략

브랜치	용도
main	제품 출시/배포
develop	다음 출시/배포를 위한 개발 진행
release	출시/배포 전 테스트 진행(QA)
feature	기능 개발
hotfix	긴급한 버그 수정


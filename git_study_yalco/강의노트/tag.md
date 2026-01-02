# 태그
 특정 시점을 키워드로 저장하거나
 버전 정보를 붙이고자 할 때

 버전정보 붙이기: semantic versioning
 major - minor - patch
 호환 - 기능 - 버그수정 

 태그 종류	설명
lightweight	특정 커밋을 가리키는 용도
annotated	작성자 정보와 날짜, 메시지, GPG 서명 포함 가능

기왕 달 거면 annotated로 다세용..

---

git tag (태그)
git show (태그) -> 해당 커밋의 정보 보임
git tag -d (태그) : 삭제 


git tag -a (태그) : annotated 
git tag (태그) -m (메시지)

원하는 커밋에 추가
git tag (태그명) (커밋 해시) -m (메시지)

like 검색두 됨 -l 

checkout 으로 버전의 커밋으로 갈 수 있음

## 원격의 태그 관리

git push 원격명 태그명

태그 원격에서 지우기 push --delete 원격 태그

전체올리기 git push --tags


## 배포
태그가 있는 버전들을 깃헙에서 배포판으로 만들 수 있음

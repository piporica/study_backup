# 취소와 되돌리기

## 관리되지 않는 파일들 삭제하기
git clean
-> 깃에서 추적하지 않는 파일들 삭제

옵션	설명
-n	삭제될 파일들 보여주기
-i	인터렉티브 모드 시작
-d	폴더 포함
-f	강제로 바로 지워버리기
-x	⚠️ .gitignore에 등록된 파일들도 삭제

(이어붙여서 사용가능)

보통 -> git clean df 


## 커밋하지 않은 변경사항 되돌리기 

git restore
-> 특정 파일을 지정된 상태로 복구

이전에 checkout -> switch / restore로 분리됨

reset은 stage 안에 있는 것까지 돌려버림

만약 이미 staging된 걸 다시 내리고 싶으면
git restore --staged (파일명)

---

특정 커밋의 상태로 되돌리기
-> restore --source=(커밋명) (파일명)


## reset했어도 희망이 있을까...

reflog
프로젝트 전체 상태를 되돌릴 수 있음



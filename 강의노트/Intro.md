## 01. Intro / git 시작하기
- https://www.yalco.kr/@git-github/0-1/

- sourceTree: git GUI

- 깃에 저장하지 않을 것
- 필요없는것 : 빌드 결과물 / 라이브러리
- 보안
: .gitignore

## gitignore 형식
- https://git-scm.com/docs/gitignore 참조

* 주석은 #으로 
*  모든 file.c
file.c

*  최상위 폴더의 file.c
/file.c

*  모든 .c 확장자 파일
*.c

*  .c 확장자지만 무시하지 않을 파일
!not_ignore_this.c

* logs란 이름의 파일 또는 폴더와 그 내용들
logs

* logs란 이름의 폴더와 그 내용들
logs/

* logs 폴더 바로 안의 debug.log와 .c 파일들
logs/debug.log
logs/*.c

* logs 폴더 바로 안, 또는 그 안의 다른 폴더(들) 안의 debug.log
log/**/debug.log
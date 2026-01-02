# 깃 보다 잘 활용하기
## help와 문서
help치면 명령어나옴 -a 치면 전부나옴
명령어치고 -h치면 설명나옴..
help치고 명령어 (-w) 치면 웹나옴

문서를 잘 보면 좋아용

pro-git이라는 책이 다국어로 올라와있어요


## 각종 설정 - git config
--global / --local 설정가능
(local이 기본)

git config --list 로 전체확인가능
--global --list로 글로벌 확인가능

빔 에디터에서 열거면 그냥 -e
기본 에디터 vscode로 수정
git config --global core.editor "code --wait"

##팁

줄바꿈 호환
git config --global core.autocrlf (윈도우: true / 맥: input)

pull 기본 전략 변경 -> merge or rebase
git config pull.rebase false
git config pull.rebase true

git config --global init.defaultBranch main

-u나 -setupstream 안하기
git config --global push.default current


단축키
git config --global alias.(단축키) "명령어"
ex) git config --global alias.cam "commit -am"

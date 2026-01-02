# 깃 추가기능

## Hooks
.git -> hooks 폴더에서 샘플을 확인할 수 있음
.sample을 빼면 바로사용가능~
깃모지 쓰고싶은데 ssl때문에 안되는듯...


## submodules
깃으로 각각 관리되는 서브모듈이 있을 때
-> 공통모듈이라던가...

git submodule add (submodule의 GitHub 레포지토리 주소) (하위폴더명, 없을 시 생략)

메인 -> 서브 
수정사항에는 직접적으로 관여하지 않으나 (add 등)
무슨 커밋 상태인지는 저장되어있음

깃헙에서 확인하면 약간 링크? 처럼 보임

git clone으로 플젝 받아오ㅕㅁㄴ 메인만 받아짐
서브모듈 받아오려면 -> git submodule init (모듛명) -> update 

원격의 변화를 끌어오기(pull)
git submodule update --remote

서브모듈 안에 또 서브모듈이 있을 시: --recursive 추가
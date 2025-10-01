한국어 자동 크롤링 LangChain
- 이 프로그램은 코딩을 모르는 사용자도 






GIT COMMIT RULE

GIT Branch 만들기
- git branch (이름) <- (이름) 브랜치 생성
- git checkout (이름) <- (이름) 브랜치로 이동
- git commit -m (커밋내용) <- (커밋내용) 로컬에 저장
- git push origin [branch이름] <- branch이름으로 업로드
- git pull origin main <- merge후 파일 받아오기

TYPE
커밋은 제목,본문,꼬리말로 구성
- Subject(제목)
- Body(본문)
- Footer(꼬리말)

커밋 종류
- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 코드 formatting, 세미콜론(;) 누락, 코드 변경이 없는 경우
- refactor : 코드 리팩토링
- test : 테스트 코드, 리팩토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정

제목 작성법
- 제목은 50자를 넘기지 않고, 마침표를 붙이지 않는다.
- 제목에는 위 커밋 종류를 함께 쓴다.
- 과거시제를 사용하지 않고 명령조로 작성한다.
- 제목과 본문은 한 줄 띄워 분리한다.
- 제목의 첫 글자는 반드시 대문자로 쓴다.
 -제목이나 본문에 이슈 번호(가 있다면) 붙여야 한다.


본문 작성법
- 선택사항이기에 모든 커밋에 본문 내용을 작성할 필요는 없다.
- 한 줄에 72자를 넘기면 안된다.
- 어떻게(How)보다 무엇을, 왜(What, Why)에 맞춰 작성한다.
- 설명뿐만 아니라, 커밋의 이유를 작성할 때에도 쓴다.

Footer 작성법
- 선택사항이기에 모든 커밋에 꼬릿말을 작성할 필요는 없다.
- Issue Tracker ID를 작성할 때 사용한다.

Git commit example:
feat : First push

이 프로젝트는 사용자가 한글로 크롤링을 진행할 수 있도록 도움을 주는 LangChain기반 프로그램이다.
LLM모델과 requests,selenium을 활용해 크롤링을 진행한다.

깃 브랜치 사용법
- Origin(master)
- 각 사용자 개인 branch
- feature branches
- develop branch
- release branches
- hotfixes

각 브랜치 역할
- Origin(master) : 최종 배포할 서비스 내용의 브랜치, 태그로 버전을 표시
- develop : 주요 개발 브랜치, 이 브랜치를 기준으로 각자 작업한 기능을 Merge
- feature : 기능 개발 브랜치, 기능 개발이 완료되면 develop 브랜치에 Merge
- release : 최종 배포 master 브랜치 전 QA(품질검사)를 하기위한 브랜치
- hotfix : master 브랜치로 배포 후에 버그가 생겼을 때 긴급 수정하는 브랜치
- 개인 branch : 개인이 개발하는 branch


명령어(dev)
Docker 실행 명령어
- docker-compose up <- Docker 실행 명령어
- docker-compose down <- Docker 중지 명령어
!! ctrl + c로 종료수 docker-compose down 실행~

- docker-compose up --build <- Docker 이미지 재생성(컨테이너 재생성) 다시 묶기 명령어
-> 언제사용? Docker파일 수정, 새로운 라이브러리(패키지) 사용시 리빌드 실행
-> 단순한 코드 파일 변경시에는 'docker-compose up'으로 최신화 가능!


-- 트러블 슈팅
- LLM응답 생성이 되지 않음!
-> LangChain에서 생성되는 응답이 비동기 방식이 아니라 동기방식이여서 LLM응답을 받기전에 db에 저장해서 오류 출력
-> LLM모델을 비동기 방식으로 변경!

- system프롬프트를 LLM모델에게 넘겨주지 않는 구문 오류 발생!
-> LangChain은 프롬프트 + 사용자 입력을 매번 넘기기 어려우니까 기본 틀로 "프롬프트 +"를 만들어주는 역할!
-> 따라서 사용자 입력값을 전달하면 자동으로 사용자 입력값 앞에 미리 설정해놓은 "프롬프트 +"가 붙어 LLM 모델에게는 "프롬프트 + 사용자 입력값"으로 넘어가게 되는 것!

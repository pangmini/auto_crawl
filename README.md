GIT COMMIT RULE

GIT Branch 만들기
- git branch (이름) <- (이름) 브랜치 생성
- git checkout (이름) <- (이름) 브랜치로 이동
- git commit -m (커밋내용) <- (커밋내용) 로컬에 저장
- git push origin [branch이름] <- branch이름으로 업로드


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

- docker-compose up --build <- Docker 패키지 다시 묶기 명령어

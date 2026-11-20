# campus-chatbot (학사 길잡이)

학사 공지, 학칙, 장학 안내, 졸업 요건 문서를 바탕으로 학생 질문에 답하고 출처를 보여 주는 RAG 챗봇입니다.
클라우드아키텍처 수업 과제로 만들고 있습니다.

## 폴더 구조

```
frontend/         채팅 화면 (S3 + CloudFront로 배포)
lambda/chat/      질문 처리 Lambda (2주차: 연결 확인용 /hello API)
lambda/collect/   문서 수집 Lambda (뼈대만 있음)
```

## 진행 상황

- [x] 1주차: 서비스 기획 및 AWS 아키텍처 설계
- [x] 2주차: AWS 환경 및 개발 환경 구성, 테스트 API 배포
- [ ] 이후: 문서 수집, Knowledge Bases 연결, 답변 생성

## 2주차 AWS 구성 (서울 리전 ap-northeast-2)

| 구분 | 리소스 | 설명 |
|---|---|---|
| 웹 화면 | S3 `campus-chatbot-web-…` + CloudFront | 퍼블릭 액세스 차단, OAC로 CloudFront만 읽기 허용 |
| 문서 저장소 | S3 `campus-chatbot-docs-…` | 분야별 폴더(haksa, scholarship, graduation, calendar), 버전 관리 켬 |
| 대화 기록 | DynamoDB `campus-chatbot-chat-history` | 온디맨드, 키: sessionId + createdAt |
| API | API Gateway(HTTP API) `GET /hello` → Lambda `campus-chatbot-chat` | 연결 확인용 테스트 API |
| 권한 | IAM 역할 `campus-chatbot-chat-lambda-role` | 로그 기록 + DynamoDB 저장만 |
| 권한 | IAM 역할 `campus-chatbot-collect-lambda-role` | 로그 기록 + 문서 버킷 저장만 |
| 권한 | IAM 정책 `campus-chatbot-ta-upload-policy` | 조교용: 문서 버킷 목록 보기·업로드만 |

OpenSearch Serverless와 Knowledge Bases는 만들기만 해도 요금이 나가서, 실제로 연결하는 주차에 만든다.

## 테스트 주소

- 웹 화면: https://d92b9cbsfkgb2.cloudfront.net
- API: https://xhi2frncaj.execute-api.ap-northeast-2.amazonaws.com/hello

## 개발 환경

- Claude Code (코드 작성 보조)
- Git + GitHub, GitHub CLI
- AWS CLI v2 (서울 리전 기본 설정)
- Python 3.13 (Lambda 런타임)

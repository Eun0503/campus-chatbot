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
- [ ] 2주차: AWS 환경 및 개발 환경 구성, 테스트 API 배포
- [ ] 이후: 문서 수집, Knowledge Bases 연결, 답변 생성

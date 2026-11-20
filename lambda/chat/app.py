import json
import os
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))


def handler(event, context):
    """2주차 테스트용 API. 배포가 잘 됐는지 확인하는 용도로 간단한 응답만 돌려준다.
    이후 주차에서 Knowledge Bases 검색과 Bedrock 답변 생성을 여기에 붙인다."""
    body = {
        "service": "학사 길잡이",
        "message": "API Gateway + Lambda 연결 확인",
        "stage": os.environ.get("STAGE", "dev"),
        "time": datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S"),
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps(body, ensure_ascii=False),
    }

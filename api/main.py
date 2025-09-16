# api/main.py

from coding_expert_agent.main import handler  # 방금 추가한 handler 함수

def main(req, res):
    """
    Vercel 서버리스 엔트리 포인트
    req: 요청 객체
    res: 응답 객체
    """
    try:
        data = req.get_json()  # {"messages": [{"role": "user", "content": "..."}]}
        if not data or "messages" not in data:
            res.status_code = 400
            return {"error": "messages key missing"}

        result = handler(data)  # coding_expert_agent/main.py의 handler 호출
        res.status_code = 200
        return result

    except Exception as e:
        res.status_code = 500
        return {"error": str(e)}
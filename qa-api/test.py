import requests
import sys

BASE_URL = "http://localhost:5000"


def test_health():
    """测试健康检查接口"""
    resp = requests.get(f"{BASE_URL}/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
    print("✓ health check passed")


def test_qa_success():
    """测试问答成功"""
    resp = requests.post(
        f"{BASE_URL}/api/qa",
        json={"question": "你好，请介绍一下你自己"}
    )
    assert resp.status_code == 200
    assert "answer" in resp.json()
    print("✓ qa success passed")
    print(f"  Answer: {resp.json()['answer'][:50]}...")


def test_qa_empty_question():
    """测试空问题"""
    resp = requests.post(f"{BASE_URL}/api/qa", json={})
    assert resp.status_code == 400
    print("✓ qa empty question passed")


if __name__ == "__main__":
    print("Running tests...")
    try:
        test_health()
        test_qa_success()
        test_qa_empty_question()
        print("\n✅ All tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
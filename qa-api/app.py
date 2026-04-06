from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 默认使用 OpenAI 兼容接口，可配置
LLM_API_URL = os.environ.get("LLM_API_URL", "https://api.openai.com/v1/chat/completions")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-3.5-turbo")


@app.route("/api/qa", methods=["POST"])
def qa():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "question is required"}), 400

    try:
        answer = call_llm(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def call_llm(prompt: str) -> str:
    """调用 LLM 接口"""
    import requests

    headers = {
        "Content-Type": "application/json",
    }
    if LLM_API_KEY:
        headers["Authorization"] = f"Bearer {LLM_API_KEY}"

    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    response = requests.post(LLM_API_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()

    result = response.json()
    return result["choices"][0]["message"]["content"]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
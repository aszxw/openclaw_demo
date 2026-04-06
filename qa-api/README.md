# LLM QA 问答后端

基于 Flask 的简单 LLM 问答 API 服务。

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
```

## API 接口

### 问答接口

**POST** `/api/qa`

请求体：
```json
{
  "question": "你的问题"
}
```

响应：
```json
{
  "answer": "答案"
}
```

## 测试

```bash
python test.py
```
from flask import Flask, request, jsonify
from chatgpt import ChatGPT

app = Flask(__name__)

# 创建 ChatGPT 对象
chatbot = ChatGPT(api_key='your_api_key', api_secret='your_api_secret')

# 定义 API 路由和控制器
@app.route('/api/v1/live_chat', methods=['POST'])
def live_chat():
    # 获取 POST 请求参数
    user_id = request.form.get('user_id')
    message = request.form.get('message')

    # 调用 ChatGPT 聊天机器人生成回复消息
    reply = chatbot.generate_reply(message)

    # 返回 API 响应
    return jsonify({
        'user_id': user_id,
        'message': message,
        'reply': reply,
    })

# 启动应用程序
if __name__ == '__main__':
    app.run()

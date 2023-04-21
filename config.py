import requests
import json
from config import API_KEY, ACCESS_TOKEN, ROBOT_ID, BASE_URL, DATABASE

# 连接数据库
db_config = DATABASE
db = pymysql.connect(host=db_config['host'], port=db_config['port'], user=db_config['user'], password=db_config['password'], db=db_config['db'])
cursor = db.cursor()

# 定义 ChatGPT 接口 URL
chatgpt_url = BASE_URL + '/chat'

# 定义抖音直播聊天室 URL
livechat_url = BASE_URL + '/livechat'

# 发送消息到 ChatGPT 接口
def send_message_to_chatgpt(message):
    data = {
        'api_key': API_KEY,
        'access_token': ACCESS_TOKEN,
        'robot_id': ROBOT_ID,
        'message': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(chatgpt_url, data=json.dumps(data), headers=headers)
    return response.json()['response']

# 接收抖音直播聊天室消息
def receive_message_from_livechat():
    response = requests.get(livechat_url)
    messages = response.json()['messages']
    return messages

# 发送消息到抖音直播聊天室
def send_message_to_livechat(message):
    data = {
        'message': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(livechat_url, data=json.dumps(data), headers=headers)
    return response.json()

# 循环接收抖音直播聊天室消息，并发送回复消息
while True:
    messages = receive_message_from_livechat()
    for message in messages:
        # 判断消息类型是否为文本消息
        if message['message_type'] == 'text':
            # 获取消息内容
            content = message['content']
            # 调用 ChatGPT 接口获取回复消息
            reply = send_message_to_chatgpt(content)
            # 发送回复消息到抖音直播聊天室
            send_message_to_livechat(reply)
            # 将聊天记录保存到数据库中
            sql = "INSERT INTO chat_history (user_id, robot_id, message, reply) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (message['user_id'], ROBOT_ID, content, reply))
            db.commit()

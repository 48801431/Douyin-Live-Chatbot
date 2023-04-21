import requests

class ChatGPTClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    def generate_reply(self, prompt):
        headers = {'Authorization': f'Bearer {self.api_secret}'}
        data = {
            'prompt': prompt,
            'max_tokens': 50,
            'temperature': 0.7,
            'stop': ['\n']
        }
        response = requests.post(self.endpoint, headers=headers, json=data)
        if response.status_code == 200:
            reply = response.json()['choices'][0]['text'].strip()
            return reply
        else:
            return None

import unittest
from unittest.mock import MagicMock
from app import ChatGPTClient

class TestChatGPTClient(unittest.TestCase):
    def setUp(self):
        self.client = ChatGPTClient('api_key', 'api_secret')
        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {
            'choices': [{'text': 'Hello, how can I help you?'}]
        }

    def test_generate_reply_success(self):
        with unittest.mock.patch('requests.post', return_value=self.mock_response):
            reply = self.client.generate_reply('Hi')
            self.assertEqual(reply, 'Hello, how can I help you?')

    def test_generate_reply_error(self):
        with unittest.mock.patch('requests.post', return_value=self.mock_response):
            reply = self.client.generate_reply('')
            self.assertIsNone(reply)

if __name__ == '__main__':
    unittest.main()

import requests

api_endpoint = 'http://localhost:11434/api/chat'

data = {
    'model': 'llama2',
    'stream': False,
    'messages': [
        {'role': 'system', 'content': 'You only speak in uppercase.'},
        {'role': 'user', 'content': 'Hello!'}
    ]
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print('Response:', response_data['message'])
else:
    print('Error:', response.status_code, response.text)
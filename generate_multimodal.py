import requests
import base64

#load image
with open('sample_image.jpg', 'rb') as image_file:

    # Read contents of the image file (binary)
    image_data = image_file.read()

    # Turn into Base64
    base64_image_date = base64.b64encode(image_data)

    # Encode to UTF-8
    base64_image_string = base64_image_date.decode('utf-8')

api_endpoint = 'http://localhost:11434/api/generate'

data = {
    'model': 'llava',
    'stream': False,
    'prompt': 'Describe the image provided',
    'images': [base64_image_string],
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print('Response:', response_data['response'])
else:
    print('Error:', response.status_code, response.text)
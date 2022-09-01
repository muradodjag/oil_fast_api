import requests
import json

multipart_form_data = {
    'file': ('2.jpg', open('1.jpg', 'rb')),
}

response = requests.post('http://127.0.0.1:8000/upload', files=multipart_form_data)

print(json.loads(response.content))
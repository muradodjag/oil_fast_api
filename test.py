import requests
import json

multipart_form_data = {
    'file': ('3.jpg', open('test.jpg', 'rb')),
}
headers = {
    'access_token' : '524c2a8d1805dba6707039618707780b'
}
response = requests.post('http://127.0.0.1:8000/api/v1/upload', files=multipart_form_data, headers=headers)

print(response.status_code,json.loads(response.content))
import requests

r = requests.post('http://127.0.0.1:8000/', data={'selom':'hello'})
print(r.text)
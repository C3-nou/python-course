# 07 - Requests

import urllib.request
import json

api_url = "https://jsonplaceholder.typicode.com/posts/"

try:
    response = urllib.request.urlopen(api_url)
    data = response.read()
    data_json = json.loads(data.decode("utf-8"))
    print(data_json)
    response.close()
except urllib.error.URLError as error:
    print(f"Ocurrió un error al realizar la solicitud: {error.reason}")


print("--------------------------------")

# implementacion con requests

import requests

response = requests.get(api_url)
data = response.json()
print(data[0])
print("---"*10)

# POST

body = {
    "userId": 1,
    "title": "Mi primer post",
    "body": "Este es mi primer post"
}

response = requests.post(api_url, json=body)
print(response.status_code)
print("---"*10)

# PUT

body = {
    "userId": 1,
    "title": "Mi primer post",
    "body": "Este es mi primer post",
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=body)
print(response.status_code)
print("---"*10)

# DELETE

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print("---"*10)

# API de Open AI

# ejemplo json.dumps

import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(json.dumps(data, indent=4))

print("---"*10)

# ejemplo json.loads

data = '{"name": "John", "age": 30, "city": "New York"}'

print(json.loads(data))

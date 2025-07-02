#Example API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title ': 'foo',
    'body': 'bar',
    'userId': 1
}
# Sending a POST request
import requests
response = requests.post(url, json=data)
# Checking the response
print(f"Status Code: {response.status_code}")
print('response.json():', response.json())
# The response should contain the data you sent, along with an ID assigned by the server.


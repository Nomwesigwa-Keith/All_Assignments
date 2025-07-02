#basic GET request using requests library
import requests

response = requests.get('https://api.github.com')

print(f"Status Code: {response.status_code}")
print('response.json():', response.json())
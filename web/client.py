import requests

url = "http://localhost:5000/get_anime"

result = requests.get(url)   

print(result.json())
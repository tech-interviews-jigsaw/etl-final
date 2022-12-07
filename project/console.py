import requests
response = requests.get("https://itunes.apple.com/lookup?id=909253")
results = response.json()

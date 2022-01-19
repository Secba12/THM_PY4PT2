import requests

url = 'https://assets.tryhackme.com/img/THMlogo.png'
request = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(request.content)
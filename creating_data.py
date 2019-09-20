import requests

r = requests.get('https://en.wikipedia.org/wiki/Australia')

print(r.text)
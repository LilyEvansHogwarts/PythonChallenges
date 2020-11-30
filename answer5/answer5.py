import requests

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
# num = "12345"
num = "8022"

while True:
    url = URL.format(num)
    text = requests.get(url).text
    print(text)
    num = text.split(' ')[-1]

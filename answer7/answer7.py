num = "90052"

while True:
    with open('./channel/'+num+'.txt') as f:
        ll = f.read()
        print(ll)
        num = ll.split(' ')[-1]
        if num[-1] < '0' or num[-1] > '9':
            break

import zipfile

archive = zipfile.ZipFile('channel.zip', 'r')
content = archive.open('90052.txt', 'r').read()
content = content.decode("utf-8")

num = '90052'
while True:
    print(archive.getinfo(num+'.txt').comment.decode("utf-8"), end='')
    content = archive.open(num+'.txt', 'r').read()
    content = content.decode("utf-8")
    num = content.split(' ')[-1]
    if num[-1] < '0' or num[-1] > '9':
        break


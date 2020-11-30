with open('test3.txt') as f:
    ll = f.read().split('\n')

out = ""
for l in ll:
    for i in l:
        if i >= 'a' and i <= 'z':
            out += i
print(out)

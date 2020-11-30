import pickle
with open('banner.p', 'rb') as f:
    data = pickle.load(f)

start_string = ""
for l in data:
    for i in l:
        start_string += i[0]*i[1]
    start_string += '\n'

print(start_string)

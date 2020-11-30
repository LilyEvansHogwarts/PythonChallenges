def lowercase(s):
    return s >= 'a' and s <= 'z'

def uppercase(s):
    return s >= 'A' and s <= 'Z'

with open('test4.txt') as f:
    ll = f.read().split('\n')
    ll = ll[:-1]

import numpy as np
N = len(ll)
M = len(ll[0])
num = 0
matrix = np.zeros((N, M))
count_left = np.zeros((N, M))
count_right = np.zeros((N, M))
count = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        matrix[i][j] += uppercase(ll[i][j])

count[:, 3:-3] = matrix[:, :-6] + matrix[:, 1:-5] + matrix[:, 2:-4] + matrix[:, 4:-2] + matrix[:, 5:-1] + matrix[:, 6:]
count[:, 4:-3][matrix[:, :-7] == 1] = 0
count[:, 3:-4][matrix[:, 7:] == 1] = 0
count[matrix == 1] = 0
out = ""
for i in range(N):
    for j in range(M):
        if count[i,j] == 6:
            out += ll[i][j]
print(out)

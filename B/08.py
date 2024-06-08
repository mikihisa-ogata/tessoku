n = int(input())
x = [None] * n
y = [None] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

q = int(input())
a = [None] * q
b = [None] * q
c = [None] * q
d = [None] * q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

z = [[0] * 10 for i in range(10)]

for i in range(n):
    z[x[i]][y[i]] += 1

import pprint

# pprint.pprint(z)

for i in range(10):
    for j in range(1, 10):
        z[i][j] += z[i][j - 1]

# pprint.pprint(z)

for i in range(1, 10):
    for j in range(10):
        z[i][j] += z[i - 1][j]

# pprint.pprint(z)

for i in range(q):
    print(z[c[i]][d[i]] + z[a[i] - 1][b[i] - 1] - z[a[i] - 1][d[i]] - z[c[i]][b[i] - 1])

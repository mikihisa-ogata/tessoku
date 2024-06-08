n = int(input())
a = list(map(int, input().split()))
q = int(input())
l = [None] * q
r = [None] * q

for i in range(q):
    l[i], r[i] = map(int, input().split())

# print(l, r)

s = [None] * (n + 1)
s[0] = 0
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

# print(s)

for i in range(q):
    if (r[i] - l[i] + 1) / 2 == s[r[i]] - s[l[i] - 1]:
        print("draw")
    elif (r[i] - l[i] + 1) / 2 < s[r[i]] - s[l[i] - 1]:
        print("win")
    else:
        print("lose")

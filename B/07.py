t = int(input())
n = int(input())
l = [None] * n
r = [None] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())

tmp = [0] * (t + 1)
for i in range(n):
    tmp[l[i]] += 1
    tmp[r[i]] -= 1
# print(tmp)

ans = [None] * (t + 1)
ans[0] = tmp[0]

for i in range(1, t + 1):
    ans[i] = ans[i - 1] + tmp[i]

for a in ans:
    print(a)
# print(ans)

# なぜか答えが合わない

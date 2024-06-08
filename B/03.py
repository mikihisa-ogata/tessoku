from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
ans = False

b = list(combinations(a, 3))

# print(b)


for x in b:
    # print(sum(x))
    if sum(x) == 1000:
        ans = True

if ans:
    print("Yes")
else:
    print("No")

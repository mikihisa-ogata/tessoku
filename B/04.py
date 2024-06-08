n = input()

# s = '12345678'
# 分割 => 数字のリスト
a = [int(c) for c in n]
# print(a)

ans = 0
for i in range(len(a)):
    ans += 2**i * a[-1 * (i + 1)]

print(ans)

import itertools

l = [1, 2, 3, 4, 5, 6]

print(l)

print(list(itertools.accumulate(l)))
# [1, 3, 6, 10, 15, 21]

print(list(itertools.accumulate(l, initial=0)))
# [0, 1, 3, 6, 10, 15, 21]

print(list(itertools.accumulate(l, initial=100)))
# [100, 101, 103, 106, 110, 115, 121]

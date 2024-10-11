a = list(map(int, input().split()))
max = 0
res = 0
for i in a:
    count = a.count(i)
    if count > max:
        max = count
        res = i
print(res)
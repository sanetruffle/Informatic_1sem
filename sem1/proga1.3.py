import math
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
res = math.prod(a)
print(res**(1/len(a)))
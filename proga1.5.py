n = int(input())
b = int(input())
c = int(input())
n = int(str(n), b)
res = ''
while n > 0:
    res = str(n % c) + res
    n //= c
print(res)
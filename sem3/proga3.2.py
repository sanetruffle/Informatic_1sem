def pf(n):
    f = []
    d = 2
    while n > 1:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    return f

n = int(input())
print(pf(n))
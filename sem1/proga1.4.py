f= open ("input.txt", 'r')
lines = f.readlines()
a = list(map(int, lines[0].split()))
op = lines[1]
if op == "+":
    res = sum(a)
elif op == "-":
    res = a[0]
    for i in a[1:]:
        res -= i 
else:
    res = 1
    for i in a:
        res *= i
f.close()
f = open ("output.txt", "w")
f.write(str(res))
f.close()
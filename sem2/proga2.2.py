a = input().split()
b = int(a[0]) 
s = a[1]       
length = len(s)
group_size = length // b
res = ""
for i in range(b):
    group = s[i * group_size:(i + 1) * group_size]
    res += group[::-1]
print(res)
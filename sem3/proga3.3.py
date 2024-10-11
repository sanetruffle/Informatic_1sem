def e(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = e(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

def main():
    a, b = map(int, input().split())
    d, x, y = e(a, b)
    print(f"{x} {y} {d}")

main()
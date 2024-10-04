def draw_triangle(size, symbol):
    for i in range(1, size+1):
        print(symbol * i)

size = int(input("Введите размер: "))
symb = input("Введите символ: ")
draw_triangle(size, symb)

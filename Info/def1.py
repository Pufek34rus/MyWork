print("~~~~~~~Часть 1~~~~~~~")
# Запись значения в переменную при вводе
x = int(input("введите число 1:"))
Y = int(input("введите число 2:"))

# Создание функции с значениями a и b.
def sum(a, b):
    # Операции которые выполняет функция
    return a + b
# вызов функции с присвоением значений от x и Y на место a и b
print(sum(x, Y))

print("~~~~~~~Часть 2~~~~~~~")
x = int(input("Введите число:"))


def f(a):
    return 2*a - 2


print(f(x))
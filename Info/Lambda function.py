# Лямбда функции те-же def функции но они не присваивают имя для фуенкции а работают
# на объект на прямую. Состоят из 1 строки и
# могут присваиватся там где def синтаксически недоступен.
# Например в самой конструкции def
# В общем мини def с определением на месте

print("~~~~~~~Часть 1~~~~~~~")
# Функция Def


def rectangle_area(a, b):
    return a * b


print(rectangle_area(5, 19))

# Функция lambda.
print((lambda a, b: a * b)(5, 19))

print("~~~~~~~Часть 2~~~~~~~")
# Функция Def


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


print(maximum(9, 4))

# Функция lambda.
print((lambda a, b: a if a > b else b)(23, 30))

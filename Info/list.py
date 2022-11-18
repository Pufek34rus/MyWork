
print("~~~~~~~Часть 1~~~~~~~")
# Создание списка. Необходимо исользовать квадратные скобки
spisok = [3, 4, 5, 9, 10, "гывы"]
print(spisok)

print("~~~~~~~Часть 2~~~~~~~")
# Список в списке
spisok = [3, 5, 34, 1, [2, 4, 6]]
print(spisok)

print("~~~~~~~Часть 3~~~~~~~")
# Вывод значения в списке по порядковому номеру. Счет от 0
Names = ["Кеша", "Толик", "Попугай"]
print(Names[2])
print(Names[-1])

print("~~~~~~~Часть 4~~~~~~~")
# Перебор списка по циклу for
for k in Names:
    print(k)

print("~~~~~~~Часть 5~~~~~~~")
# Добавление элемента в список
Names.append("Аляска")
print(Names)

print("~~~~~~~Часть 6~~~~~~~")
# Удаление элемента в списке
print(Names)
Names.pop(1)
print(Names)

print("~~~~~~~Часть 7~~~~~~~")
# Возврат индекса
n = Names.index("Кеша")
print(n)

print("~~~~~~~Часть 8~~~~~~~")
# Количество элементов в списке
print(len(Names))

print("~~~~~~~Часть 9~~~~~~~")
# сортировка списка по порядку
number = [1, 3, 5, 2, 87, 12]
number.sort()
print(number)

print("~~~~~~~Часть 10~~~~~~~")
# Сортировка списка в обратном порядке
number.sort(reverse=True)
print(number)

print("~~~~~~~Часть 11~~~~~~~")
# Замена элемента в списке на новый
number[4] = "челен"
print(number)

print("~~~~~~~Часть 12~~~~~~~")
# Поиск по списку. arrey_search(массиф, диапазон, значение(все можно с типом)).
# Возвращает первый найденный индекс. Или -1 если его нет.


def array_search(A, N, x:int):
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1, 2, 3, 123]
    m = array_search(A1, 3, 2)
    if m == -1:
        print("Значение отсутствует")
    else:
        print("Значение найдено")

test_array_search()

print("~~~~~~~Часть 13~~~~~~~")
# инверсия списка


def loh(a:list, n:int):
    for k in range(n//2):
        a[k], a[n-1-k] = a[n-1-k], a[k]

def test_loh():
    a1 = [1, 2, 3, 4, 5]
    print(a1)
    loh(a1, 5)
    print(a1)
    if a1 == [5, 4, 3, 2, 1]:
        print("збс")
    else:
        print("Дичь")
test_loh()

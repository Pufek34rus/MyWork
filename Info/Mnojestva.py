# Множество это список в котором данные не упорядочны, не признают дубликаты,
# и не поддерживают срезы и индексацию как в списке или кортеже.
print("~~~~~~~Часть 1~~~~~~~")
numbers = {1, 2, 4, 63, 12, 4, 63}
print(numbers)
print("~~~~~~~Часть 2~~~~~~~")
# Пустыми скобками создаётся словарь а не множество
numbers2 = {}
print(type(numbers2))
print("~~~~~~~Часть 3~~~~~~~")
# Функция set() дает пустым скобкам тип множества.
numbers3 = set()
print(type(numbers3))
print("~~~~~~~Часть 4~~~~~~~")
# Конвертируем списки в множества
numbers4 = set([1, 1, 4, 5, 2, 3, 4, 4])
print(type(numbers4))
print("~~~~~~~Часть 5~~~~~~~")
# Вывод по элементам
numbers5 = {1, 2, 3, 4, 5, 6, 7}
for i in numbers5:
    print(i)
print("~~~~~~~Часть 6~~~~~~~")
# Поиск совпадения в множестве
print(3 in numbers5)
print("~~~~~~~Часть 7~~~~~~~")
# Добавление элемента в множество
numbers5.add("поляныца")
print(numbers5)
print("поляныца" in numbers5)
print("~~~~~~~Часть 8~~~~~~~")
# Удаление элемента из множество. 4 метода. Если элемента нет в множестве
# remove выведет ошибку, а discard нет. .pop() удалит первый элемент.
# .clear() удалить все элементы
numbers5.discard("vodka")
# Удалить с следующей строки хэштег для теста
# numbers5.remove("vodka")
numbers5.pop()
print(numbers5)
numbers5.clear()
print(numbers5)
print("~~~~~~~Часть 9~~~~~~~")
# Объединение множеств, .union и разделитель, одно и тоже.
numbers6 = numbers.union(numbers4)
print(numbers6)
numbers7 = {"d", "hgf", "sss"}
numbers8 = numbers6 | numbers7
print(numbers8)
print("~~~~~~~Часть 9~~~~~~~")
# Внесение одинаковых значиний 2 множеств в одно.
numbers11 = {1, 1, 2, 3, 5, 8, 13}
numbers12 = {1, 1, 4, 5, 8, 24}
numbers13 = numbers11.intersection(numbers12)
# numbers13 = numbers11 & numbers12 тоже самое
print(numbers13)
print("~~~~~~~Часть 10~~~~~~~")
# Внесение значений из одного множества,
# исключая повторяющиеся значения с другим множеством
numbers14 = numbers11 - numbers12
print(numbers14)
print("~~~~~~~Часть 11~~~~~~~")
# Копирование множества
numbers15 = numbers11.copy()
print(numbers15)
print("~~~~~~~Часть 12~~~~~~~")
# Колличество элементов в множестве
print(len(numbers15))
print("~~~~~~~Часть 13~~~~~~~")
# Создание неизменяемого множества
numbers16 = frozenset({1, 2, 3, 5})
print(numbers16)
# Убрать с следующей строки хэштег для теста
# numbers16.add(23)

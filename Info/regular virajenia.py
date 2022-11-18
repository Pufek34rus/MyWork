# Работа с кодом по шаблону
import re

print("~~~~~~~Часть 1~~~~~~~")
# re.match ищет шаблон именно в начале строки.
# В результате указанно (0,2) т.е. поиск прошёл с 0 и до 2-го символа,
# и со следующего пошло совпадение
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.match("AC", s)
print(result)
# Тут не найдет потому что не в начале
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.match("DC", s)
print(result)

print("~~~~~~~Часть 2~~~~~~~")
# Поиск по всей строке, и возврат диапазона первого совпадения от символа
# после которого идёт совпадение до последнего символа ссовпадения
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.search("DC", s)
print(result)
# Поиск по всей строке но с возвратом не места, а самого совпадения
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.search("DC", s)
print(result[0])

print("~~~~~~~Часть 3~~~~~~~")
# Поиск всех совпадений и вывод списком
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.findall("DC", s)
print(result)

print("~~~~~~~Часть 4~~~~~~~")
# Разбивка строки на части выбирая символ разделитель из строки.
# Выводит списком. Можно добавить аргумент "maxsplit=" с
# указанием кол-ва разбивок
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.split(",", s)
print(result)

print("~~~~~~~Часть 5~~~~~~~")
# Замена элемента строки на новый элемент.
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.sub("A", "P", s)
print(result)

print("~~~~~~~Часть 6~~~~~~~")
# Сравнение всей строки на идентичность с шаблоном
s = "AC/DC,AC/DC,AC/DC,AC/DC,AC/DC,"
result = re.fullmatch("AC/DC,", s)
print(result)

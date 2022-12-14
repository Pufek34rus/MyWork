import re
from unittest import result

print("~~~~~~~Часть 1~~~~~~~")
# Аргумент "r" делает строку "сырой" тоесть указанные в ней символы не будут
# работать как команды, например \t не будет работать как символ табуляции.
# Таким образом родные команды не будут мешать
# работать с регулярными выражениями.
print(r"fdsfs\tdsda")
print("fdsfs\tdsda")

# Точка заменяет собой любой символ при поиске.
s = "44309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"k.k", s)
print(result)


print("~~~~~~~Часть 2~~~~~~~")
# Аргумент "\d" выводит любую первую цифру
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\d", s)
print(result)
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\d\d\d", s)
print(result)

print("~~~~~~~Часть 3~~~~~~~")
# Аргумент "\D" выводит любой первый символ или букву
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\D", s)
print(result)

print("~~~~~~~Часть 4~~~~~~~")
# Аргумент "\s" выводит любой пробельный символ.
# Пробел, табуляция, конец строки.
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\s", s)
print(result)

print("~~~~~~~Часть 5~~~~~~~")
# Аргумент "\S" выводит любой непробельный символ.
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\S", s)
print(result)

print("~~~~~~~Часть 6~~~~~~~")
# Аргумент "\w" выводит любую цифру, букву или нижнее подчеркивание.
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\w", s)
print(result)

print("~~~~~~~Часть 7~~~~~~~")
# Аргумент "\W" выводит любую не цифру, не букву или не нижнее подчеркивание.
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\W", s)
print(result)

print("~~~~~~~Часть 8~~~~~~~")
# Аргумент "\b" находит начало или конец слова по шаблону
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\bDDi", s)
print(result)

print("~~~~~~~Часть 9~~~~~~~")
# Аргумент "\B" не находит границы слова (я хз как это)
s = "ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\BDDi", s)
print(result)

print("~~~~~~~Часть 10~~~~~~~")
# Аргумент "\*" указывает кол-во вхождений
# символов после первой найденной цифры. От нуля и больше вхождений.
# Аргумень "\+" одно или больше вхождений
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\d*", s)
print(result)

print("~~~~~~~Часть 11~~~~~~~")
# Квадратные скобки для указания диапазона поиска. Первую из списка он нашёл "в" её и указал
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"[kxвa]", s)
print(result)
# Поискк цифры в диапазоне от 1 до 6
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"[3-6]", s)
print(result)
# Поиск цифры не входящей в диапазон
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"[^3-6]", s)
print(result)

print("~~~~~~~Часть 12~~~~~~~")
# Поиск одной или дпугой указанной буквы.
# Выведет первую найденную из предложенных.
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"d|v", s)
print(result)

print("~~~~~~~Часть 13~~~~~~~")
# Фигурные скобки это квантификаторы, нужны
# для указания кол-ва повторения шаблона.
# Вместо \d\d\d можно \d{3}
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\d{3}", s)
print(result)
# Квантирование для указания числа вхождений
# для указанного поиска. От 4 символо до 7
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\d{4,7}", s)
print(result)
# Не менее указанного кол-ва вхождений {4,} не менее. {,9} не более
s = "224ввфф+44d309242#$+   --klkdDDidv=a'erkm*&"
result = re.search(r"\d{4,}", s)
print(result)

 ####ПРИМЕР ИСМПОЛЬЗОВАНИЯ####

# Надо вывести все слова начинающтиеся на согл. букву.

s = "-Привет как дела? -Привет, иди на хуй. -А у меня очень хорошо"
result = re.findall(r'\b[бвгджзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ]\w+', s)
print(result)

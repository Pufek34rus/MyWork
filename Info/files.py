# присвоение к переменной файла. w=для перезаписи
# (есои файла нет то он создатся).
# r=для чтение, a=для добавления инфы в файл
print("~~~~~~~Часть 1~~~~~~~")
# Запись
f = open("1.txt", "w")
f.write("Z t,e cj,fr")
f.close()

print("~~~~~~~Часть 2~~~~~~~")
# Чтение
f = open("1.txt", "r")
print(f.read())
f.close()

print("~~~~~~~Часть 3~~~~~~~")
# with позволяет не прописывать закрытие файла.
# Он будет закрыт автоматически при начатии нового блока
with open("1.txt", "a") as f:

    f.write("eq cjcb nthgbkf")


print("~~~~~~~Часть 4~~~~~~~")

f = open("1.txt", "r")
print(f.read())
f.close()

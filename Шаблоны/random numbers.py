import random


str1 = '123456789'

ls = list(str1)

a = 1
while a < 10:
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(6)])

    with open("test.txt", "a") as f:
        f.write(psw + '\n')
    a = a + 1

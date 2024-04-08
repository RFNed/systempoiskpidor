from random import randint, uniform
from time import sleep
from os import system 

print("Хотите ли вы испытать удачу и узнать относитесь ли вы к 'этим'?")
fd = input("Хочу (Да/Нет): ")
if fd == "Да" or fd == "Нет" or fd == "Y" or fd == "N":
    print("Поехали...")
    sleep(1.0)
    system('CLS')
    print("Загрузка", end='')
    for i in range(3):
        hh = uniform(1.0, 3.0)
        print(".", end="")
        sleep(hh)
    sleep(2.0)
    system('CLS')
    pidor = randint(0, 1)
    if pidor == 1:
        print("Ты пидор")
        system('pause')
    else:
        print('Поздравляю ты русский! РОССИЯЯЯ!!!')
        system('PAUSE')

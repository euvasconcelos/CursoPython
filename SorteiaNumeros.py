from time import sleep
from random import randint

sorteados = []
sleep(2)
print('Sorteando . . .')
for i in range (1,7):
    sorteados.append(randint(1,61))
    sorteados.sort()
print(sorteados)
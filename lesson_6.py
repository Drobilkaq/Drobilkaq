# 5
from random import randint

a, b = randint(2, 10), randint(2, 10)
arr = list()

for i in range(a):
    brr = list()
    for j in range(b):
        brr.append(randint(-10, 10))
    arr.append(brr)
print(arr)
summi = {}

for i in arr:
    summi.update({sum(i):i})
    
print(f'макс сумма {max(summi.keys())} у строчки {summi.get(max(summi.keys()))}')
print(f'мин сумма {min(summi.keys())} у строчки {summi.get(min(summi.keys()))}')

# 6
from random import sample, randint

a, b = randint(2, 10), randint(2, 10)
arr = list()

for i in range(b):
    brr = sample(range(-30, 30), a)
    arr.append(brr)
print(arr)

for i in arr:
    if i[i.index(min(i))] % 2 == 0:
        i[i.index(min(i))] = 0
    else:
        i[i.index(min(i))] = 1
print(arr)
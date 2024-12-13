#1
n = int(input('enter number under 100 above 1\n'))
summ = 0
if n<= 100:
    for i in range(n+1):
        summ += n**3
    print(summ)
else:
    print('error')
# 2
for i in range(10):
    st = [i*j for j in range(10)]
    for j in range(len(st)):
        if len(str(st[j])) == 1 and j != 8:
            print(f'{st[j]}  ', end='')
        elif len(str(st[j])) != 1 and j != 8:
            print(f'{st[j]} ', end='')
        else:
            print(f'{st[j]}', end='\n')
# 2*
for i in range(9, 0, -1):
    strochka = [i*j for j in range(10)]
    for j in range(len(strochka)):
        if len(str(strochka[j])) == 1 and j != 8:
             print(f'{strochka[j]}  ', end='')
        elif len(str(strochka[j])) != 1 and j != 8:
             print(f'{strochka[j]} ', end='')
        else:
             print(f'{strochka[j]}', end='\n')
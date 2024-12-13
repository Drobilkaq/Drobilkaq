#1
a, b = map(float, input().split())

if b!=0:
    a, b = map(float, (a, b))
    print(round(a/b,2))
else:
    print('error')

#2

print('enter chek sum')
chsum=int(input())

if chsum>20:
    sksum=chsum-chsum*0.35
    print(round(sksum,2),round(chsum-sksum,2))
else:
    print(chsum)

#3
print('enter num from 1 to 12')

winter=[12,1,2]
spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10,11]
mes=['январь','февраль','март','апрель','июнь','июль','август','сентябрь','октябрь','ноябр','декабрь']

ch= int(input())
if ch in winter:
    print('winter', mes[ch])
if ch in spring:
    print('spring', mes[ch])
if ch in summer:
    print('summer',mes[ch])
if ch in autumn:
    print('autumn',mes[ch])
elif ch>12 or ch<1:
    print('error')
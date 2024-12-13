#1
def read_last(lines, file):
    f = open(file, 'r', encoding='utf-8')
    stroki = f.readlines()
    
    if len(stroki) >= n and n > 0:
        for i in stroki[len(stroki) - lines:]:
            print(i)

n = int(input())
read_last(n, r'C:/Users/article.txt')

#2
import os 

def print_docs(directory):
    use_files = os.walk(directory)
    for i in use_files:
        print(f'в папке {i[0]} \n папки {", ".join([papka for papka in i[1]])} \n файлы {", ".join([file for file in i[2]])} \n')
print_docs('C:/Users/randomik')

#3
def longest_words(file):
    f = open(file, 'r', encoding='utf-8')
    stroki = f.readlines()
    dlini = set()
    
    for i in stroki:
        smotr = i.split()
        dlini.add(max(smotr, key=len))
    if len(dlini) > 0: return max(dlini, key=len)

print(longest_words('C:/Users/article.txt'))

#4
def redactor():
    name = input()
    file = open(f'name.txt', 'w+', encoding='utf-8')
    text = 'пишите содержимое файла'
    print(text)
    
    while text != '':
        text = input()
        file.write(f'{text} \n')
    file.close()
redactor()
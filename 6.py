'''Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.
Виконав студент групи 122-А Андрощук Артем Олександрович
'''
'''
У цій задачі, на мою думку, краще використати ітераційний метод через простоту його написання(всього 1 стрічка) але цей
метод займає досить багато часу, тому для більш швидкого виконання задачі буде краще рекурсивний спосіб
'''

import timeit

print("1 - recursion;\n"
      "2 - iteration.")

flag = int(input("What do you want to use?"))

mysetup = '''import sys'''

if flag == 1:
    mycode = '''
all_digs = "0123456789ABCDEF"
def converter(n):
    n, modulo = n//16, all_digs[n%16]
    if n:
        return converter(n) + modulo
    return modulo

n = int(input("Input your number: "))
print(converter(n))
'''
elif flag == 2:
    mycode = '''
n = int(input("Input your number: "))
print(hex(n))
    '''
print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))

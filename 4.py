'''
Сформувати функцію для введення з клавіатури послідовності чисел і виведення
її на екран у зворотному порядку (завершаючий символ послідовності – крапка)
Виконав студент групи 122-А Андрощук Артем Олександрович
'''

import timeit

print("1 - recursion;\n"
      "2 - iteration.")

flag = int(input("What do you want to use?"))

mysetup = ''''''

if flag == 2:
    mycode = '''
numbers = input("Input numbers in a row with spaces: ")
numbers = numbers.replace('.', "")
array = numbers.split(" ")
print(list(reversed(array)))
'''
elif flag == 1:
    mycode = '''
s_new = []
def reverse(s):
    if len(s)==1:
        s_new.append(s[0])
        return 
    s_new.append(s[-1])
    return reverse(s[0:len(s)-1])

numbers = input("Input numbers in a row: ")
numbers = numbers.replace('.', "")
array = numbers.split(" ")
reverse(array)
print("The answerr is: ", s_new)
'''

print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))

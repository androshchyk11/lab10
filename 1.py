'''Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
Виконав студент групи 122-А Андрощук Артем Олександрович
'''
'''
У цій задачі обидва способи є непоганим рішенням, майже не відрізняються по часу та величина коду майже однакова
'''

import timeit

print(
    "This is a program to search for factorial, you  should use iteration method because it`s much easier in this case,"
    "but you can also use recursion. In tasks like this it doesn`t matter.\n")

print("1 - recursion;\n"
      "2 - iteration.")

flag = int(input("What do you want to use?"))

mysetup = ''''''
if flag == 2:
    mycode = '''
n = int(input("Input n: "))
answer = 1
for i in range(1, n+1):
    answer *= i
print("answer: ", answer)
'''
elif flag == 1:
    mycode = '''
def factorial(n):
    if n==0: 
        return 1
    return factorial(n-1)*n

n = int(input("Input n: "))
print("answer: ",factorial(n))
'''

print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))

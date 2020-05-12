'''Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе).
Виконав студент групи 122-А Андрощук Артем Олександрович
'''

import timeit

print("1 - recursion;\n"
      "2 - iteration.")

flag = int(input("What do you want to use?"))

mysetup = '''
import math
'''

if flag == 2:
    mycode = '''
n = int(input("Input your number: "))
 
if n < 2:
    print("The number shoul be more than 1!")
    quit()
elif n == 2:
    print("This is simple number")
    quit()
 
i = 2 
 
limit = int(math.sqrt(n))
 
while i <= limit:
    if n % i == 0:
        print("False")
        quit() 
    i += 1 
 
print("True")
'''
elif flag == 1:
    mycode = '''
def Isprime(n):
    i = 2
    j = 0
    while(True):
        if(i*i <= n and j != 1):
            if(n % i == 0):
                j=j+1
            i=i+1
        elif(j==1):
            return False
        else:
            return True
n = int(input("Input your number: "))
print(Isprime(n))
'''
print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))

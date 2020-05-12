'''Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Виконав студент групи 122-А Андрощук Артем Олександрович
'''

import timeit

print("1 - recursion;\n"
      "2 - iteration.")

flag = int(input("What do you want to use?"))

mysetup = '''
import numpy as np
import random
'''

if flag == 2:
    mycode = '''
n = int(input("Input your number: "))
array = np.zeros((n,n),dtype=int)
for i in range(n):
    for j in range(n):
        array[i][j] = random.randint(0,100)
print("Your array was filled by random: ")
print(array)

maxNum = array[0][0]
maxIndex = [0,0]
for i in range(n):
    for j in range(n):
        if maxNum < array[i][j]:
            maxNum = array[i][j]
            maxIndex.append(i)
            maxIndex.append(j)
print(maxNum)
print(f"Index of max number: ({maxIndex[-2]}, {maxIndex[-1]})")
'''
elif flag == 1:
    mycode = '''
def maxInd(b, k=None,a=0):
    if k == None : 
        k = b[0][0]
    if len(b) == 0:
        return k
    else:
        if k < b[0][a]:
            k = b[0][a]
        if a == len(b[0])-1:
            b = np.delete(b,0,0)
            a = -1
        return maxInd(b,k,a+1)

n = int(input("Input your number: "))
array = np.zeros((n,n),dtype=int)
for i in range(n):
    for j in range(n):
        array[i][j] = random.randint(0,100)
print("Your array was filled by random: ")
print(array)
print("max element: ",maxInd(array))
'''

print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))

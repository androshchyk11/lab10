'''
Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа
Виконав студент групи 122-А Андрощук Артем Олександрович
'''

import timeit

print("1 - recursion;\n"
      "2 - iteration.")

flag = int(input("What do you want to use?"))

mysetup = ''''''

if flag == 2:
    mycode = '''
n = int(input("Input your number: "))

s = str(n)
while len(s) > 1:
    n = 0;
    for i in s:
        n += int(i)
    s = str(n)
print("answer is: ", s)
'''
elif flag == 1:
    mycode = '''
def root(x):
    if len(str(x))==1:
        return(x)
    else:
        return root(sum([int(i) for i in str(x)]))

n = int(input("Input your number: "))
print("answer is: ", root(n))
'''
print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))

a = int(input('Enter 1-number: '))
x = input("Select the operation type('+,-,*,/'): ")
b = int(input('Enter 2-number: '))

if x == '+':
    print(a+b)
if x == '-':
    print(a-b)
if x == '*':
    print(a*b)
if x == '/' and b == 0:
    print('Numbers cannot be divided by zero')
elif x == '/' and b != 0:
    print(a/b)
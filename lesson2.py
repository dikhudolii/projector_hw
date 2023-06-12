"""
#1
Syntax error:
print error (we need parenthesis to successful running code. Here we have syntax error)

Logic error:
num1=1
num2=2
num3=3
average=(num1+num2+num3)/2
print('Average of num1,num2 and num3:',average)
(we should divide by the total number of values, in our case it is 3)

#2
print(1/0) result:ZeroDivisionError: division by zero
print(0/1) result:0.0

#3
we need comments through our code for its explanation for us and others

#4
variable is a name of a value that is stored in computer's memory
"""


#Practice1
#1
num1 = int(input('Введіть перше число:'))
num2 = int(input("Введіть друге число:"))
print(num1,num2)

#2
print(num1+num2,num1-num2,num1*num2,num1/num2)

#3
base = int(input('Введіть число:'))
power = int(input('Введіть ступінь до якого піднести Ваше число:'))
c = base ** power
print(base,'в степені',power,'це',c)


#4
num1 = float(input('Введіть перше число:'))
num2 = float(input("Введіть друге число:"))
print(num1+num2,num1-num2,num1*num2,num1/num2)

base = float(input('Введіть число:'))
power = float(input('Введіть ступінь до якого піднести Ваше число:'))
c = base**power
print(base,'в степені',power,'це',c)


#5
name = str(input('''Ваше ім'я:'''))
surname = str(input('Ваше прізвище:'))
age = int(input('Ваш вік:'))
print(name,surname+'\n'+'You are',age,'years old')



#Practice2
#1
a = 50       #1st method
b = 100
var = a
a = b
b = var
print(a,b)

a = 65       #2nd method
b = 78
a = a + b
b = a - b
a = a - b
print(a,b)

a = 100500    #3rd method
b = 6000000
(a,b) = (b,a)
print(a,b)


#2
num_1 = int(input('Enter the first number:'))
num_2 = int(input('Enter the second number:'))
print('Maximum is',max(num1,num2))


#3
num = int(input("Enter a 3-digit number: "))
digit_1 = num % 10
digit_2 = (num // 10) % 10
digit_3 = num // 100
reversed_num = digit_1 * 100 + digit_2 * 10 + digit_3
print("The reversed number is:", reversed_num)

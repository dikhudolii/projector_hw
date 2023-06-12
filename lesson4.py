True and not (3 != 3.0) # Що виведе даний код? Опишіть по крокам що виконується в якій послідовності.
''' 1) спочатку виконується пріорітетність в дужках --> not true aka false
2) далі виконується перша частина
3) В кінці повертається Тру бо дійсні обидві частини 
'''


# Practice session 1
# Figure out the result of the following expressions:
(1 <= 1) and (1 != 1) # false
not (1 != 2) # false
("good" != "bad") or False # true
("good" != "Good") and not (1 == 1) # false
# Make all of them True by adding parentheses:
# a)
False == True
False == (not True)
# b)
True and False == True and False
(True and False) == (True and False)
# c)
not True and "A" == "B"
(not True) and ('A' == ('B'))


# Task 1. Even or odd. Прийняти від користувача число, вивезти чи even/odd
number0 = int(input('Enter a number: '))
if number0 % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')


# Task 2. When provided with a number between 0-9, return it in words. Input :: 1 Output :: "One".
number1 = int(input('Enter a number between 0-9'))
match number1:
    case 0:
        print('Zero')
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case 4:
        print('Four')
    case 5:
        print('Five')
    case 6:
        print('Six')
    case 7:
        print('Seven')
    case 8:
        print('Eight')
    case 9:
        print('Nine')
    case _:
        print('no match found')


# Task 3. Прийняти від користувача два числа і отримати дію над цими числами. Реалізувати +,-, //, , /, *
num1, num2, oper = int(input('Enter the 1st number: ')), int(input('Enter the 2nd number: ')), str(input('Enter an operator: '))
match oper:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        if num2 == 0:
            print('Error')
        else:
            print(num1/num2)
    case '//':
        print(num1//num2)
    case '**':
        print(num1**num2)
    case _:
        print('Error')


# Task 4. Прийняти від користувача name, surname. Вивезти ініціали.
name, surname = str(input('Enter your name: ')), str(input('Enter your surname: '))
print('Your initials are: ' + name[0] + '.' + surname[0])


# Practice section 2
# 1. Write a Python program that reads two integers representing a month and prints the season for that month. Get month from the user input.
month = input("Input the month: ").lower()
if month in ("december", "january", "february"):
    season = "winter"
elif month in ("march", "april", "may"):
    season = "spring"
elif month in ("june", "july", "august"):
    season = "summer"
elif month in ("september", "october", "november"):
    season = "autumn"
else:
    print("Invalid month. Please enter a valid month name.")
print(f"Season is {season}")


# 2. Write a Python program to get next day of a given date. Get day, month and year from the user input.
year, month, day = int(input('Input a year: ')), int(input('Input a month [1-12]: ')), int(input('Input a day [1-31]: '))
# the year is a leap year when it's evenly divisible by 4 and not evenly divisible by 100 OR or evenly divisible by 400
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    leap_year = True
else:
    leap_year = False
# restrictions for month parameter:
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30
# restrictions for day parameter:
if day < month_length:
    day += 1
else:
    day = 1
    # restrictions for month parameter
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


# 3. Get a phrase from user input.
# Display whether the length of the string is longer than 5 characters, equal to 5 characters or shorter than 5 characters.
# Use if, elif, else for this.
phrase = str(input('Enter a phrase: '))

if len(phrase) > 5:
    print('The length is longer than 5 characters.')
elif len(phrase) == 5:
    print('The length is equal to 5 characters.')
else:
    print('The length is shorter than 5 characters.')


# 4. Get a positive number from user input. Find all factors of this number.
pos_num = int(input('Enter a positive number: '))
factors = [i for i in range(1, pos_num + 1) if pos_num % i == 0]

if pos_num < 0:
    print('Error')
else:
    print("The factors of", pos_num, "are:", factors)


# 5. Write a Python program to check a triangle is equilateral, isosceles or scalene. Get all three sides from user input.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a == b == c:
    print("This is an equilateral triangle.")
elif a == b or b == c or c == a:
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")


# Practice section 3
# 1. Write a for loop that prints out the integers from 2 to 10, each on a new line, by using the range() function.
my_range = range(2, 10)
for i in my_range:
    print(i)

print(10)

# 2. Use a while loop that prints out the integers from 2 to 10
i = 1
while i < 10:
    i += 1
    print(i)


# 3. Write a program that takes number as its input and doubles that number few times in a loop.
# Number of iterations and initial number should be taken from user input.
# You should display each result on a separate line.
num = int(input('Enter a number: '))
iter = int(input('Enter a number of iterations: '))

for i in range (iter):
    num *= 2
    print(num)


# 4. Write a program that calculate Fibonacci series.
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on.
# Number of iterations should be taken from user input.
iter = int(input('Enter a number of iterations: '))
a, b = 1, 1

for i in range(iter):
    n = a + b
    print(n)
    a, b = b, a + b


# 5. Write a program that takes a number as input and revert it using math operators.
# Here you should be able to do it not only for three-digit numbers, but for any numbers.
n = int(input('Enter a number: '))
rev = 0

while n > 0:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)


# Practice section 4
# 1. Write a program that always asks user to input somethings. Quit only if user inputs 'q' or 'Q'.
while True:
    inp = str(input('Enter something: '))
    if inp.lower() == 'q':
        break


# 2. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
for i in range(0, 101):
    if i % 3 == 0:
        print(i)


# 3. Get a number from user input and iterate from 0 to that number.
num = int(input('Enter a number: '))

for i in range(0, num):
   # Print 'foobar' if the number is divisible by both 3 and 5.
    if num % 3 == 0 and num % 5 == 0:
        print('foobar')
    # Print 'foo' if the number is divisible by 3.
    elif num % 3 ==0:
        print('foo')
    # Print 'bar' if the number is divisible by 5.
    elif num % 5 == 0:
        print('bar')
    else:
    print(num)







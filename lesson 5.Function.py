# Task 3. Розвернути строку
# за допомогою циклу
string = 'abcdefg'
integer = 10
new_string = ''
for i in range(len(string)-1, -1, -1):
    new_string += string[i]
print(new_string)
# slice
print(string[::-1])
# function
def mirror(string: str):
    new_string = ''
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    return new_string

 print(mirror(str(integer)))


# Practice section 1:
# Write a program that calculate Fibonacci series.
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on.
# Number of iterations should be taken from user input.
n = int(input('Enter a number of iterations: '))

def fib(n):
    a,b = 1,1
    for i in range(n):
        a, b = b, a + b
    return b
print(fib(n))


# Practice section 2:
# 1. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
def div_by_n(n: int = 3) -> int:
    for i in range(0, 101):
        if i % n == 0:
            print(i)
div_by_n()

# Get a number from user input and iterate from 0 to that number.
# Print 'bar' if the number is divisible by 5.
# Print 'foo' if the number is divisible by 3.
# Print 'foobar' if the number is divisible by both 3 and 5.
def foobar(num: int):
    if num % 3 == 0 and num % 5 == 0:
        print('foobar')
    elif num % 3 == 0:
        print('foo')
    elif num % 5 == 0:
        print('bar')

n = int(input('Enter a number: '))
for i in range(n + 1):
    print('i: ', i)
    foobar(i)


# Practice section 3:
# 1. Write a function called square() with one argument of int type and returns the value of that number raised to the second power.
def square(n: int) -> int:
    return n ** 2

print(square(4))


square_lambda = lambda n: n ** 2
print(square_lambda(4))


# 2. Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit.
# It should take a number as an argument from user input and return a number to the console.
def convert_cel_to_fahr(cel: int) -> int:
# To convert Celsius to Fahrenheit we need to multiply the temperature in Celsius with two and add 30
    fahr = cel * 2 + 30
    return fahr

user_cel = int(input('Enter a temperature in Celsius: '))
print(f"The Fahrenheit temperature is {convert_cel_to_fahr(user_cel)} degrees")

# Write a function that implement case swapping. It should return the same result as swapcase() method.
# Your function should accept one str argument and convert all lower case values to upper case and vice versa.
def swapcase(input_string: str) -> str:
    output = ""
    for char in input_string:
        if char.islower():
            output += char.upper()
        elif char.isupper():
            output += char.lower()
        else:
            output += char
    return output

print(swapcase('HelLo'))

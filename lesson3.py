# Task 1. Прийняти від користувача(вас) два числа, і реалізувати операцію %, за допомогою інших функцій
num1 = int(input('enter a number: '))
num2 = int(input('enter a number: '))
var_1 = int(num1 / num2)
var_2 = var_1 * num2
remainder = int(num1 - var_2)
print(remainder)

# Task 2. Порахувати скільки секунд в одному дні.
sec_per_hour = 60
min_per_hour = 60
sec_per_hour = sec_per_hour * min_per_hour
hours_per_day = 24
sec_per_day = sec_per_hour * hours_per_day
print(sec_per_day)
# 2.* Секунд в роках
sec_per_year = sec_per_day * 365
print(sec_per_year)

# Practice chapter 2.

# Print the text in which there will be a quote with double quotes.
print('One of my favorite songs is "Heroin" by Lana del Rey.')
# Print the text in which there will be an apostrophe.
print("I don't like this food.")
# Print a line that will be displayed on several lines.
print(
    "Swingin' in the backyard, pull up in your fast car \nWhistlin' my name \nOpen up a beer and you say, 'Get over here \nAnd play a video game'")
# Print text that doesn`t fit in one line but will be displayed in one line
print(
    'Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss for HBO. It is an adaptation of A Song of Ice and Fire, a series of fantasy novels by George R. R. Martin, the first of which is A Game of Thrones. The show was shot in the United Kingdom, Canada, Croatia, Iceland, Malta, Morocco, and Spain. It premiered on HBO in the United States on April 17, 2011, and concluded on May 19, 2019, with 73 episodes broadcast over eight seasons.')

# Test task 1. знайти парні числа
numbers = '123456789'
print(numbers[1::2], numbers[-2::-2])

# Task 2. Отримати строку від користувача. Вивезти в консоль чи є строка паліндромом
string = str(input('enter a string:'))
print(string == string[::-1])

# Practice chapter 3

# Create a variable with data type string. Count the length of this line.
var1 = str("I'm Diana.")
print(len(var1))
# Create another variable with string data type. Output the result of concatenation of these two variables.
var2 = str('I like hot yoga.')
print(var1 + var2)
# Print the two previous variables, but with a space between them.
print(var1 + ' ' + var2)
# Get a string from user input. Check if the string is a palindrome.
user_hobby = str(input('Enter your hobby:'))
print(user_hobby == user_hobby[::-1])
# Replace age in the following string with your age. "I'm 10 years old" -> "I'm 30 years old". Do it with:
# a) indexing
string = "I'm 10 years old"
new_string = string[:4] + '20' + string[6:]
print(new_string)
# b) replace function
print(string.replace('10', '20'))

# Practice chapter 4

# The program receives user's name and age from input. Then you need to display the name and age in one line in several ways:
name = input('Enter your name: ')
age = input('Enter your age: ')
# a) by listing all the parameters in the print function
print('Your name is', name, 'and your age is', age, 'years old')
# b) by formatting a string using the format function
print('Your name is {name} and your age is {age} years old'.format(name=name, age=age))
# c) by formatting a string with f-string
print(f'Your name is {name} and your age is {age} years old')

# Practice chapter 5

# There are the following lines of code:
string_1 = "Animals  "
string_2 = "  Badger"
string_3 = "honey bee"
string_4 = "   HoneyPot   "
# Print each of these lines with the following conditions
# 1. All letters must be written in lowercase.
print(string_1.lower(), string_2.lower(), string_3.lower(), string_4.lower())
# 2. All letters must be capitalized.
print(string_1.upper(), string_2.upper(), string_3.upper(), string_4.upper())
# 3. Remove all spaces:
# a) from the beginning of the line
print(string_1.lstrip(), string_2.lstrip(), string_3.lstrip(), string_4.lstrip())
# b) from the end of the line
print(string_1.rstrip(), string_2.rstrip(), string_3.rstrip(), string_4.rstrip())
# c) on both sides of the line
print(string_1.strip(), string_2.strip(), string_3.strip(), string_4.strip())

# 4. Check the value of the startwith ('be') function for each line:
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
print(string_1.startswith('be'), string_2.startswith('be'), string_3.startswith('be'), string_4.startswith('be'))
# Convert all rows with methods so that when using startwith ('be') it returns True.
print(string_1.lower().startswith('be'), string_2.startswith('be'), string_3.lower().startswith('be'),
      string_4.lower().startswith('be'))

# 5. Find and replace all letters 's' with the letter 'x' in the following line:
string = 'Somebody said something to Samantha.'
print(string.replace('s', 'x'))

# 6. Write a program that receives a phrase and letter from the user and returns "Yes!" if you find this letter in a line.
line, letter = input('Enter a phrase: '), input('Enter a letter: ')
print("Yes!" if letter in line else "No!")
#OR
print("Yes!" if line.find(letter) != -1 else "No!")
# не розумію як не використовувати if взагалі(((

# Clean the following line with string methods and output only the numbers:
line = '12345!,_6--'
line1 = line.replace('!,_', '')
line2 = line1.replace('--', '')
numbers = ' '.join(line2)
print(numbers)

# 8. At the input we get two numbers - the numerator and denominator of the fraction. Display the number as a percentage in the console.
numerator, denominator = int(input('Enter the numerator: ')), int(input('Enter the denominator: '))
percentage = int((numerator / denominator) * 100)
print (str(percentage) + '%')

# 9. Find a secret message in the following text: 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'
text = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'
text = text.replace('X', '')
text = text.replace('x', '')
print(text[::-1])

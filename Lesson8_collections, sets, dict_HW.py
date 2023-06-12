# # Task 1. Given two non-negative integers low and high.
# # Return the count of odd numbers between low and high (inclusive).
# def count_odd_numbers(a: int, b: int) -> int:
#     count = 0
#     odd = []
#     for i in range(a, b+1):
#         if i % 2 != 0:
#             odd.append(i)
#             count += 1
#     print(f'The odd numbers between {a} and {b} are: {odd}')
#     return count
#
#
# low = int(input('enter a number:'))
# high = int(input('enter a number bigger than previous: '))
#
# count_odd_numbers(low, high)
#
#
#
# # Task 2. You are given an array of unique integers salary where salary[i] is the salary of the i-th employee.
# # Return the average salary of employees excluding the minimum and maximum salary.
# salary = [int(i) for i in input('Enter salaries separated by a comma: ').strip().split(',')]
# print(f'Inputted salary range: {salary}')
#
#
# def defining_max_min(salary_list:list[int]) -> int:
#     max_salary = max(salary_list)
#     min_salary = min(salary_list)
#     print(f'Maximum salary is {max_salary} and minimum salary is {min_salary}')
#     salary_list.remove(max_salary)
#     salary_list.remove(min_salary)
#     print(f'The renewed salary list for calculating the average: {salary_list}')
#
#
# defining_max_min(salary)
#
#
# def average_salary(salary_list:list) -> int:
#     avg = sum(salary_list)/len(salary_list)
#     print(f'The average salary is {sum(salary_list)} / {len(salary_list)} = {avg}')
#
#
# average_salary(salary)
#
#
#
# # Practice 1:
# # Create emtpy dictionary named en_ua_dictionary.
# en_ua_dictionary = {}
# # Add few key-value pairs to the dictionary. Example: 'red': 'червоний'
# en_ua_dictionary["red"] = 'червоний'
# en_ua_dictionary["cat"] = 'кішка'
# en_ua_dictionary["sun"] = 'сонце'
# en_ua_dictionary["table"] = 'стіл'
#
# print(en_ua_dictionary)
# # Check if the dictionary contains key 'blue' and 'purple'. If not, set their values to unknown.
# print(en_ua_dictionary.get('blue'))
# print(en_ua_dictionary.get('purple'))
# # Keys 'blue' and 'purple' return as 'None', so:
# en_ua_dictionary["blue"] = 'unknown'
# en_ua_dictionary["purple"] = 'unknown'
#
# print(en_ua_dictionary)
# # Create a loop over existing values and print them to the console in the following format: Red in Ukrainian is червоний
# for en, ukr in en_ua_dictionary.items():
#     print(f'{en} in Ukrainian is {ukr}')
# # Delete all key-values pairs from the dictionary if the lenght of value is lower than 5.
# for key, value in list(en_ua_dictionary.items()):
#     if len(value) < 5:
#         del en_ua_dictionary[key]
#
# print(en_ua_dictionary)


# Write a game where user should guess of a capital of the country that you have in your dictionary.
import random

capitals = {
    'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome',
    'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna',
    'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen',
    'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia',
    'Greece': 'Athens'
}

score = 0
total_questions = 0

while True:
    # Pick a random country
    country = random.choice(list(capitals.keys()))

    # Ask user to guess the capital
    answer = input(f"What is the capital of {country}? ")

    # Check if user wants to exit the game
    if answer.lower() == "exit":
        break

    # Check if user's guess is correct
    if answer == capitals[country]:
        print("You are right!")
        score += 1
    else:
        # Give user one more chance to guess
        answer = input(f"Sorry, that's incorrect. Please guess again: ")
        if answer == capitals[country]:
            print("You are right!")
            score += 1
        else:
            print(f"Sorry, the capital of {country} is {capitals[country]}.")

    total_questions += 1
    print(f"Your current score is {score}/{total_questions}\n")

print(f"Your final score is {score}/{total_questions}. Thanks for playing!")



# OPTION A:
# Give user a hint if he guesses wrong. Hint should looks like first letter of the capital.
# If user makes another mistake, you should print one more letter from the capital.
score = 0
total_questions = 0

while True:
    # Pick a random country
    country = random.choice(list(capitals.keys()))

    # Ask user to guess the capital
    answer = input(f"What is the capital of {country}? ")

    # Check if user wants to exit the game
    if answer.lower() == "exit":
        break

    # Check if user's guess is correct
    if answer == capitals[country]:
        print("You are right!")
        score += 1
    else:
        # give user a hint with the 1st letter
        answer = input(f"Sorry, that's incorrect. Please guess again, the 1st letter is : {capitals[country][0]}: ")
        if answer == capitals[country]:
            print("You are right!")
            score += 1
        else:
            answer = input(f"Sorry, that's incorrect. Please guess again, the 1st letter is : {capitals[country][0:2]}: ")
            if answer == capitals[country]:
                print("You are right!")
                score += 1
            else:
                print(f"Sorry, the capital of {country} is {capitals[country]}.")

    total_questions += 1
    print(f"Your current score is {score}/{total_questions}\n")

print(f"Your final score is {score}/{total_questions}. Thanks for playing!")



# OPTION B:
# If user make a mistake you should decrement his lives. Initial amount of lives is 3. Game will end when user has no lives left.
# You should print the final score after user has no lives left.
score = 0
lives = 3
total_questions = 0

while lives > 0:
    # Pick a random country
    country = random.choice(list(capitals.keys()))

    # Ask user to guess the capital
    answer = input(f"What is the capital of {country}? ")

    # Check if user wants to exit the game
    if answer.lower() == "exit":
        break

    # Check if user's guess is correct
    if answer == capitals[country]:
        print("You are right!")
        score += 1
    else:
        # Decrement lives and print remaining lives
        lives -= 1
        print(f"Sorry, that's incorrect. You have {lives} lives remaining.")

        if lives == 0:
            break

        # give user a hint with the 1st letter
        answer = input(f"Sorry, that's incorrect. Please guess again, the 1st letter is : {capitals[country][0]}: ")
        if answer == capitals[country]:
            print("You are right!")
            score += 1
        else:
            # Decrement lives and print remaining lives
            lives -= 1
            print(f"Sorry, that's incorrect again. You have {lives} lives remaining.")

            if lives == 0:
                break

            # Give user another hint
            answer = input(f"Sorry, that's incorrect. Please guess again, the 1st letter is : {capitals[country][0:2]}: ")
            if answer == capitals[country]:
                print("You are right!")
                score += 1
            else:
                # Decrement lives and print remaining lives
                lives -= 1
                print(f"Sorry, that's incorrect again. You have {lives} lives remaining.")

                if lives == 0:
                    break


    total_questions += 1
    print(f"Your current score is {score}/{total_questions}\n")

print(f"Game over! Your final score is {score}/{total_questions}. Thanks for playing!")


# Optional task:
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def roman_to_int(s: str) -> int:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer_value = 0
    prev_value = 0

    # Iteration over the characters in the Roman numeral string from right to left
    for i in range(len(s) - 1, -1, -1):
        current_value = roman_dict.get(s[i])

        # If the current value is less than the previous value, we subtract the current value from the integer value
        if current_value < prev_value:
            integer_value -= current_value
        # Otherwise, we add the current value to the integer value
        else:
            integer_value += current_value

        # Set the previous value to the current value for the next iteration
        prev_value = current_value

    return integer_value


roman_to_int(str(input('Please, enter a roman number to convert: ')))


def test_roman_to_int():
    result1 = roman_to_int("III")
    assert result1 == 3

    result1 = roman_to_int("LVIII")
    assert result1 == 58

    result1 = roman_to_int("MCMXCIV")
    assert result1 == 1994


# Try to create a function that will do reverse operation - from integer to roman
def int_to_roman(s: int) -> str:
    roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_value = ''

    while s > 0:
        for key in sorted(list(roman_dict.keys()), reverse=True):
            if key > s:
                pass
            elif key <= s:
                s -= key
                roman_value += roman_dict.get(key)
                break

    return roman_value


int_to_roman(int(input('enter a number: ')))


def test_int_to_roman():
    result1 = int_to_roman(3)
    assert result1 == "III"

    result1 = int_to_roman(58)
    assert result1 == "LVIII"

    result1 = int_to_roman(1994)
    assert result1 == "MCMXCIV"


# Task 3:
# In an array of integers of length n + 1 (n > 1), every number in the range 1...n appears once except for one number which appears twice (so the array’s length is n+1).
# Write an efficient function that finds the number that appears twice.
def task3(arr: list) -> int:
    return [i for i in set(arr) if arr.count(i) == 2] if not arr == False else 'Emp list'


task3([1, 2, 3, 4, 5, 6, 6, 7])


def task3(arr: list) -> int:
    for i in set(arr):
        if arr.count(i) > 1:
            return i


task3([1, 2, 3, 4, 5, 6, 6, 7])


# Task 4: Intersection
# Given two arrays of numbers where each one contains unique values and is already sorted in ascending order, find the number of elements that belong to both arrays.
def task4(arr1: list, arr2: list) -> int:
    return len(set(arr1) & set(arr2)) if not arr1 == False and not arr2 == False else 'Emp list'


task4([1, 2, 3, 4], [1, 2, 5, 6])


# Task 5. RLE (Run-Length Encoding)
# Given a string of letters (without numbers), create a string encoding it by the rules where the first character is char itself,
# followed by a number indicating the number of letter repeats.

# Examples:
# ABBA => A1B2A1 ATTTGC => A1T3G1C1
def rle(s):
    count_ = 1
    encoded = ''
    sym = ''
    for i in s:
        if i == sym:
            count_ += 1
        if i != sym and sym != '':
            encoded += f"{sym}{count_}"
            count_ = 1
        sym = i

    encoded += f"{sym}{count_}"

    return encoded


rle('AAABBCBBACBACCC')





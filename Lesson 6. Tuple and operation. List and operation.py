# Practice block 1:

# Create an outer function that will accept two parameters, a and b
def outer(a: int or str, b: int or str) -> int or str:
    # Create an inner function inside an outer function that will calculate the addition of a and b
    def inner():
        return a + b

    # At last, an outer function will add 5 into addition and return it
    return inner() + 5


outer(5, 5)


# Task 1:
# Write a function that can verify if the given integer n is a perfect number, and return True if it is, or return False if not.
def perf(given_int: int) -> bool:
    # A perfect number is a number in which the sum of its divisors (excluding itself) are equal to itself.
    divisor_sum = sum(i for i in range(1, given_int) if given_int % i == 0)
    return divisor_sum == given_int


num = int(input('Enter an integer: '))
print(perf(num))


# Practice block 2

# 1. Write a program that asks user to enter an integer and convert it to int.
def conv(given_num: str):
    try:
        # if user inputs an integer, program should print this number and quit w/o any error.
        given_num = int(given_num)
        print(given_num)
        # If the user enters something that is not an integer, program should catch an error and ask the user to enter an integer again.
    except ValueError:
        conv(input('Enter an integer again'))


conv(input())


# 2. Write a program that asks the user to input a string and an integer n. Then display the character at index n in the string.You should handle an error properly and display proper error message.
def index(string: str, n: int) -> str:
    try:
        return string[n]
    except IndexError:
        return index(string, int(input('Wrong index. Enter the index again: ')))
    except TypeError:
        return index(string, int(input('Index must be an integer. Enter the integer again: ')))


index(input('Enter a string: '), input('Enter an index: '))

# Practice block 3:

# 1. Write a function that simulate a dice roll and returns the result from 1 to 6.
import random

def roll_dice():
    return random.randint(1, 6)


# 2. Write a function that simulate 10_000 rolls and returns the number of times that the dice rolled for each value
def cases():
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    for _ in range(10000):
        v = rd.randint(1, 6)

        match v:
            case 1:
                a += 1
            case 2:
                b += 1
            case 3:
                c += 1
            case 4:
                d += 1
            case 5:
                e += 1
            case 6:
                f += 1

    print(a, b, c, d, e, f)


cases()


# Simulate an election for two candidates.
def elections():
    # Program should take amount of regions and rating for 1st candidate in each region (in percentage).
    num_of_regions = int(input('Enter a number of regions: '))
    candidate1_regions_rates = ()
    print(f'Number of regions: {num_of_regions}')
    # Program should run election in every region.
    for _ in range(num_of_regions):
        rate_for_cand1 = float(input('Enter a rate for candidate 1: '))
        candidate1_regions_rates = candidate1_regions_rates + (rate_for_cand1,)


    for rate_for_cand1 in candidate1_regions_rates:
        rate_for_cand2 = 100 - rate_for_cand1

        print(f'Rates for candidate 1: {rate_for_cand1} and candidate 2: {rate_for_cand2}')
    # In every region, program should ask 10 000 voters.
    cand1_total = sum(candidate1_regions_rates) * num_of_regions * 10000
    cand2_total = num_of_regions * 10000 - cand1_total
    # Candidate count as a winner if he gains more than 50% of all votes.Program should print the result of the election for each region and the winner
    if cand2_total < cand1_total:
        print('Candidate 1 has won elections')
    if cand1_total < cand2_total:
        print('Candidate 2 has won elections')
    if cand1_total == cand2_total:
        print('draw')


elections()


# Practice block 4

# Create a tuple with your first name, last name, and age.
my_tuple = ('Diana', 'Khudolii', '20')
# Print your last name using indexing.
print(my_tuple[1])
# Create three variables in one line that extracted from tuple that you created in step 1.
name = my_tuple[0]
surname = my_tuple[1]
age = my_tuple[2]
# Print your name letter by letter from this tuple
for i in name:
    print(i)
# Create a new tuple that contains all info from the first tuple but remove first letter from all strings
new_tuple = tuple([s[1:] for s in my_tuple])

print(new_tuple)
# Create a tuple with two values. First one is (1, 2), second one is (3, 4).
tuple_ = ([1, 2], [3, 4])
# Create a program that calculates the sum of all values in the tuple and print it to the console.
total_sum = sum(tuple_[0]) + sum(tuple_[1])
print(total_sum)

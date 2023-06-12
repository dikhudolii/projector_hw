# Task 1:
# Створити два списка, number, square, користувач вводить перший список(з консолі), після цього ми повертаемо квадрат до кожного числа.
# Використати try/except
def squared_list():
    number = []
    square = []
    try:
        n = int(input("Enter the length of the list: "))
        for i in range(n):
            num = int(input("Enter a number for the list: "))
            number.append(num)
            square.append(num * num)
    except ValueError:
        print("Помилка! Введіть ціле число.")
        return None
    return square


print(squared_list())


# Написати функцію з тестами
def test_squared_list():
    assert squared_list() == [1, 1, 1, 1], "Test case 1 failed"
    assert squared_list() == [], "Test case 2 failed"
    assert squared_list() == None, "Test case 3 failed"
    print("All test cases passed")


test_squared_list()


# Task 2:
# In this task you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def filtering(arr: list) -> list:
    return [i for i in arr if isinstance(i, int)]


lst = [1, 2, 3, 4, 'diana', 456, 'diana']
filtering(lst)


# Practice block 1

# Write a Python program to compute the difference between two lists.
def compute_difference(first: list, second: list) -> tuple:
    # compute the difference between the two lists
    first_minus_second = [x for x in first if x not in second]
    second_minus_first = [x for x in second if x not in first]
    return (first_minus_second, second_minus_first)


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 5, 6])

    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])

    # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.


def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]


# print(sum_of_two([2, 7, 11, 15], 13))


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 13)
    assert result1 == [0, 2]

    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]

    result3 = sum_of_two([3, 3], 6)
    assert result3 == [0, 1]

    print('All tests passed successfully')


test_sum_of_two()


# Practice block 2:

# 1. Create a list with next values [1, 4, 2, 5]. Create a sorted copy of that list w/o changing the original list.
lst = [1, 4, 2, 5]
sorted_lst = sorted(lst)

print(lst)
print(sorted_lst)

# 2. Sort the following list by population. Calculate average and total population for cities from this list:
city_pop = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]

sorted_city_pop = sorted(city_pop, key=lambda x: x[1])

total_pop = sum(city[1] for city in sorted_city_pop)
average_pop = total_pop / len(sorted_city_pop)

print("Sorted list by population:")

for city in sorted_city_pop:
    print(f"{city[0]}: {city[1]}")

print('***********************************')

print(f"Total population: {total_pop}")
print(f"Average population: {average_pop}")

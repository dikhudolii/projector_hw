# 1. Write a decorator that ensures a function is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs

def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('user_type') != 'admin':
            raise ValueError('Permission denied')
        else:
            return func(*args, **kwargs)

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    # some very dangerous operation
    print("Showing customer receipt...")


try:
    show_customer_receipt(user_type='user')
except ValueError as v:
    print(v)

try:
    show_customer_receipt(user_type='admin')
except ValueError as v:
    print(v)


# 2. Write a decorator that wraps a function in a try-except block and print an error if error has happened
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__} {str(e)}")
        return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})


# 3. Optional: Create a decorator that will check types.
# It should take a function with arguments and validate inputs with annotations.
def check_types(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for arg_index in range(len(args)):
            actual_type = type(args[arg_index])
            arg_name = list(annotations.keys())[arg_index]
            needed_type = annotations[arg_name]

            if actual_type != needed_type:
                raise TypeError(f'Argument a must be {needed_type}, not {actual_type}')

        for k, v in kwargs.items():
            if type(v) != annotations[k]:
                raise TypeError(f'Argument a must be {annotations[k]}, not {type(v)}')

        return func(*args, **kwargs)

    return wrapper


@check_types
def add(a: int, b: int, c: str = None) -> int:
    return a + b


add(1, 2)
# > 3
add("1", "2")


# > TypeError: Argument a must be int, not str


# 4. Create a function that caches the result of a function, so that if it is called with same argument multiple times,
# it returns the cached result first instead of re-executing the function.
def cache_results(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@cache_results
def some_function(a, b):
    pass


some_function(1, 2)


# task 1, another way
def role_required(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 'user_type' in kwargs and kwargs['user_type'] == role:
                return print("Successfully connected")
            else:
                raise PermissionError("User does not have the required role.")

        return wrapper

    return decorator


@role_required('admin')
def admin_function(*args, **kwargs):
    pass


admin_function(user_type='admin')
admin_function(user_type='user')

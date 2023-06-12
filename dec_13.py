import time


def dec_pr(func):
    def wrapper():
        print('We are executing wrapper, then we will execute func')
        func()

    return wrapper


def repeat(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        _ = func(*args, **kwargs)
        print(f"Execution time is {time.time_ns() - start}")

    return wrapper


@repeat
def pr(a, b, c, d=None):
    return f'We are printing {a} {b} {c}'


# pr = repeat(pr)

@repeat
def pr2(a, b):
    for _ in range(100000000):
        pass
    print(f'{a} {b} without c')





pr(1, 2, 3)
pr2(4, 5)



class A:
    def b(self):
        print("b")



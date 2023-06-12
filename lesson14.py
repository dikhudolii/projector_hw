# 1. Modify the Country class to include a third instance attribute called capital as a string.
# Store your new class in a script and test it out by adding the following code at the bottom of the script:
# japan = Country('Japan', 140_000_000, 'Tokyo')
# print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
# The output of your script should be:
# Japan population is 140000000 and capital is Tokyo.


class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


# Add increase_population method to country class.
# This method should take an argument and increase population of the country on this number.
class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def increase_population(self, increase_amount):
        self.population += increase_amount


# Create add method to add two countries together.
# This method should create another country object with the name of the two countries combined
# and population of the two countries added together.
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


# Optional) Implement previous method with magic method
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


# Create a Car class with the following attributes: brand, model, year, and speed.
# The Car class should have the following methods: accelerate and brake.
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5


# Create a Robot class with the following attributes: orientation, position_x, position_y.
# The Robot class should have the following methods: move, turn, and display_position.
class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    # The move method should take a number of steps and move the robot in the direction it is currently facing.
    def move(self, steps):
        if self.orientation == 'up':
            self.position_y += steps
        elif self.orientation == 'down':
            self.position_y -= steps
        elif self.orientation == 'left':
            self.position_x -= steps
        elif self.orientation == 'right':
            self.position_x += steps

    # The turn method should take a direction (left or right) and turn the robot in that direction.
    def turn(self, direction):
        if direction == 'left':
            if self.orientation == 'up':
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.orientation = 'up'
        elif direction == 'right':
            if self.orientation == 'up':
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.orientation = 'up'

    # The display_position method should print the current position of the robot.
    def display_position(self):
        print(f"Current position: ({self.position_x}, {self.position_y})")


class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance += (self._balance * self._interest_rate)


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit


class Bank:
    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def test_accounts(self):
        self._accounts.append(SavingsAccount(500.0, 'SA1', 0.05))
        self._accounts.append(CurrentAccount(200.0, 'CA1', -1000.0))
        self._accounts.append(Account(1000.0, 'A1'))


    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                if account.get_balance() < 0:
                    print(f"Sending overdraft warning to account {account.get_account_number()}")


    def open_account(self, account_type, account_number, initial_balance=0.0,
                     interest_rate=0.0, overdraft_limit=0.0):
        if account_type == 'savings':
            account = SavingsAccount(initial_balance, account_number, interest_rate)
        elif account_type == 'current':
            account = CurrentAccount(initial_balance, account_number, overdraft_limit)
        else:
            account = Account(initial_balance, account_number)
        self._accounts.append(account)

    def close_account(self, account_number):
        for account in self._accounts:
            if account.get_account_number() == account_number:
                self._accounts.remove(account)
                print(f"Account {account_number} closed")
                return
        print(f"Account {account_number} not found")

    def pay_dividend(self, dividend_amount):
        for account in self._accounts:
            account.deposit(dividend_amount)
            print(f"Paid dividend of {dividend_amount} to account {account.get_account_number()}")


if __name__ == '__main__':
    japan = Country('Japan', 140_000_000, 'Tokyo')
    print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")

    japan = Country('Japan', 140_000_000, 'Tokyo')
    print(f"Before increase: {japan.name} population is {japan.population}.")

    japan.increase_population(500_000)
    print(f"After increase: {japan.name} population is {japan.population}.")

    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)

    bosnia_herzegovina = bosnia + herzegovina
    print(f"{bosnia_herzegovina.name} population is {bosnia_herzegovina.population}.")

    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)

    bosnia_herzegovina = bosnia.add(herzegovina)
    print(f"{bosnia_herzegovina.name} population is {bosnia_herzegovina.population}.")

    my_car = Car('Toyota', 'Camry', 2022)
    print(my_car.speed)

    my_car.accelerate()
    print(my_car.speed)

    my_car.brake()
    print(my_car.speed)

    my_robot = Robot('up', 0, 0)
    my_robot.move(5)
    my_robot.turn('right')
    my_robot.move(3)
    my_robot.display_position()

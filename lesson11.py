import json
import requests

# Вивеcти з API(приватбанка) курс валют для:
my_currencies = {
    'UAH': '🇺🇦',
    'USD': '🇺🇸',
    'EUR': "🇪🇺",
    'GBP': '🇬🇧',
    'PLN': '🇵🇱',
    'CAD': '🇨🇦',
}


def get_response(url, params=None):
    response_ = requests.get(url, params=params)
    if response_.status_code == 200:
        return response_
    else:
        raise Exception(f"Request to {url} returned a status code of {response_.status_code}")


url_pryvatbank = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=06.05.2023'


def task1():
    my_rates = []

    res_pryvatbank = get_response(url_pryvatbank)

    for obj in res_pryvatbank.json().get('exchangeRate', []):
        if obj['currency'] in my_currencies and obj not in my_rates:
            my_rates.append(obj)

    for rate in my_rates:
        print(f'{my_currencies[rate["currency"]]} {rate["purchaseRateNB"]} / {rate["saleRateNB"]}')


task1()

# user input exchange rates
my_currencies_dict = {
    'CHF': '🇨🇭',
    'EUR': '🇪🇺',
    'GBP': '🇬🇧',
    'PLN': '🇵🇱',
    'SEK': '🇸🇪',
    'UAH': '🇺🇦',
    'USD': '🇺🇸',
    'XAU': '🇦🇱',
    'CAD': '🇨🇦'
}


def task2():
    user_input = input('Enter a currency code: ').upper()

    output = None

    res_pryvatbank = get_response(url_pryvatbank)

    for obj in res_pryvatbank.json().get('exchangeRate', []):
        if obj['currency'] in my_currencies_dict and user_input == obj['currency'].upper():
            output = obj

    if output:
        print(f'{my_currencies_dict[output["currency"]]} {output["purchaseRateNB"]} / {output["saleRateNB"]}')
    else:
        print(f'Error: could not find exchange rate for currency {user_input}')


task2()


# Practice:
# Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result
def task3():
    search_term = input("Enter a search term: ")

    url_giphy = "http://api.giphy.com/v1/gifs/search"
    api_key = "rVo5bz067UGMHU9iyEgA08GWHvieHkav"
    giphy_params = {
        "q": search_term,
        "api_key": api_key,
    }

    response_giphy = get_response(url_giphy, giphy_params)
    data = json.loads(response_giphy.content)

    for gif in data["data"]:
        print(gif["url"])


task3()


# Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода, вологість і тд)
# https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа
def task4():
    api_key = 'e10aa2cf98d38fb13c1241f2c7c8f8bb'
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    location = input("Enter a location: ")

    weather_params = {"q": location, "appid": api_key}

    try:
        response = get_response(base_url, weather_params)

        if response:
            data = response.json()
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print(f"The temperature in {location} is {temperature} K.")
            print(f"The humidity in {location} is {humidity}%.")
            print(f"The weather in {location} is {description}.")

    except Exception:
        print(f"Error: Could not retrieve weather information for {location}.")


task4()


# Вивеcти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json
def task5():
    url_cosmo = 'http://api.open-notify.org/astros.json'

    res_cosmo = get_response(url_cosmo)

    cosmonauts = res_cosmo.json().get('people', [])
    num_cosmonauts = len(cosmonauts)
    cosmonaut_names = [cosmonaut['name'] for cosmonaut in cosmonauts]

    print(f'There are {num_cosmonauts} cosmonauts:')
    for name in cosmonaut_names:
        print(name)


task5()

"""
countries = {}
countries["Polska"] = ("Warszawa", 37.97)
countries["Niemcy"] = ("Berlin", 83.02)
countries["Słowacja"] = ("Bratysława", 5,45)

for country in countries.keys():
    print(country)

country = input("Informacje o kraju ")

countries_inf = countries.get(country)

print()
print(country)
print("---------------------------")
print("Stolica: " + countries_inf[0])
print("Liczba mieszk: " + str(countries_inf[1]))


countries = {}
countries["Polska"] = ("Warszawa", 37.97)
countries["Niemcy"] = ("Berlin", 83.02)
countries["Słowacja"] = ("Bratysława", 5,45)

def show_country(country):
    countries_inf = countries.get(country)
    print()
    print(country)
    print("---------------------------")
    print("Stolica: " + countries_inf[0])
    print("Liczba mieszk: " + str(countries_inf[1]))


country = input("Informacje o kraju ")
show_country(country)

"""

def display_sum(a, b):
    print(a+b)

def calculate_sum(a, b):
    return a + b

sum = display_sum(1, 2)
print(sum)

calc = calculate_sum(1, 2)
print(calc)

def massage():
    print("To jest tylko wiadomość")

massage()

def calculate_sum(a, b):
    print(a+b)
    return a + b

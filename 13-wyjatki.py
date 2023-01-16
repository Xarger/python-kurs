countries = {'Poland': 'Warsaw', 'Czechia': 'Prague', 'Germany': 'Berlin'}

try:
    print(2 / 0)
    print(countries['USA'])
except KeyError:
    print("klucza nie ma")
except ZeroDivisionError:
    print("Nie mozna dzielic przez zero")
finally:
    print("to wykona sie zawsze")
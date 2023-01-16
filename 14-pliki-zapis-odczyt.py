file = open("countries_and_capitals.txt", "w+")

countries = {'Poland': 'Warsaw', 'Czechia': 'Prague', 'Germany': 'Berlin'}

for country, capital in countries.items():
    file.write(country + "-" + capital + "\n")

file.close()

file = open("countries_and_capitals.txt")

for line in file.readlines():
    print(line.strip())

file.close()
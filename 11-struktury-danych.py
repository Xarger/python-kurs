"""
names_list = []
names_list.append("Kamil")
names_list.append("Mariusz")

names_list = ["Marcin", "Kamil", "Adam", "Kamil"]
print(names_list)

names_list.reverse()
names_list.sort()
for name in names_list:
    print(name)

print(names_list[0])

print(names_list.count("Kamil"))
print(len(names_list))

print(names_list)
print(names_list.pop(0))
print(names_list)

names_list.remove("Kamil")
print(names_list)

names_list.clear()
print(names_list)

names_list1 = ["Marcin", "Kamil", "Adam", "Kamil"]
names_list2 = ["Greg", "Kamil"]
names_list3 = names_list1 + names_list2
print(names_list3)

names_list3.sort()
print(names_list3)

names_list3.sort(reverse=True)
print(names_list3)

#KROTKA

names_list = ("Marcin", "Brzesinski", 32)
print(len(names_list))
print(names_list.count("Marcin"))
print(names_list)

#SET czyli zbiory
names_set = {"Marcin", "Kamil", "Kamil"}
print(names_set)

names_set_empty = set()
names_set_empty.add("Kamil")
names_set_empty.add("Krzysiek")

names_set_empty.remove("Kamil")
names_set_empty.discard("Kamil")

for name in names_set_empty:
    print(name)


names_set = set()

names_set.add("Kamil")
names_set.add("Dominik")

names_set2 = {"Mariusz", "Tytus"}
names_set3 = names_set.union(names_set2)

for name in names_set3:
    print(name)

names_set.update(names_set2)

for name in names_set:
    print(name)



names_set = set()

names_set.add("Kamil")
names_set.add("Dominik")

names_set2 = {"Mariusz", "Tytus", "Kamil"}

# names_set3 = names_set.difference(names_set2)
#names_set3 = names_set.intersection(names_set2)

names_set3 = names_set.symmetric_difference(names_set2)

# names_set3.clear()

for name in names_set3:
    print(name)



names_set = set()

names_set.add("Kamil")
names_set.add("Dominik")

names_set2 = {"Mariusz", "Tytus", "Kamil"}

names_list = ["Artus", "Rafał"]

names_list.extend(names_set2)

print(names_list)

"""
# Slownik, nie mozna miec tych samych kluczy

countrie_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countrie_and_capitals["Czechia"] = "Prague"

print(countrie_and_capitals)

for country in countrie_and_capitals.keys():
    print(country)

for capitals in countrie_and_capitals.values():
    print(capitals)

for country, capital in countrie_and_capitals.items():
    print(country + "-" + capital)

print(countrie_and_capitals["Poland"])      #jesli nie ma to błąd
print(countrie_and_capitals.get("Poland"))    #jesli nie ma to none

print(countrie_and_capitals.setdefault("USA", "Washington DC"))
print(countrie_and_capitals)

print(countrie_and_capitals.pop("USA", "Washington DC"))
print(countrie_and_capitals)

print(countrie_and_capitals.popitem())
print(countrie_and_capitals)

if "Poland" in countrie_and_capitals.keys():
    print("Zanleziono")
else:
    print("Nie zanleziono")

print("USA" in countrie_and_capitals)

countrie_and_capitals.clear()
print(countrie_and_capitals)
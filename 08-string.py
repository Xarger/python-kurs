name = "kamil"
nam = "GREG"

print(len(name))

print(name.capitalize())
print(name.upper())
print(nam.lower())

name = "Lamil"
print(name[0])

print(name[3:])
print(name[-3:])

channel = "Jak nauczyć sie programowania"
print(channel.split(" "))

join_string = "<=>"
print(join_string.join(channel.split(" ")))

print(name.startswith("K"))
print(name.startswith("L"))

print(name.endswith("l"))
print(name.endswith("L"))

print(name.rstrip("l"))
print(name.lstrip("L"))

name = "aKAmila"
print(name.strip("a"))

name = " aKAm ila    "
print(name.strip())

first_name = "Kamil"
last_name = "Brzezisnki"

print(first_name + " " + last_name)

join_string = " "
print(join_string.join([first_name, last_name]))

james_bond = 7
print(str(james_bond).zfill(3))
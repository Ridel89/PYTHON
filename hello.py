print("Hello world")

#var---------------------------------------------
first_var = "value of first var"
print(first_var)

secondVar = 'second var'
print(secondVar)

name = 'ada lovelace'
print('title method: ' + name.title())
print( name.upper())
print( name.lower())

first_name = 'Victor'
second_name = 'Kravchuk'
full = f'{first_name} {second_name}'
print(full)

#String-------------------------------------------
print("Languages: \nPython\nJs\n\tC++")

fav_language = ' python '
print('~'+fav_language.rstrip()+'~')
print('~'+fav_language.lstrip()+'~')
print('~'+fav_language.strip()+'~')

#number-------------------------------------------
print(2+3, 3-2, 2*3, 3/2, 3**2, 2**8, 10**6, (2+3) * 4)
print(0.1 + 0.1, 3*0.1)
print(14_000_000_000)
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
x, y, z = 0, 0, 0
print(x, y, z)

#array---------------------------------------------
bicekl = ['trek', 'specialized', 'canondale']
print(bicekl)
print(bicekl[1])
print(bicekl[1].title())
print(bicekl[-1])
print(bicekl[-3])

moto = ['honda', 'yamaha', 'suzuki']
print(moto)
moto[0] = 'Ducati'
print(moto)
moto.append('ferari')
print(moto)

moto.insert(0, 'honda')
print(moto)
moto.insert(3, 'jaguar')
print(moto)

del moto[0]
print(moto)
last_app = moto.pop()
print(last_app)
print(moto)

sec_moto = moto.pop(2)
print(sec_moto)
print(moto)
moto.remove('Ducati')
print(moto)


cars = ['bmv', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmv', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

cars.reverse()
print(cars)
print(f'lenght of cars = {len(cars)}' )

#loops---------------------------------------------
musicians = ['Jeff', 'Kurt', 'Jon', 'Hadges']

for musician in musicians:
	print(musician)

for musician in musicians:
	print('------')
	print(musician)
	print('------')
print('They are great musicians')
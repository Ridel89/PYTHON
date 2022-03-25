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

#loops--------------------------------------------------------
musicians = ['Jeff', 'Kurt', 'Jon', 'Hadges']

for musician in musicians:
	print(musician)

for musician in musicians:
	print('------')
	print(musician)
	print('------')
print('They are great musicians')

for value in range(1, 5):
	print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2)) #third prams is step
print(even_numbers)

squares = []
for value in range(1, 11):
	square = value ** 2 #value^2
	squares.append(square)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'mark', 'florende', 'eli']
print(players)
#slices:
print(players[0:3]) 
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
	print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #create copy of array

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

#TUPLE (CORTAGE) aka CONST-------------------------------------------------
dim = (200, 50)
print(dim)
print(dim[0])
print(dim[1])

for d in dim:
	print(d)

dim = (23, 78)
print(dim)

#CONDITIONS-------------------------------------------------
cars = ['audi' 'bmw', 'Subaru', 'toyta']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
#dictionaries-----------------------------------------------------

#input------------------------------------------------------------
message = input('Tell me something: ')
print('Thank you! You said: ')
print(message)

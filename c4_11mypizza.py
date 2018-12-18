pizzas = ["jirou","niurou","huotui"]
friend_pizzas = pizzas[:]

#1
pizzas.append("mix")

#2
friend_pizzas.append("sanmingzhi")

#3
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\n")

print("my friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

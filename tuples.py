#Tuples in python
# Conventionallu tuples look like this

Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)

Lists_of_fruits = ["Apples", 4, "Bananas", 5, "Oranges", 6]

# print(type(Fruit))
# print(type(Lists_of_fruits))
# We can modify elements within a list
# Lists_of_fruits[0] = "Strawberries"
#
# print(Lists_of_fruits)

#We cannot modify elements within a tuple!
# Fruit [0]= "Strawberries"
#
# print(Fruit)

# #Concatenation of tuples
# Fruit = Fruit[0:4] + ("Cherries", 10)
# print(Fruit)

# creating a tuple
another_tuple = tuple(("Hello", 18, True))

print(type(another_tuple))

#Converting atuple to a list and then back to a tuple1
Fruit = list(Fruit)
Fruit.append("Pears")

print(Fruit)

#Unpacking tuples
Fruit = ("Apples", "Pears", "Bananas", "Strawberries")
(one, two, three, four) = Fruit
print(one)
print(two)
print(three)

#Incorporating loops within tuples
for i in range(len(Fruit)):
    print(Fruit[i])
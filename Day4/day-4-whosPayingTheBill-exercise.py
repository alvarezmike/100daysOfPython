from random import randrange
# Split string method

print("Notice there must be a space between the comma and the next name.\n")
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(names)

random_index = randrange(len(names))
print(names[random_index] + " is going to buy the meal today!")
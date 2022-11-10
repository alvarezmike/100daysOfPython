# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25\n")
print("Pepperoni for small pizza: +$2")
print("Pepperoni for medium or large pizza: +$3\n")
print("Extra cheese for any size pizza: +$1\n")

size = input("What size pizza do you want? S, M, or L?  ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
small = 15
medium = 20
large = 25

if size == "L":
    if (add_pepperoni == "Y"):
        large += 3

    if (extra_cheese == "Y"):
        large += 1
        print(f"Your total bill is ${large}")
    else:
        print(f"Your total bill is ${large}")

if size == "M":
    if (add_pepperoni == "Y"):
        medium += 3

    if (extra_cheese == "Y"):
        medium += 1
        print(f"Your total bill is ${medium}")
    else:
        print(f"Your total bill is ${medium}")

if size == "S":
    if (add_pepperoni == "Y"):
        small += 2

    if (extra_cheese == "Y"):
        small += 1
        print(f"Your total bill is ${small}")
    else:
        print(f"Your total bill is ${small}")

print("""
// ""--.._
||  (_)  _ "-._
||    _ (_)    '-.
||   (_)   __..-'
 \\__..--""

""")







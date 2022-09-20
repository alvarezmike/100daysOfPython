print("Welcome to the rollercoaster!")
# input height
height = int(input("What is your height in cm? "))
# declare bill variable
bill = 0

# condition to ride the rollercoaster
if height >= 125:
    print("You can ride the rollercoaster")
    # input age
    age = (int(input("What is your age? ")))

    # tickets price based on age
    if age >= 18 and age < 45:
        bill = 15
    elif age < 18:
        bill = 7
    elif age > 45 and age < 55:
        bill = 0
    # ask user if he wants a photo
    # condition for price if photo is added.
    want_photo = input("Do you want a photo taken? Y or N : ")
    if want_photo == "Y":
        bill += 3
        print(f"Your ticket is {bill}")
    elif want_photo == "N":
        print(f"Your ticket is {bill}")


else:
    print("Sorry, you have to be taller to ride the rollercoaster")

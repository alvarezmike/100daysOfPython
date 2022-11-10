# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# control flow to verify if the year given is leap or not.

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")

else:
    print("Not leap year.")



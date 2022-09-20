# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# converting age to int
age = int(age)
daysYear = 365 * (90 - age)
days = 90 - age
# weeks in a year
weeks = 52 * days
# months in a year
months = 12 * days

# Analyze when you will become 90 years old based on your current age.
print(f"You have {daysYear} days, {weeks} weeks, and {months} months left to be 90 years old.")
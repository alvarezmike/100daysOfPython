# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# converting int height and float weight.
# formula to get bmi
bmi = (weight)/(height) ** 2
# converting bmi to int
bmi_as_int = int(bmi)
#  show result bmi
print(f"Your body max index: {bmi_as_int}" )

# print body max index category logic/ if/elif
if bmi_as_int <= 18  :
    print("You are underweight.")

elif bmi_as_int >= 18.5 and bmi_as_int < 25:
     print("You have a normal weight.")

elif bmi_as_int >= 25 and bmi_as_int <30:
    print("You are slightly overweight.")

elif bmi_as_int >= 30 and bmi_as_int < 35:
     print("You are obese.")

elif bmi_as_int >= 35 :
    print("You are clinically obese.")



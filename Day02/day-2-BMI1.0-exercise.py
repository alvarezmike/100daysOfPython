
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


#converting int height and float weight.
#formula to get bmi
bmi = int(weight)/float(height) ** 2
#converting bmi to int
bmi_as_int = int(bmi)
#show result bmi
print(bmi_as_int)




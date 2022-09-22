"""
You are going to use dictionary comprehension to create a dictionary called
result that takes each word in the given sentence and calculates the number of letters in each word.

"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sp = sentence.split()
print(sp)

result = {s: len(s) for s in sp}
print(result)

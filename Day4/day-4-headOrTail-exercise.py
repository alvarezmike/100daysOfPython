# Write your code below this line 👇
#  Hint: Remember to import the random module first. 🎲
import random

head_or_tail = random.randint(0, 1)
print("Flipped coind landed..")

if head_or_tail == 0:
    print("Heads")

else:
    print("Tails")

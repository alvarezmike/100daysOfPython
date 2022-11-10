rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# player select rock, paper or scissors
player_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")


# show ascii art based on user selection.
if player_choose == '0':
    print(rock)
elif player_choose == '1':
    print(paper)
elif player_choose == '2':
    print(scissors)
else:
    print("Wrong input. Accepted inputs are 0, 1 or 2")


# computer random selection rock , paper or scissors.
import random
computer_choose = random.randint(0,2)
print("Computer choose:\n")

# conditional to determine who wins the game. Player or the computer
if computer_choose == 0:
    print(paper)
elif computer_choose == 1:
    print(rock)
elif computer_choose == 2:
    print(scissors)
else:
    print("Something went wrong")

if player_choose == '0' and computer_choose == 0:
    print("You lose")
elif player_choose == '0' and computer_choose == 2:
    print("You win")
elif player_choose == '0' and computer_choose == 1:
    print("Draw")

if player_choose == '1' and computer_choose == 0:
    print("Draw")
elif player_choose == '1' and computer_choose == 2:
    print("You lose")
elif player_choose == '1' and computer_choose == 1:
    print("You win")

if player_choose == '2' and computer_choose == 0:
    print("You win")
elif player_choose == '2' and computer_choose == 2:
    print("Draw")
elif player_choose == '2' and computer_choose == 1:
    print("You lose")

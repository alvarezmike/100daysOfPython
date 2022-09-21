from art import logo
from random import randint
print(logo)

should_continue = True
should_continue_hard = True
# guess number answer
# choose a number between 1,24
number_to_guess = randint(1,24)
print(number_to_guess) # testing random guess.
# attempt available in easy mode.
attempts_easy = int(5)
# attempts available in hard
attempts_hard = int(3)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 24")
difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")

# easy mode
while should_continue:
  if difficulty == 'easy':
    print(f"You have {attempts_easy}  attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
      print(f"You got it! The answer was {number_to_guess}")
      should_continue = False
    elif guess != number_to_guess:
      print("Wrong number")
      attempts_easy = attempts_easy -1
      should_continue
      if attempts_easy == 0:
        should_continue = False
        print("You lost.")
 # hard mode
  elif difficulty == 'hard':
    print(f"You have {attempts_hard}  attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
      print(f"You got it! The answer was {number_to_guess}")
      should_continue = False
    elif guess != number_to_guess:
      print("Wrong number")
      attempts_hard = attempts_hard -1
      should_continue
      if attempts_hard == 0:
        should_continue = False
        print("You lost.")

# add to high or too low functionality later.
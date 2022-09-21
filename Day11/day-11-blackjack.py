############### Blackjack Project #####################
import random

from art import logo

print(logo)


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# function that generates the user first two cards.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.sample(cards, 2)


# function that generates the first computer card
def computer_deal_card():
    cards_c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.sample(cards_c, 1)


# variables containing random generated card values.
user_cards = deal_card()
computer_cards = computer_deal_card()

print(f"Your cards are: {user_cards}, current score is ")

print(f"Computer's first card is: {computer_cards}")
# decide if user wants to get another card
get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
# if yes
if get_another_card == 'y':

    user_cards.append(deal_card().pop(1))
    print(f"Your final hand is {user_cards}, total score is: {sum(user_cards)}")
    # code before good
    computer_cards.append(computer_deal_card().pop(0))
    print(f"Computer's final hand is {computer_cards}, total score is: {sum(computer_cards)}")

    # saving sum into new variables
    result_user = sum(user_cards)
    result_computer = sum(computer_cards)

    # decide who won
    if result_user > result_computer and result_user <= 21:
        print("You won.")

    elif result_user > 21:
        print("You lost")

    elif result_computer > result_user and result_computer <= 21:
        print("Computer won.")

    elif result_computer > 21:
        print("Computer lost.")

    elif result_computer == result_user:
        print("It's a draw.")

# if not
if get_another_card == 'n':

    print(f"Your final hand is {user_cards}, total score is: {sum(user_cards)}")
    computer_cards.append(computer_deal_card().pop(0))
    print(f"Computer's final hand is {computer_cards}, total score is: {sum(computer_cards)}")

    # saving sum into new variables
    result_user = sum(user_cards)
    result_computer = sum(computer_cards)

    # decide who won
    if result_user > result_computer and result_user <= 21:
        print("You won.")

    elif result_user > 21:
        print("You lost")

    elif result_computer > result_user and result_computer <= 21:
        print("Computer won.")

    elif result_computer > 21:
        print("Computer lost.")

    elif result_computer == result_user:
        print("It's a draw.")

from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)


# function to find the highest bid in the dictionary.
def find_highest_bid(findbidder):
    winner = max(findbidder, key=findbidder.get)
    highest_bid = findbidder[winner]
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# creating empty dictionary
bid_collection = {}
running = True

# loop while there are active bidders
while running:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    # adding key and values to dictionary
    bid_collection[name] = bid

    question = input("Are there more bidders. Type 'yes' or 'no'.")

    if question == 'yes':
        clear()
        print()

        # if no more bidders, show the winner.
    elif question == 'no':
        clear()
        find_highest_bid(bid_collection)
        running = False

import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

def get_current_datetime():
    """Print motivational quote from quotes.txt if it is Wednesday"""
    # Monday 0, Tuesday 1, Wednesday 2 and so on..
    if weekday == 0:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

            print(quote)

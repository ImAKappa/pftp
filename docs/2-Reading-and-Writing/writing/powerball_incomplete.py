"""powerball.py

Simulates net profit from playing the powerball lottery many, many times
"""
import random

winning_draw = set(random.choices(range(1, 70), k=5))
powerball = random.choice(range(1, 27))

tickets = 0
earnings = 0

NUM_DRAWS = 2_000_000

print("Notable winnings".center(30, "="))
for draw in range(NUM_DRAWS):
    tickets += 1
    my_draw = set(random.choices(range(1, 70), k=5))
    my_powerball = random.choice(range(1, 27))
    # matching_nums is the total count of matching numbers
    matching_nums = len(my_draw.intersection(winning_draw))
    i_have_powerball = my_powerball == powerball
    
    # Code goes here...

print()
print("Summary".center(20, "="))
TICKET_COST = 2
# Don't forget to complete this!
spent = ???
print(f"I just spent ${spent:,.2f} on lottery tickets :0")
print(f"I earned ${earnings:,.2f}")
print(f"My net profit is ${earnings - spent:,.2f} :')")
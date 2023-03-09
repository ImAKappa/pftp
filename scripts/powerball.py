"""powerball.py

Simulates net profit from playing the powerball lottery many, many times
"""
import random

winning_draw = set(random.choices(range(1, 70), k=5))
powerball = random.choice(range(1, 27))

tickets = 0
earnings = 0

# This script is inefficient; it takes around 12s to run 5,000,000 iterations
NUM_DRAWS = 5_000_000

print("Notable winnings".center(30, "="))
for draw in range(NUM_DRAWS):
    tickets += 1
    my_draw = set(random.choices(range(1, 70), k=5))
    my_powerball = random.choice(range(1, 27))
    matching_nums = len(my_draw.intersection(winning_draw))
    i_have_powerball = my_powerball == powerball
    
    if matching_nums == 5:
        if i_have_powerball:
            print("OHMYGAH I WON!")
            earnings += 60_000_000
        else:
            print("It's just a small loan of a million dollars")
            earnings += 1_000_000
    elif matching_nums == 4 and i_have_powerball:
        print("Cool 50k :)")
        earnings += 50_000
    elif matching_nums == 4 or (matching_nums == 3 and i_have_powerball):
            earnings += 100
    elif matching_nums == 3 or (matching_nums == 2 and i_have_powerball):
        earnings += 7
    elif i_have_powerball or (matching_nums == 1 and i_have_powerball):
        earnings += 4
    else:
        continue

print()
print("Summary".center(20, "="))
TICKET_COST = 2
spent = TICKET_COST * tickets
print(f"I just spent ${spent:,.2f} on lottery tickets :0")
print(f"I earned ${earnings:,.2f}")
print(f"My net profit is ${earnings - spent:,.2f} :')")
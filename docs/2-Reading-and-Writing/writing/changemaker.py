"""changemaker

Prompt the user to enter an amount of dollars and cents. For example $1.18.
Display the number of quarters, dimes, nickels, and pennies to make that amount,
making sure to maximize the amount of higher-value coins.

Examples: 

- If the user entered $1.18 it should output: 4 quarters, 1 dimes, 1 nickels, 3 pennies
- If the user entered $1.02 it should output: 4 quarters, 0 dimes, 0 nickels, 2 pennies
"""
from typing import NamedTuple
from enum import Enum

class Coin(NamedTuple):
    name: str
    value: float

class Change(Enum):
    QUARTER = Coin("Quarter", 0.25)
    DIME = Coin("Dime", 0.10)
    NICKEL = Coin("Nickel", 0.05)
    PENNY = Coin("Penny", 0.01)

def make_change(dollar_amount: float) -> dict[str, int]:
    """Counts change from `dollar_amount`"""
    dollar_amount = round(dollar_amount, ndigits=2)
    change_count = dict()
    for change in Change:
        coin: Coin = change.value
        change_count[coin.name] = int(dollar_amount / coin.value)
        dollar_amount -= change_count[coin.name] * coin.value
        dollar_amount = round(dollar_amount, ndigits=2)
    return change_count

if __name__ == "__main__":
    dollar_amounts = [1.18, 1.02, 22.16, 16299182456.22]
    for dollar_amount in dollar_amounts:
        change_count = make_change(dollar_amount)

        print(f"To make change from ${dollar_amount:,.2f}, we could use:")
        for coin, amount in change_count.items():
            print(f"\t{amount:,} {coin}{'s' if amount != 1 else ''}")
        print()

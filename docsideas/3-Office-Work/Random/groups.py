"""groups

Module for randomly sorting things into groups
"""
import random

people = [
    "Robert Walker",
    "Cassandra Walters",
    "Benjamin Hodges",
    "Susan Hammond",
    "Michele Jones",
    "Michelle Stone",
    "Diane Walker",
    "Mr. Troy Woodard",
    "Emma Hartman",
    "Joshua Smith",
    "Sharon Parker",
    "David Reynolds",
    "Donald Mullins",
    "Jacob Blair",
    "Richard George",
    "Scott Meyer",
    "James Banks",
    "Richard Porter",
    "Christopher Ramos",
    "William Martinez",
]

if __name__ == "__main__":
    # Shuffle a few times
    shuffle_amount = 4
    for _ in range(shuffle_amount):
        random.shuffle(people)

    # Create groups
    group_size = 2
    for group_number, i in enumerate(range(0, len(people), group_size)):
        print(f"Group {group_number+1}".center(20, "="))
        group = people[i:i+group_size]
        print("\n".join(group))
        print()
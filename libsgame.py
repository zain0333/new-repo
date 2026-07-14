# Mad Libs Game

print("=== Welcome to the Mad Libs Game! ===")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
verb = input("Enter a verb (ending in -ing): ")
adjective = input("Enter an adjective: ")

print("\n--- Your Story ---\n")

story = f"""
One day, {name} went to {place}.
There, {name} saw a {adjective} {animal}.
The {animal} was {verb} while eating {food}.
Everyone laughed, and {name} had the best day ever!
"""

print(story)
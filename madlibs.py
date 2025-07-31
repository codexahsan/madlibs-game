import random

print("\n Welcome to the Madlibs Game! \n")

# Get user inputs (with strip and small prompt help)
adjective = input("Enter an adjective (e.g. funny, scary): ").strip()
action = input("Enter an action verb (e.g. jump, run): ").strip()
thing = input("Enter an object (e.g. shoe, pizza): ").strip()
animal = input("Enter an animal (e.g. cat, lion): ").strip()
name = input("Enter a name: ").strip().capitalize()
verb_ing = input("Enter a verb ending in -ing (e.g. laughing, dancing): ").strip()
name2 = input("Enter another name: ").strip().capitalize()

# Define madlib story templates with placeholders
madlib1 = f"It was a day of mourning as friends and family gathered to say goodbye to {name}. But the somber atmosphere was shattered when a {adjective} {animal} burst into the chapel and {action}ed right on the casket. The shocked silence was broken by {name2}'s uncontrollable {verb_ing} as they threw a {thing} at the {animal}, setting off a chain reaction of laughter that turned the funeral into an unforgettable event."

madlib2 = f"{name} and {name2}'s wedding was a beautiful affair, with every detail meticulously planned. However, no one could have predicted that the {adjective} {animal} chosen as the ring bearer would decide to {action} the {thing} instead of walking down the aisle. As the creature continued its antics, the guests' initial gasps turned to {verb_ing}, making it a wedding to remember for all the wrong reasons."

madlib3 = f"The highlight of {name}'s birthday party was supposed to be the {animal} show, but things took a turn when the {adjective} {animal} broke free from its handler and {action}ed through the crowd. Children and adults alike found themselves {verb_ing} as they dodged the rampaging beast, while {name2} tried to calm it down with a {thing}, turning the celebration into a chaotic adventure."

madlib4 = f"As {name} stepped up to receive their diploma, a {adjective} {animal} swooped down from the rafters and {action}ed on their head. {name2} in the audience immediately started {verb_ing}, throwing a {thing} onto the stage. The incident became the talk of the town."

madlib5 = f"At {name}'s retirement party, the mood was festive until a {adjective} {animal} from the petting zoo escaped and began {action}ing the buffet table. Guests scattered in every direction, {verb_ing} as they went, while {name2} tried to stop it with a {thing}, turning the event into a legendary tale."

# Put all madlibs in a list
madlib_list = [madlib1, madlib2, madlib3, madlib4, madlib5]

# Pick one randomly
madlib = random.choice(madlib_list)

# Print the final story
print("\n" + "-"*60)
print("Here's your Madlib:\n")
print(madlib)
print("\n" + "-"*60)

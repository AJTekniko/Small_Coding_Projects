direction1 = input("""Welcome to Treasure Island!
Your mission is to find the treasure.
You're at a cross road. Where do you
want to go? Type 'left' or 'right'""")

#Results and new conditional statements
if direction1.lower() == "left":
    direction2 = input("""You've come to a lake. There is an
island in the middle of the lake.
What would you like to do? Type 'swim
towards it' or 'leave'""")
    if direction2.lower() == "swim towards it":
        print("""We regret to inform you that hostile
people found you and you're dead 💀""")
    elif direction2.lower() == "leave":
        print("""You left the area but the temperature
dropped and you froze to death 💀""")
    else:
        print("""Please type a valid direction.
Game over.""")
elif direction1.lower() == "right":
    direction2 = input("""You've encountered a swarm of bees!
Which direction will you run? Type
'left' or 'right'""")
    if direction2.lower() == "left":
        print("""We regret to inform you that you were
stung to death 💀""")
    elif direction2.lower() == "right":
        direction3 = input("""After running for some time, you trip
on something on the ground. What will
you do? Type 'continue' or 'investigate'""")
        if direction3.lower() == "continue":
            print("""You overexerted yourself. We regret
to inform you that you are dead 💀""")
        elif direction3.lower() == "investigate":
            print("""Congratulations! You found the
treasure!!! 💰""")
        else:
            print("""Please type a valid direction.
Game over.""")
    else:
        print("""Please type a valid direction.
Game over.""")
else:
    print("""Please type a valid direction.
Game over.""")
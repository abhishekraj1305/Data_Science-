import random

'''
1 for snake
-1 for water
0 for gun
'''

# Computer chooses randomly from the three choices
computer = random.choice([1, -1, 0])

youstr = input("Enter 1 for snake, -1 for water, 0 for gun: ")

# Allow both number-style input and short letters
youDict = {
    "1": 1,
    "-1": -1,
    "0": 0,
    "s": 1,   # snake
    "w": -1,  # water
    "g": 0    # gun
}

reversedict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

# Validate user input
if youstr not in youDict:
    print("Invalid input! Please enter 1, -1, or 0 (or s, w, g).")
else:

    you = youDict[youstr]

    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")
    
    # if ((computer - you)==-1) or (computer - you)==2:
    #     print("You win!")
    # elif computer == you:
    #     print("It's a draw!")
    # else:
    #     print("You lose!")

    # Same choice → Draw
    if computer == you:
        print("It's a draw!")

    else:
        # Snake vs Water vs Gun scenarios
        if computer == -1 and you == 1:
            # Computer: water, You: snake → snake drinks water
            print("You win! (snake drinks water)")
        elif computer == -1 and you == 0:
            # Computer: water, You: gun → water sinks gun
            print("You lose! (water sinks gun)")
        elif computer == 1 and you == -1:
            # Computer: snake, You: water → snake drinks water
            print("You lose! (snake drinks water)")
        elif computer == 1 and you == 0:
            # Computer: snake, You: gun → gun shoots snake
            print("You win! (gun shoots snake)")
        elif computer == 0 and you == 1:
            # Computer: gun, You: snake → gun shoots snake
            print("You lose! (gun shoots snake)")
        elif computer == 0 and you == -1:
            # Computer: gun, You: water → water sinks gun
            print("You win! (water sinks gun)")
        else:
            # This should *never* occur structurally
            print("Unexpected case encountered!")
            
            

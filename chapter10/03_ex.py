#WRP game fxn in a program lets user play a game and return the score as a integer you need to read file hi-score.txt to get the current high score and update it if the user score is higher than the current high score


import random

def play_game():
    print("Welcome to the game!")
    score = random.randint(0, 100)
    #fetching high score from file
    with open(r"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\highscore.txt") as f:
        high_score = f.read()
        if(high_score!=""):
            high_score = int(high_score)
        else:
            high_score = 0
        
    print(f"Your score is: {score}")
    
    if score > high_score:
        with open(r"C:\Users\LENOVO\.cursor\python_oneshot\chapter10\highscore.txt", "w") as f:
            f.write(str(score))
        print(f"Congratulations! You have the new high score!,your previous Score Was {high_score} and now your new high score is {score}")
    
    return score

play_game()
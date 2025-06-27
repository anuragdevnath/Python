import random

def game():
    score = random.randint(1, 100)
    print(f"Your score is {score}")
    # get highscore from hiscore.txt
    with open("Chapter 9 - File/highscore.txt", "r") as f:
        highscore = f.read()
        if(highscore == ""):    
            highscore = 0
        if(score > int(highscore)):
            print("You have broken the highscore!")
            with open("Chapter 9 - File/highscore.txt", "w") as f:
                f.write(str(score))
        else:
            print("You have not broken the highscore!")

game()
import random

def guess(randomNum):
    numGuess = 0
    userNum = None
    while randomNum != userNum:
        userNum = int(input("Guess the number: "))
        if randomNum > userNum:
            print("You guessed it wrong! Enter a Higher Number Please!!")
            numGuess += 1
        elif randomNum < userNum:
            print("You guessed it wrong! Enter a Lower Number Please!!")
            numGuess += 1

    print(
        f"Yes!! you have got the right number in {numGuess} guesses and the number was {randomNum}")
    try:
        with open("Highscore.txt", 'r') as f:
            highScore = int(f.read())
        if numGuess < highScore:
            with open("Highscore.txt", 'w') as f:
                f.write(str(numGuess))
            print("\nCongratulation! You have broken the high score!!")
    except:
        print("Good Game!")

if __name__ == "__main__":
    print(
        "**********Welcome to the Game of Guesses**********\n[Here computer will genrate a number and you have to guess a number]\n(Press Enter to Start)")
    start = str(input())
    if start == "":
        lvl = input(
            "Select the level of the game, Type 'H' for Hard and 'E' for easy: ")
        if lvl.lower() == 'e':
            a = int(
                input("Enter the number you want the computer to genrate number below: "))
            #randomNum = random.randint(0, a)
            guess(random.randint(0, a))
        elif lvl.lower() == 'h':
            #randomNum = random.randint(0, 100)
            guess(random.randint(0, 100))
    else:
        print("Thank you!")

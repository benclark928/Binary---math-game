from gameclasses import Games
from gameclasses import BinaryGame
from gameclasses import MathGame

from gametasks import getUserScore
from gametasks import updateUserScore
from gametasks import printInstructions

try: 
    mathInstructions = "In this game, you will be given a simple arithmetic question. Each correct answer gives you one mark. No mark is deducted for wrong answers."
    binaryInstructions = "In this game, you will be given a number in base 10. Your task is to convert this number to base 2. Each correct answer gives you one mark. No mark is deducted for wrong answers."

    bg = BinaryGame()
    mg = MathGame()

    userName = input("Please enter your username: ")
    score = getUserScore(userName)
    
    newUser = False
    
    if score == -1:  
        newUser = True
        score = 0 

    print("Welcome %s, your score is %d "% (userName, score))

    userChoice = 0 

    while userChoice != "-1": 
        game = input("MathGame(1) or BinaryGame(2)? ")
        while game != "1" and game != "2":
            game = input("Enter either 1 for MathGame or 2 for BinaryGame: ")
        
        numPrompt = input("How many questions do you want per game (1-10)? ")
        
        while (True): 
            try: 
                num = int(numPrompt)
                break
            except: 
                print("The answer given wasn't an integer")
                numPrompt = input("Enter another answer: ")
        
        if game == "1": 
            mg.noOfQuestions = num
            printInstructions(mathInstructions)
            score += mg.generateQuestions()
        else: 
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score += bg.generateQuestions()
        
        print(score)

        userChoice = input("Press Enter to continue or -1 to exit: ")

    updateUserScore(newUser, userName, score)

except Exception as e:
    print(e)
    print("System Generated Error")
    print("An unknown error has occurred")
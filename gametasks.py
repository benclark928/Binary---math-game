from os import remove
from os import rename

#prints the instructions
def printInstructions(instructions):
    print(instructions)

#opens the txt file, if the file doesn't exist makes a new one in w mode 
#reads through the lines splitting them at a , 
#checks if the newUsername == the username in the file and if so returns the value 
def getUserScore(userName):
    try:
        inputf = open('userScore.txt','r')
        print("File found")
    except IOError:
        inputf = open('userScore.txt','w')
        print("File not found")
        inputf.close()
        return "-1"
    
    lines = inputf.readlines()
    
    for line in lines:
        content = line.split(',')
        if(len(content) < 2):
            continue
        
        lineUserName = content[0]
        lineScore = int(content[1].strip())
        
        if (userName == lineUserName):
            inputf.close()
            return lineScore
    
    inputf.close()        
    return -1

#if the newUser is new then write in their name and score into the file
#if not re-write the name and the new score 
#rename/ replace the tmp file with the txt file as it has all the useful info
def updateUserScore(newUser, userName, score):
    if (newUser == True):
        inputf = open('userScore.txt','a')
        inputf.write("\n%s, %d"%(userName, score))
        inputf.close()
    else:
        newFile = open('userScore.tmp', 'w')
        inputf = open('userScore.txt','r')

        lines = inputf.readlines()
        
        for line in lines:
            content = line.split(',')
            lineUserName = content[0]
            lineScore = content[1]

            if (lineUserName == userName):
                newFile.write("%s, %d\n"%(userName, score))
            else:
                newFile.write(line)

        newFile.close()
        inputf.close()
        
        remove('userScore.txt')
        rename('userScore.tmp', 'userScore.txt')
class Games:
    #sets noOfQuestions to an instance variable and to 0
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions 

    #gets the value of noOfQuestions
    @property
    def noOfQuestions(self): 
        return self._noOfQuestions

    #checks the value of noOfQuestions to these conditions 
    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("Minimum Number of Questios = 1")
            print("Hence, number of questions will be set to 1")
        elif value > 10:
            self._noOfQuestions = 10 
            print("Maximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else: 
            self._noOfQuestions = value 

class BinaryGame(Games): 
    #imports the randint function 
    #does a for loop and asks the user to convert a number to binary 
    #evaluates the answer in a while true loop, uses try and except for a non- bianry number
    # returns the score
    def generateQuestions(self): 
        from random import randint
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1,100)
            userResult = input("Convert the number %d into binary: "%(base10))
            while(True):
                try: 
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        print("The answer is correct") 
                        score += 1
                    else: 
                        print("Wrong answer. The correct answer is %d."% (base10))
                    
                    break
                except:   
                    print("Please enter a valid binary number: ")
                    userResult = input("Please enter another answer: ")
        
        return score

class MathGame(Games):
    def generateQuestions(self): 
        #import randint
        from random import randint

        # declare variables and 4 called score
        score = 0
        numberList = [0,0,0,0,0]
        symbolList = ['','','','']
        operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}

        #using a for loop to generate questions
        for i in range(self.noOfQuestions):
            for j in range(len(numberList)): 
                numberList[j] = randint(1,9)

            # print(numberList)
            
            for j in range(len(symbolList)):
                if(j > 0 and symbolList[j-1] == '**'):
                    symbolList[j] = operatorDict[randint(1,3)]
                else:
                    symbolList[j] = operatorDict[randint(1,4)]
                
            # print(symbolList)

            questionString = ''

            for j in range(0,4):
                questionString = questionString + str(numberList[j])
                questionString = questionString + symbolList[j]
            
            questionString = questionString + str(numberList[4])
            
            # print(questionString)
            result = eval(questionString)
            questionString = questionString.replace("**", "^")
            
            userInp = input("Please try this question: %s\n"%(questionString))

            while(True):
                try: 
                    answer = int(userInp)
        
                    if answer == result:
                        print("The answer is correct") 
                        score += 1
                    else: 
                        print("Wrong answer, the answer is %f"% (result))
                    break
                except:   
                    print("Please enter a valid number")
                    userInp = input("Please enter another answer:\n")

        return score
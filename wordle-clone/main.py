from random import randint
def readAnswersFromFile():
    # Read all answers from File, select answer to use.
    with open('answers_alphabetical.txt','r') as file:
        allAnswers = file.readlines()
        answerCount = len(allAnswers)
        chosenAnswer = allAnswers[randint(0,answerCount-1)]
    return chosenAnswer

readAnswersFromFile()
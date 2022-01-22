# randint to select word from wordlist
from random import randint
class Game():
    def __init__(self):
        self.legalAnswers = readLegalAnswersFromFile()
        self.answer = readAnswersFromFile()
        self.guessCount = 1
    
    def gameLoop(self):
        while self.guessCount <= 6:
            guess = input(f"Guess #{self.guessCount}>")
            if self.evaluateLegal(guess):
                print("Legal Guess")
            else: print("Illegal")
            self.guessCount+=1
    
    def evaluateLegal(self,guess):
        if guess.lower() in self.legalAnswers:
            return True
        return False
        
def readLegalAnswersFromFile():
    with open('allowed_guesses.txt', 'r') as file:
        allowedAnswers = file.readlines()
    return allowedAnswers

def readAnswersFromFile():
    # Read all answers from File, select answer to use.  Return chosen Answer
    with open('answers_alphabetical.txt','r') as file:
        allAnswers = file.readlines()
        answerCount = len(allAnswers)
        chosenAnswer = allAnswers[randint(0,answerCount-1)]
    return chosenAnswer

NewGame = Game();
NewGame.gameLoop();
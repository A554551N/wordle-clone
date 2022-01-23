# randint to select word from wordlist
from random import randint
class Game():
    def __init__(self):
        self.legalAnswers = readLegalAnswersFromFile()
        self.answer = selectAnswerFromFile()
        self.guessCount = 1
        self.usedGuesses = []
        self.usedLetters = set()

    def gameLoop(self):
        while self.guessCount <= 6:
            guess = input(f"Guess #{self.guessCount}>").lower().rstrip()
            if self.evaluateLegal(guess):
                if guess == self.answer:
                    print(f"You Win!  It took {self.guessCount} guesses.")
                    break
                else:
                    self.usedGuesses.append(guess)
                    for letter in guess:
                        self.usedLetters.add(letter)
                    print(self.updatePrompt(guess))
                    print(f"You have tried these letters: {self.usedLetters}")
            else:
                print("Entry not valid or already used")
                continue
            self.guessCount+=1
    
    def evaluateLegal(self,guess):
        if guess in self.legalAnswers and guess not in self.usedGuesses:
            return True
        return False
    
    def updatePrompt(self,guess):
        promptOut = ""
        for i in range(5):
            if guess[i] == self.answer[i]:
                promptOut+= "!"
            elif guess[i] in self.answer:
                promptOut+= "?"
            else: promptOut+= "_"
        return promptOut

        
def readLegalAnswersFromFile():
    with open('allowed_guesses.txt', 'r') as file:
        allowedList = [line.rstrip() for line in file]
    with open('answers_alphabetical.txt','r') as file:
        allAnswers = [line.rstrip() for line in file]
    return allowedList + allAnswers

def selectAnswerFromFile():
    # Read all answers from File, select answer to use.  Return chosen Answer
    with open('answers_alphabetical.txt','r') as file:
        allAnswers = [line.rstrip() for line in file]
        answerCount = len(allAnswers)
        chosenAnswer = allAnswers[randint(0,answerCount-1)]
    return chosenAnswer

NewGame = Game();
intro = """The WORD has five letters.  When you enter a word, you will receive
the following:
_ The letter does not appear in the WORD.
? The letter appears in the WORD but is not in the correct position.
! The letter appears in the WORD and is in the correct position.

You have 6 attempts to correctly guess the WORD."""
print(intro)
NewGame.gameLoop();
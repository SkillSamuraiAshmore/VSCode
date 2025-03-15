from MAINX3 import LetterState

class Wordle:
    
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass
    
   
    
    def attempt(self, word: str):
        self.attempts.append(word)
        
    def guess(self, word: str):
        result = []
        
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = MAINX3(charcter)
            letter.is_in_word =  character in self.secret
            letter.is_in_posiiton = charcter == self.secret
            
        return []

    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
        pass
    
    def can_attempt(self):
        return self.remaining_attempts == 0 and not self.is_solved
    
    
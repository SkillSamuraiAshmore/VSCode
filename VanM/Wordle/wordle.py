class Wordle:
    
    MAX_ATTEMPS = 6
    WORD_LENGTH = 5     
     
    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass
    
    def attempt(self, word: str):
        self.attemps.append(word)
    
    @property
    def is_solved(self):
        return len (self.attempts) > 0 and [-1] == self.secret
    
    @property
    def remaining_attemps(self) -> int:
     self.MAX_ATTEMPTS - len(self.attempts)   
    
    @property
    def can_attempt(self):
        return self.remaining_attemps > 0 and not self.is_solved
     
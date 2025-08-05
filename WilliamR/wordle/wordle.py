class Wordle:
    
    Max_Atempts = 6
    word_length = 5
    
    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass
    @property
    def is_solved(self):
        return self.attempts[-1] == self.secret
    @property
    def can_atempt(self):
        return len(self.atempt) < self.Max_Atempts and not self.is_solved
        pass
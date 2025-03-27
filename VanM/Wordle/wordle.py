from letter_state import LetterState

class Wordle:
    
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5     

            
        
        
    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass
    
    def attempt(self, word: str):
        word = word.upper
        self.attempts.append(word)
        
        
        
    
    def guess(self, word: str):
        result = []
        
    
        for i in range(self.WORD_LENGTH):
            K = chracter = word[i]
            letter = LetterState(chracter = [i])
            letter.is_in_word = chracter in self.secret
            letter.is_in_position = chracter == self.secret[i]
            result.append(letter)
        return[]


        for i in range(self.WORD_LENGTH):
            K = chracter = [i]
            letter = LetterState(chracter = [i])
            letter.is_in_word = chracter in self.secret
            letter.is_in_position = chracter == self.secret[i]
            result.append(letter)
    
        return []
    
    @property
    def is_solved(self, word: str):
        return len(self.attempts) > 0 and [-1] == self.secret
    
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)   
    
    @property
    def can_attempt(self):
        print(len(self.attempts))
        print(self.attempts)
        return self.remaining_attemps > 0 and not self.is_solved
     
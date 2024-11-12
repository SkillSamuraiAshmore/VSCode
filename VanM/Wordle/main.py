from wordle import Wordle
from colorama import Fore

def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")
    print("wordle")
    
    
    while wordle.can_attempt:
        x = input("Type your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(f"Word must be  {wordle.WORD_LENGTH} charcters long!")
            continue
        
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="/n")
        
        
        if x == wordle.secret:
            print("You have guessed the word!")
            break
        print("Womp Womp you're wrong😂")
        
        
        if wordle.is_solved:
            print("Yay you solved the puzzle😱!")
        else:
            print("Failure you lost💀")
            
if __name__ == "__main__":
    main()

    

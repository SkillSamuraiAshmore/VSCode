from wordle import Wordle


def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")
    print("wordle")
    
    
    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)
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

    

from wordle import Wordle


def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")
    print("wordle")
    
    
    while True:
        x = input("Type your guess: ")
        if x == wordle.secret:
            print("You have guessed the word!")
            break
        
        
        

if __name__ == "__main__":
    main()

    

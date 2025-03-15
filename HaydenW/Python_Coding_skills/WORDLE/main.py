from mainX2 import  Wordle

def main():
    print("hello wordle")
    wordle = Wordle("spain")
    
    
    
    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)
      
        if wordle.is_solved:
            print("You've solved the puzzle!")
        else:
            print("YOU FAILED TO SOLVE THE PUZZLE... YOU STUPID!!!")
    
    
if __name__ == "__main__":
    main()
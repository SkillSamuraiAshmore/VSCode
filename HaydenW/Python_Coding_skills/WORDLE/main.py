def main():
    print("hello wordle")
    wordle = Wordle("Apple")
    
    
    
    while True:
        x = input("Type your guess: ")
        if x == wordle.secret:
            print("you have guessed the rigt word!!!")
            break
        print("Your guess is incorrect")
    
    
if __name__ == "__main_":
    main()
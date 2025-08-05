from wordle import Wordle


def main():
    print("hello wordle!")
    wordle = Wordle("APPLE")
    print(wordle)
    
    while True:
        x = input("type your guess: ")   
        if x == wordle.secret:
            print("You have succeeded")
            break
        print("your guess is incorect")
    
    
if __name__ == "__main__":
    main()
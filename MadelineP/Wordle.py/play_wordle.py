from wordle import Wordle


def main():
    print("hello world!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)
        result = wordle.guess(x)
        print(result)
        
    if wordle.is_solved:
        print("You've sovled the puzzle")

    else:print("You have failed to solve the puzzle!")

if __name__ == "__main__":
    main()


from wordle import Wordle
from colorama import Fore

def main():
    print("hello wordle!")
    wordle = Wordle("APPLE")
   
    
    while wordle.can_attempt:
        x = input("type your guess: ")   
        if len(x) != wordle.Word_length:
            print(Fore.RED + f"word MUST be {wordle.Word_length} letters  long !!!!!!!" + Fore.RESET)
            continue
        wordle.attempt(x)
        display_results(wordle)
    if wordle.is_solved:
        print("you have solved the puzzle")
    else:
        print("you failled to solve the puzzle")
    
    
def display_results(Wordle):
    for word in Wordle.attempts:
        result = Wordle.guess(word)
    pass

def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position_:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            coulor = Fore.LIGHTWHITE_EX
            
            
            
            
if __name__ == "__main__":
       main()

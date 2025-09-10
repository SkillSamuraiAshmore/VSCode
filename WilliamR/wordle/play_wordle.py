from wordle import Wordle
from colorama import Fore
from letter_state import LetterState

def main():
    print("hello wordle!")
    #instantiating the Wordle class (building the house)
    wordle = Wordle("APPLE")
   
    
    while wordle.can_attempt:
        x = input("\ntype your guess: ")   
        if len(x) != wordle.Word_length:
            print(Fore.RED + f"word MUST be {wordle.Word_length} letters  long !!!!!!!" + Fore.RESET)
            continue
        wordle.attempt(x)
        display_results(wordle)
    if wordle.is_solved:
        print("you have solved the puzzle")
    else:
        print("you failled to solve the puzzle")
    
    
def display_results(wordle: Wordle):
    print("\nresults.....\n")
    print(f"You Have {wordle.remaining_attempts } attempts remaining\n")
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color
        print(colored_result_str)
    for _ in range(wordle.remaining_attempts):
        print(" ".join (["_"] * wordle.WORD_LENGTH))

def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position_:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            coulor = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return "".join(result_with_color)
def draw_border_around         
            
            
if __name__ == "__main__":
       main()

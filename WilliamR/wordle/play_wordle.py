from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
import random


def main():
    
    word_set = load_word_set("WilliamR/data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle("secret")
    
    
    print("hello wordle!")
    #instantiating the Wordle class (building the house)
    wordle = Wordle("APPLE")
   
    
    while wordle.can_attempt:
        x = input("\ntype your guess: ")   
        if len(x) != wordle.Word_length:
            print(Fore.RED + f"word MUST be {wordle.Word_length} letters  long !!!!!!!" + Fore.RESET)
            continue
        
   
         
        if not x in word_set:
            print(Fore.RED + f" is not a valid word" + Fore.RESET)
            continue    
        
        
        wordle.attempt(x)
        display_results(wordle)
    if wordle.is_solved:
        print("you have solved the puzzle")
    else:
        print("you failled to solve the puzzle")
        print(f"the secret word was: {wordle.secret}")
    
def display_results(wordle: Wordle):
    print("\nresults.....\n")
    print(f"You Have {wordle.remaining_attempts } attempts remaining\n")
    
    lines = []
    
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color
        lines.append(colored_result_str)
        
    for _ in range(wordle.remaining_attempts):
        print(" ".join (["_"] * wordle.WORD_LENGTH))
    draw_border_around(lines)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r" ) as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


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

def draw_border_around(lines: list[str], size: int = 9, pad: int = 1):  
    
    content_length = size + pad * 2
    top_border = "┌"  +  "─"  * content_length + "┐"
    bottom_border = "└"  +  "─"  * content_length + "┘"
    space = " " * pad
    print(top_border)
    
    for line in lines:
        print("│", +  space + line + space + "│")

        
    print(	bottom_border)  
    
         
    if __name__ == "__main__":
       main()

from wordle import Wordle
from colorama import Fore

def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")
    print("wordle")
    
    
    while wordle.can_attempt:
        x = input("Type your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be  {wordle.WORD_LENGTH} charcters long! + {Fore.RESET}")
            continue
        
            
        wordle.attempt(x)
        display_results(wordle)
        
            
        if x == wordle.secret:
            print("You have guessed the word!")
            break
        print("Womp Womp you're wrong😂")
        
        
        if wordle.is_solved:
            print("Yay you solved the puzzle😱!")
        else:
            print("Failure you lost💀")
            
def display_results(wordle):
    print("\nYour results so far...\n ")
    print(f"You have {wordle.remaining_attemps} attemps remaing.\n ")
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)
    pass

    for _ in range(wordle.remaining_attempts):
        print(" ".join(["-"] * wordle.WORD_LENGTH))
        

    def convert_result_to_color(result: List[LetterState]):
        result_with_color = []
        for letter in result:
            if letter.is_in_position:
                color = Fore.GREEN
            elif letter. is_in_word:
                color = Fore.YELLOW
            else:
                color = Fore.WHITE
            colored_letter = color + letter.chracter + Fore.RESET
            result_with_color.append(colored_letter)
        return "".join(result_with_color)
        
def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):       
    pass
        
        
        
if __name__ == "__main__":
    main()

    


secret_word="wordle"
guess=""
guesses=0
guess_limit=3
out_of_guesses=False
while guess != secret_word and not(out_of_guesses) :
    if guesses < guess_limit:
     guess = input("Enter guess:")
     guesses+=1
    else:
     out_of_guesses=True
if out_of_guesses==False:
 print('you win')
else:
 print('you lose')
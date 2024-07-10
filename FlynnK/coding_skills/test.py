<<<<<<< HEAD
#print("hello my name is " + name)
#age = str(11)
#print("my age is " + age + " years old")

#print(20 // 3) # 6 - integer
#print(20 % 3)  # % = modulo


#fruit = "apple"
#print("my fruit is an " + fruit)
#fruit = "orange"
#age = 50
#print (age)

#age = age + 1
#print(age)

#cool = "hi" 
#print(cool + " my name is flynn")

#a = "hi "
#b = "my "
#c = "name "
#d = "is "
#e = "flynn"
#print(a + b + c + d + e)
#print(flynn)
#my = 123
#print(my + 10)
#yay = 299
#print(yay - 1)

=======
# name = "flynn"
# print("hello my name is " + name)
# age = str(11)
# print("my age is " + age + " years old")

# print(20 // 3) # 6 - integer
# print(20 % 3)  # % = modulo


# fruit = "apple"
# print("my fruit is an " + fruit)
# fruit = "orange"
# age = 50
# print (age)

# age = age + 1
# print(age)

# cool = "hi" 
# print(cool + " my name is flynn")

# a = "hi "
# b = "my "
# c = "name "
# d = "is "
# e = "flynn"
# print(a + b + c + d + e)
# code = "hi my name is flynn, i'm 11"
# flynn = "i like coding"
# print(code)
# print(flynn)
# my = 123
# print(my + 10)
# bag = 99
# print(bag + 1)
# yay = 299
# print(yay - 1)

# name = input("what is your name?")
# print("nice to meet you" + name)

# fruit = "apple"
# amount = 10
# price = 2.99
# good = True

#light = input("what it the traffic light? ")

#if light == "red":
 #   print("stop")
#elif light == "green":
  #  print("go")
#else:
   # print("uh oh!")

#name = input("what is your name? ")

#if name == "flynn":
#    print("hi " + name)
#elif name == "josh":
 #   print("hi " + name)
#elif name == "mum":
 #   print("hi " + name)
#elif name == "dad":
 #   print("hi " + name)
#else:
 #   print("this is not a good name!")

#money = 0
#if money >= 10:
 #   print("lunch")
#elif money >= 5:
    #print("snack")
#else:
 #   print("to bad")

#hi = {"o", "b"}
#print(hi)

#for i in range

import random 

score = ["leaderboard"]
maxnumber = 88
difficulty = 0 


def game():
    global maxnumber
    print('')
    difficulty = (input("please choose a difficulty 1,2 or 3 "))

    if difficulty == '1':
      maxnumber = 10
    elif difficulty == '2':
      maxnumber = 20
    elif difficulty == '3':
      maxnumber = 30

def game_over():
  replay = input("Do you want to play again? y'n ")
  if replay == "y" or replay == "Y":
    game()
  elif replay == "n" or replay == "N":
      print("thank you for playing")
      final = "\n".join(score)
      print(final)
  else:
    print("invalid input")
    game_over


lives = 10

game()
number = random.randint(1, maxnumber)
myname = input("what is your name? ")
print("well, " + myname + " , i am thinking of a number between 1 and " + str(maxnumber))

for guessTaken in range(lives):
  print("you have " + str(lives - guessTaken) + " guesses left")
  guess = input("take a guess: ")
  guess = int(guess)

  if guess == number:
    print("good job you won!")
    break
  elif guess < number:
    print("your guess is to low")
  elif guess > number:
    print("your guess is to high")

  elif guess > maxnumber:
    print("your guess is out of range")

if guess != number:
  number = str(number)
  print("Nope. that number is not what i was thinking of. i was thinking of: " + number)
  game_over()
elif guess == number:
  if guessTaken+1 == 1:
    grammar = "guess"
  else:
    grammar = "guesses"
  
  print("that is correct i was thinking of " + str(number) + " you took " + str(guessTaken+1) + grammar)

  score.append(myname + "(lVL " + str(difficulty) + ") - " + str(guessTaken+1) +grammar)
  final = "\n".join(score)
  print(final)
  game_over(1)

  




      
    
>>>>>>> 55799ab25fbcef131958cfcb0716d98e08286e11

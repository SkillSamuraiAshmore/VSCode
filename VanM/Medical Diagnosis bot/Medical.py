def name():
    name = input("What is your name?\n")
    print("Welcome " + name + "\n")
#This is the name for the objective of second parts in my comments
welcome_prompt = " - To list all patients, press 1\n - To run a new diagnosis, press 2\n - to quit, press q\n"
def appearance():
    
    diagnosis_selction = input("How is the patients general appearance\n - 1: Normal appearance\n - 2: Irritable or Lethargic\n")
    if diagnosis_selction == "1":
        print("What is the apperance of your eye?")
    
    elif diagnosis_selction == "2":
        print("Please pinch your skin")
        print("Assessing skin")
    












def list_patients():
    name()
    print("Listing patients and diagnosis")
    
    
def start_new_diagnosis():
    name()
    print("Starting a new diagnosis")    



def main():
  while(True):  
    selection = input(welcome_prompt)
    if selection == "1":        
        list_patients()
    elif selection == "2":
        start_new_diagnosis()
    elif selection == "q":    
        return
    
main() 
    
    
    
    
    
    
    # is the exmpaple for if i give up which will not happen(❁´◡`❁)
#name_prompt = "What is the patient's name?\n"
#appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"

#def list_patients():
    #print("Listing patients and diagnoses")

# Try calling the 2 functions below according to the appearance_prompt input!
#def print("Assessing skin")

#def assess_eyes():
   # print("Assessing eyes")
    
    
    
    #Start of finshed parts
    
    #REMEBER PUT THE CODE AT THE BOTTOM ONE FINSHED(EACH PART)
# The code in hashtags is code i made (Maybe later use it to look good or if we need it)
# name = input("What is your name?\n")
# print("Welcome " + name)
# copy this maybe for diagnostiscs

#Requiremnts:
# make a variable called name_prompt or smth to name the var
# make another var about their appearnace so try make smth like example which is: "How is the patients general appearance\n - 1: Normal appearance\n - 2: Irritable or Lethargic\n"
#REMEBER PUT THE CODE AT THE BOTTOM ONE FINSHED(EACH PART)



#Requiremnts:
# make a variable called name_prompt or smth to name the var
# make another var about their appearnace so try make smth like example which is: "How is the patients general appearance\n - 1: Normal appearance\n - 2: Irritable or Lethargic\n"
#REMEBER PUT THE CODE AT THE BOTTOM ONE FINSHED(EACH PART)



#irritable or lethatrgic - print("Skin pinch")
#normal - print("ask for eye appearnace")
# for this ive converted it into parts so future me knows what to do and probaly make a var for both but still keep it in the diagnoses
#REMEBER PUT THE CODE AT THE BOTTOM ONE FINSHED(EACH PART)


#Example at complete bottom of this script
# is the exmpaple for if i give up which will not happen(❁´◡`❁)
#name_prompt = "What is the patient's name?\n"
#appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
#REMEBER PUT THE CODE AT THE BOTTOM ONE FINSHED(EACH PART)

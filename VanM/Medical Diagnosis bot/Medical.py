welcome_prompt = "Welcome doctor!, What would you like today? \n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - to quit, press q\n"

# The code in hashtags is code i made (Maybe later use it to look good or if we need it)
# name = input("What is your name?\n")
# print("Welcome " + name)


def list_patients():
    print("Listing patients and diagnosis")
    
    
def start_new_diagnosis():
    print("Starting a new diagnosis")    



def main():
    selection = input(welcome_prompt)
    if selection == "1":        
        list_patients()
    elif selection == "2":
        start_new_diagnosis()
    elif selection == "q":    
        return
    
main() 
    
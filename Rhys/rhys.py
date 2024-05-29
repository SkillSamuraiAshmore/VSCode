

def vending():
    print("hello")
    money = int(input("how much money do you have? "))
    print ("soup 123 $15")
    print ("phone 12 $10")
    print ("glass 14 $5")
    input = int(input("what code ")) 
    if input == 123:
        if money >= 15:
            money -= 15
            print ("u get soup")
            print (money)
        else:
            print("u do not have money")
    elif input == 12:
        if money >= 10:
            money -= 10
            print ("u get phone")
            print (money)
        else:
            print("u do not have money")
    elif input == 14:
        if money >= 5:
            money -= 5
            print ("u get glass")
            print (money)
        else:
            print("u do not have money")
    else:
        print("wrong code")
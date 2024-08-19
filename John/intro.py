import random

def vending(money, s):
    if (s=="1"):
        if (random.randint(1, 5) == 1):
            print("Jammed, refunding $"+str(money))
        elif (money > 2):
            print("$" + str(money-2))
            print("soda")
        else:
            print("Refund because not enough ")
            print("$"+str(money))
            
    if (s=="2"):
        if (random.randint(1, 6) == 1):
            print("Jammed, refunding $"+str(money))
        elif (money > 3):
            print("$" + str(money-3))
            print("pepsi")
        else:
            print("Refund because not enough ")
            print("$"+str(money))
        
    if (s=="refund" or s=="r"):
        print("$"+str(money))
        
    if (s=="3"):
        if (random.randint(1, 3) == 1):
            print("Jammed, refunding $"+str(money))
        elif (money > 10):
            print("$" + str(money-10))
            print("family size chips")
        else:
            print("Refund because not enough ")
            print("$"+str(money))
running=True
while (running):
    money=int(input("How much cash? $"))
    s = input("Enter number ")
    if s == ("off"):
        running = False
    else:
        vending(money, s)

        
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3
    
    
print(max_num(6546546546565465465465336546543,5476465465465654654546666666,6465465465465465))
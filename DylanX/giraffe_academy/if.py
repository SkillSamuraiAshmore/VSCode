is_male= False
is_tall=False 
if is_male and is_tall:
    print('You are a tall male')
elif not(is_male) and is_tall:
    print('You are a tall woman')
elif not(is_tall) and is_male:
    print('You are a short male')
else:
    print('You are a short woman')

"""
Title: Dice
Author: Devin Mozee

Description: 

User inputs the amount of sides on a dice, then input the amount of rolls the user wants to take.
The program will return the number that the dice landed on for ever roll then show how many times the number landed 
and the percentage of each number.

"""

import random
from collections import Counter
def dice(sides,roll):
    side = sides
    number = 0
    countr = []
    for i in range(roll):
        num = random.randrange(1,side)
        countr.append(num)
    print(countr)

    organized_list = dict((i,countr.count(i)) for i in countr)
    
    print(organized_list)
    return organized_list



def percentage(organized_list,my_rolls):

    for key in organized_list.iterkeys():
        if organized_list[key] > 1:
            variable = str( int((organized_list.get(key)  / my_rolls) * 100) )        
            print("The percent of " + str(key) + " : " + variable + "%" )        











def main():
	user_side = int(input("How many sides our on your dice?"))
	my_rolls = int(input("How many rolls will you take?"))
	rolling = dice(user_side,my_rolls)
	percentage(rolling, float(my_rolls))
    

main()
import sys
import xlrd
import xlwt
from xlutils.copy import copy
import random

community_deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
chance_deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
secure_random = random.SystemRandom()
def draw_chance(pointer):
    global chance_deck, secure_random
    if(len(chance_deck) == 0):
        chance_deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    card = secure_random.choice(chance_deck)
    if(card == 0):
        pointer = 0;# move to go
    elif(card == 1):
        pointer = 24;#move to illinois ave
    elif(card == 2):
        pointer = 11#st. charles pl
    elif(card == 3):
        #utillities at 12 and 28
        if(pointer > 28):
            pointer = 12
        else:
            pointer = 12
    elif(card == 4):
        # railroads at 5,15,25,35
        if (pointer < 5):
            pointer = 5
        elif(pointer < 15):
            pointer = 15
        elif(pointer < 25):
            pointer = 25
        else:
            pointer = 35
    elif(card == 7): # back 3 spaces
        pointer -= 3
    elif(card ==8): # go to jail
        pointer = 10
    elif(card ==11): # go to reading railroad
        pointer = 5
    elif(card == 12): # go to Boardwalk
        pointer = 39
    chance_deck.remove(card)
    return pointer

def draw_community(pointer):
    global community_deck, secure_random
    if(len(community_deck) == 0):
        community_deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    card = secure_random.choice(community_deck)
    if(card == 0):
        pointer = 0;# move to go
    elif(card == 5):
        pointer = 10;#jail
    commnity_deck.remove(card)
    return pointer

def main():
    print("Welcome to Monopoly Probability simulator")
    output_file = input("Would you like to save results to excel file (y/n): ")
    if(output_file == 'y' or output_file == 'n'):
        print("Starting")
    else:
        print("Command not recognized, defaulting to no")
    workbook = xlrd.open_workbook("Monopoly_odds.xlsx")
    sheet = workbook.sheet_by_index(0)
    locations = []
    a_landed = []
    roll_distribution = [0,0,0,0,0,0]
    for row in range(sheet.nrows):
        space = sheet.cell_value(row,0)
        locations.append(space)
        a_landed.append(0)
    end_turn = input("# of turns to simulate: ")
    pointer = 0
    for i in range(int(end_turn)):
        roll = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll + roll2
        pointer += total
        if(pointer > 39):
            pointer -= 40
        if(locations[pointer] == 'Chance'):
            pointer = draw_chance(pointer)
        if(locations[pointer] == 'Community Chest'):
            pointer = draw_chance(pointer)
        a_landed[pointer] += 1
        roll_distribution[roll-1] += 1
        roll_distribution[roll-2] += 1
    for i in range(40):
        print(str(locations[i]) + ':' + str(a_landed[i]))
    for i in range(6):
        print(str(i+1) + ':' + str(roll_distribution[i]))
    if(output_file == 'y'):
        wbcopy = copy(workbook)
        wbcopy_sheet = wbcopy.get_sheet(0)
        for row in range(sheet.nrows):
            wbcopy_sheet.write(row,1,a_landed[row])
        wbcopy.save('monopoly_outputfile.xlsx')
        print('Copied')

if __name__ == '__main__':
  main()

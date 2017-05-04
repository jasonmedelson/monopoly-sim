import xlrd
import xlwt
from xlutils.copy import copy
import random

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
    for row in range(wbcopy_sheet.nrows):
        wbcopy_sheet.write(row,1,a_landed[row])
    wbcopy.save('monopoly_outputfile.xlsx')
    print('Copied')

    
    

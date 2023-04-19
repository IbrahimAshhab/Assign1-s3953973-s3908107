
import random


print("Please enter dataset size:")
print("(number of rows/columns in the dataset)")

size = int(input())

print("Please enter where the cells you want to update are in the spreadsheet:")
print("(beginning)")
print("(middle)")
print("(end)")

location = input()

f = open("UpdateCommands.in", "w")


if location == "beginning":
    lower = -1
    upper = round((size*size)*0.1)
elif location == "middle":
    lower = round((size*size)*0.45)
    upper = round((size*size)*0.55)
elif location == "end":
    lower = round((size*size)*0.9)
    upper = round((size*size))

for i in range(20):
    randRowIndex = random.randint(lower, upper)
    randColIndex = random.randint(lower, upper)
    f.write("U" + " " + str(randRowIndex) + " " + str(randColIndex) + "\n")


f.close()

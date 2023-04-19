
import random


print("Please enter dataset size:")
print("(number of rows/columns in the dataset)")

size = int(input())

print("Please enter where you are testing inserting rows/cols in the spreadsheet:")
print("(beginning)")
print("(middle)")
print("(end)")

location = input()

f = open("InsertCommands.in", "w")


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
    randIndex = random.randint(lower, upper)
    if i < 10:
        f.write("IC" + " " + str(randIndex) + "\n")
    if i >= 10:
        f.write("IR" + " " + str(randIndex) + "\n")


f.close()

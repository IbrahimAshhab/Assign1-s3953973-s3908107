import random

cellSet = set()
validInp = False
while validInp != True:
    print("Please choose dataset size:")
    print("small")
    print("medium")
    print("large")

    userInp = input()

    if userInp == "small":
        size = random.randint(100, 500)
        validInp = True
    elif userInp == "medium":
        size = random.randint(1000, 2500)
        validInp = True
    elif userInp == "large":
        size = random.randint(5000, 10000)
        validInp = True
size = 8313
print(size)
# numValCells = random.randint(0, size*size)

print("Please enter the precentage of non-None cells in the dataset:")
print("(enter a percentage between 0 and 1)")
valPercentage = input()

numValCells = round(float(valPercentage) * (size*size))
f = open("large-0.9-data.txt", "w")
f.write(str(size) + " " + str(size) + " " +
        str(round(random.uniform(-9.99, 10), 2)) + "\n")
numValCells -= 1

while numValCells != 0:
    randRow = random.randint(0, size-1)
    randCol = random.randint(0, size-1)
    if (randRow, randCol) not in cellSet:
        f.write(str(randRow) + " " + str(randCol) + " " +
                str(round(random.uniform(-9.99, 10), 2)) + "\n")
        cellSet.add((randRow, randCol))
        numValCells -= 1
f.close()

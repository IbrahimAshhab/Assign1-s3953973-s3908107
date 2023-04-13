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
        size = random.randint(1000, 5000)
        validInp = True
    elif userInp == "large":
        size = random.randint(10000, 50000)
        validInp = True

numIters = random.randint(0, size*size)
f = open("generatedData.txt", "w")
while numIters != 0:
    randRow = random.randint(0, size-1)
    randCol = random.randint(0, size-1)
    if (randRow, randCol) not in cellSet:
        # print(randRow, randCol, round(random.uniform(-9.99,10), 2))
        f.write(str(randRow) + " " + str(randCol) + " " +
                str(round(random.uniform(-9.99, 10), 2)) + "\n")
        cellSet.add((randRow, randCol))
        numIters -= 1
f.close()

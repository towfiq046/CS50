while True:
    try:
        var = int(input("Height: "))
        break
    except ValueError:
        print("Character is not allowed!")

if var > 8 or var <= 0:
    var = 4

space = 1

for row in range(var):
    for s in range(var - space):
        print(" ", end="")
    space += 1
    for left in range(row + 1):
        print("#", end="")
    for middle in range(2):
        print(" ", end="")
    for right in range(row + 1):
        print("#", end="")

    print("")

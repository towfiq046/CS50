while True:
    try:
        var = int(input("Height: "))
        break
    except ValueError:
        print("Character is not allowed!")
        
if var > 8 or var <= 0:
    var = 4

for i in range(var+1):
    for j in range(var - i):
        print(" ", end="")
    for i in range(i):
        print("#", end="")
    print()

o = int(input("Enter the size of O: "))

for row in range(o):
    for col in range(o):
        if (
            row == 0 or row == o - 1              # Top and bottom borders
            or col == 0 or col == o - 1           # Left and right borders
        ):
            print("*", end='')
        else:
            print(" ", end='')
    print()

j = int(input("Enter the size of J: "))

for row in range(j):
    for col in range(j):
        if row == 0:  # Top horizontal line
            print("*", end='')
        elif col == j // 2:  # Middle vertical line
            print("*", end='')

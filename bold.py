j = int(input("Enter the size of J (minimum 5): "))

for row in range(j):
    for col in range(j):
        if row == 0:
            print("*", end='')  # Top horizontal bar
        elif col == j // 2:
            print("*", end='')  # Vertical middle bar
        elif row >= j - 2 and col <= j // 2:
            print("*", end='')  # Bottom hook (bold curve)
        else:
            print(" ", end='')
    print()

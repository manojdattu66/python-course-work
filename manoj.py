m = int(input("Enter the size of M: "))

for row in range(m):
    for col in range(m):
        # Left and right vertical lines
        if col == 0 or col == m - 1:
            print("*", end='')
        # Diagonals inside M (only for upper half)
        elif row == col and row <= m // 2:
            print("*", end='')
        elif row + col == m - 1 and row <= m // 2:
            print("*", end='')
        else:
            print(" ", end='')
    print()

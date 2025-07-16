m = int(input("Enter the size of A: "))

for row in range(m):
    for col in range(m):
        if (
            (col == 0 or col == m - 1) and row != 0  # Side bars except top row
            or row == 0 and col > 0 and col < m - 1  # Top bar
            or row == m // 2                         # Middle bar
        ):
            print("*", end='')
        else:
            print(" ", end='')
    print()

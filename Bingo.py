import random

print("Let's play Bingo!")

# Generate unique random numbers for the computer and user matrices
unique_random_numbers = random.sample(range(1, 26), 25)
matrixC = [unique_random_numbers[i:i+5] for i in range(0, 25, 5)]

unique_random_numbers = random.sample(range(1, 26), 25)
matrixU = [unique_random_numbers[i:i+5] for i in range(0, 25, 5)]

# Display the user's numbers
print("Your numbers are:")
for row in matrixU:
    print("\t".join(map(str, row)))

# List to keep track of available numbers
my_list = [i for i in range(1, 26)]

# Function to check rows, columns, and diagonals for Bingo
def chickM(matrix, func):
    listrow = []
    listcol = []
    bingo = 0  # Initialize bingo count

    for i in range(5):
        rowbi = 0  # Initialize row count
        colbi = 0  # Initialize column count
        for j in range(5):
            if matrix[i][j] == 0:
                rowbi += 1
            if matrix[j][i] == 0:
                colbi += 1
        listrow.append(rowbi)
        listcol.append(colbi)
        if rowbi == 5:
            bingo += 1
        if colbi == 5:
            bingo += 1

    # Check diagonals
    diag1 = sum(1 for i in range(5) if matrix[i][i] == 0)
    diag2 = sum(1 for i in range(5) if matrix[i][4 - i] == 0)

    if diag1 == 5:
        bingo += 1
    if diag2 == 5:
        bingo += 1

    if func == "result":
        return bingo
    if func == "row":
        return listrow
    if func == "col":
        return listcol
    if func == "diag":
        return [diag1, diag2]

# Function to choose the best move for the computer
def chose():
    max_zeros = 0
    pos = ""
    k = 0

    listY = chickM(matrixC, "row")
    listZ = chickM(matrixC, "col")
    diagZ = chickM(matrixC, "diag")

    for i in range(5):
        if listY[i] > max_zeros:
            max_zeros = listY[i]
            pos = "row"
            k = i

    for i in range(5):
        if listZ[i] > max_zeros:
            max_zeros = listZ[i]
            pos = "col"
            k = i

    if diagZ[0] > max_zeros:
        max_zeros = diagZ[0]
        pos = "diag1"
    if diagZ[1] > max_zeros:
        max_zeros = diagZ[1]
        pos = "diag2"

    if pos == "row":
        for j in range(5):
            if matrixC[k][j] != 0:
                return matrixC[k][j]
    elif pos == "col":
        for i in range(5):
            if matrixC[i][k] != 0:
                return matrixC[i][k]
    elif pos == "diag1":
        for i in range(5):
            if matrixC[i][i] != 0:
                return matrixC[i][i]
    elif pos == "diag2":
        for i in range(5):
            if matrixC[i][4 - i] != 0:
                return matrixC[i][4 - i]

    return random.choice([num for row in matrixC for num in row if num != 0])

# Main game loop
while True:
    # User's turn
    while True:
        try:
            num = int(input("Enter a number: "))
        except:
            print("Invalid input. Please enter a number.")
            continue

        found = False
        for i in range(5):
            for j in range(5):
                if matrixU[i][j] == num:
                    matrixU[i][j] = 0
                    found = True
                    if num in my_list:
                        my_list.remove(num)
                if matrixC[i][j] == num:
                    matrixC[i][j] = 0
                    found = True
                    if num in my_list:
                        my_list.remove(num)
        if found:
            break
        else:
            print(f"Number {num} not found. Please try again.")

    # Computer's turn
    numC = chose()
    print("I am choosing:", numC)

    for i in range(5):
        for j in range(5):
            if matrixU[i][j] == numC:
                matrixU[i][j] = 0
                if numC in my_list:
                    my_list.remove(numC)
            if matrixC[i][j] == numC:
                matrixC[i][j] = 0
                if numC in my_list:
                    my_list.remove(numC)

    # Display updated matrices with X instead of 0
    print("\nUpdated MatrixU:")
    for row in matrixU:
        print("\t".join("X" if val == 0 else str(val) for val in row))

    print("\nUpdated MatrixC:")
    for row in matrixC:
        print("\t".join("X" if val == 0 else str(val) for val in row))

    # Check for Bingo
    resultU = chickM(matrixU, "result")
    resultC = chickM(matrixC, "result")
    if resultU >= 5:
        print("\nCongratulations, you win!")
        break
    if resultC >= 5:
        print("\nOh, I win!")
        break

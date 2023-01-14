import numpy as np 

matrix1 = np.empty((3,3))

# Question 1
for i in range(0,3):
    for j in range(0,3):
        if (i==j):
            matrix1[i][j] = 1
        else:
            matrix1[i][j] = 0

for i in range(0,3):
    for j in range(0,3):
        print(int(matrix1[i][j]), end=" ")
    print()

# Question 2
for i in range(0,3):
    for j in range(0,3):
        if (i!=j):
            matrix1[i][j] += 3

print()
for i in range(0,3):
    for j in range(0,3):
        print(int(matrix1[i][j]), end=" ")
    print()

matrix2 = np.delete(matrix1,2,1)

print()
for i in range(0,3):
    for j in range(0,2):
        print(int(matrix1[i][j]), end=" ")
    print()
import numpy as np
import timeit


# a = [[1, -2, 1], [2, 6, -1], [3, -2, 2]]
def transpose(a):
    transpose_matrix = []
    for z in range(len(a[0])):
        transpose_matrix.append([])
        for i in range(len(a)):
            transpose_matrix[z].append(a[i][z])
    return transpose_matrix

def npInverse():
    #a = [[1, -2, 1], [2, 6, -1], [3, -2, 2]]
    a = np.array([[1, -2, 1], [2, 6, -1], [3, -2, 2]])
    return np.linalg.inv(a)

def inverse():
    a = [[1, -2, 1], [2, 6, -1], [3, -2, 2]]
    determinant = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[1][0]*a[2][1]*a[0][2] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[1][0]*a[0][1]*a[2][2]
    if determinant != 0:
        b = [[], [], []]
        b[0].append((-1)**(1+1) * (a[1][1]*a[2][2] - a[1][2]*a[2][1]))
        b[0].append((-1)**(1+2) * (a[1][0]*a[2][2] - a[2][0]*a[1][2]))
        b[0].append((-1)**(1+3) * (a[1][0]*a[2][1] - a[1][1]*a[2][0]))
        b[1].append((-1)**(2+1) * (a[0][1]*a[2][2] - a[0][2]*a[2][1]))
        b[1].append((-1)**(2+2) * (a[0][0]*a[2][2] - a[0][2]*a[2][0]))
        b[1].append((-1)**(2+3) * (a[0][0]*a[2][1] - a[0][1]*a[2][0]))
        b[2].append((-1)**(3+1) * (a[0][1]*a[1][2] - a[0][2]*a[1][1]))
        b[2].append((-1)**(3+2) * (a[0][0]*a[1][2] - a[0][2]*a[1][0]))
        b[2].append((-1)**(3+3) * (a[0][0]*a[1][1] - a[0][1]*a[1][0]))
        b = transpose(b)
        for i in range(3):
            for z in range(3):
                    b[i][z] = b[i][z]/determinant
        # for row in b:
        #     print(row)
    else:
        print('Определитель матрицы равен нулю, составить обратную матрицу невозможно')

#inverse(a)
#print(npInverse(a))


#print("erwe")
print(timeit.timeit("npInverse()", setup="from __main__ import npInverse", number = 10))
print(timeit.timeit("inverse()", setup="from __main__ import inverse", number = 10))


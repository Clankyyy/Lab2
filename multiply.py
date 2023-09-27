
# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4

def initializeMatrix(rows, columns):
    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        result.append(row)
    return result


def multiply(m1,m2):
    columns_m1 = len(m1[0])
    rows_m1 = len(m1)
    columns_m2 = len(m2[0])
    rows_m2 = len(m2)

    result = initializeMatrix(rows_m1, columns_m2)

    if columns_m1 != rows_m2:
        print("Operation Invalid")
        return 0
    
    for i in range(rows_m1):
        for j in range(columns_m2):
            for k in range(rows_m2):
                result[i][j] += m1[i][k] * m2[k][j]
    for r in result: print(r)
    return 1
    

multiply(X,Y)
def matrixInput():
    matrix = []
    rows = 0
    columns = 0
    while 1:
        print('Введите кол-во строк в матрице (1, 2 или 3):')
        columns = input()
        if columns.isdigit():
            break
        else:
            continue
    while 1:
        print('Введите кол-во чисел в строке матрицы (1, 2 или 3):')
        rows = input()
        if rows.isdigit():
            break
        else:
            continue
    for i in range(int(columns)):
        row = []
        for j in range(int(rows)):
            print('Введите значение ' + str((j + 1)) + '-го элемента ' + str((i + 1)) + '-ой строки')
            while 1:
                element = input()
                if element.isdigit():
                    row.append(int(element))
                    break
                else:
                    print('Введите значение ' + str((j + 1)) + '-го элемента ' + str((i + 1)) + '-ой строки')
                    continue
        matrix.append(row)
    return matrix

def transpose(a):
    transpose_matrix = []
    for z in range(len(a[0])):
        transpose_matrix.append([])
        for i in range(len(a)):
            transpose_matrix[z].append(a[i][z])
    for i in range(len(transpose_matrix)):
        print(transpose_matrix[i])

def initializeMatrix(rows, columns):
    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        result.append(row)
    return result

def multiply(m1, m2):
    columns_m1 = len(m1[0])
    rows_m1 = len(m1)
    columns_m2 = len(m2[0])
    rows_m2 = len(m2)

    result = initializeMatrix(rows_m1, columns_m2)

    if columns_m1 != rows_m2:
        print("Умножение невозможно")
        return 0

    for i in range(rows_m1):
        for j in range(columns_m2):
            for k in range(rows_m2):
                result[i][j] += m1[i][k] * m2[k][j]
    for r in result: print(r)
    return 1

def check(a):
    rows = len(a)
    columns = len(a[0])
    if rows == columns and rows in [2, 3] and columns in [2, 3]:
        return 1
    else:
        return 0

def rang(a):
    rows = len(a)
    columns = len(a[0])
    if rows == 2:
        for i in range(rows):
            for z in range(columns):
                if a[i][z] == 0:
                    print('Ранг матрицы равен 1')
                    break
            if a[i][z] == 0:
                print('Ранг матрицы равен 1')
                break
        else:
            determinant = (a[0][0]*a[1][1])-(a[0][1]*a[1][0])
            if determinant == 0:
                print('Ранг матрицы равен 1')
            else:
                print('Ранг матрицы равен 2')
    if rows == 3:
       determinant = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[1][0]*a[2][1]*a[0][2] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[1][0]*a[0][1]*a[2][2]
       if determinant != 0:
           print('Ранг матрицы равен 3')
       else:
           for i in range(rows - 1):
               for z in range(columns - 1):
                    for y in range(z + 1, columns):
                        determinant = (a[i][z] * a[i+1][z]) - (a[i][y] * a[i+1][y])
                        if determinant != 0:
                            print('Ранг матрицы равен 2')
                            break
                    if determinant != 0:
                        break
               if determinant != 0:
                   break
           else:
               print('Ранг матрицы равен 1')

flag = 1
while flag:
    print('Выберите необходимую функцию:\n1 - Транспонирование матрицы\n2 - Умножение матриц\n3 - Определение ранга матрицы (возможные размеры матриц: 2x2, 3x3)')
    while 1:
        choise = input()
        if choise.isdigit and choise in ['1', '2', '3']:
            if choise == '1':
                transpose(matrixInput())
                break
            if choise == '2':
                matrix1 = matrixInput()
                matrix2 = matrixInput()
                multiply(matrix1, matrix2)
                break
            if choise == '3':
                while 1:
                    matrix = matrixInput()
                    if check(matrix):
                        rang(matrix)
                        break
                    else:
                        print('Размерность введенной матрицы не поддерживается, задайте новую матрицу (возможные размеры матриц: 2x2, 3x3):')
                        continue
                break
        else:
            print('Введите номер необходимой функции (1, 2 или 3):')
            continue
    print('Желаете ли выполнить еще одну функцию?\n1 - Да\n2 - Нет')
    while 1:
        choise = input()
        if choise.isdigit and choise in ['1', '2']:
            if choise == '1':
                break
            if choise == '2':
                flag = 0
                break
        else:
            print('Выберите ответ (1 или 2):')
            continue
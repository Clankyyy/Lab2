import numpy as np

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
    a = np.array(a)
    return a.T

def multiply(m1, m2):
    result = np.matmul(m1, m2)
    return result

def rang(a):
    return np.linalg.matrix_rank(a)



flag = 1
while flag:
    print('Выберите необходимую функцию:\n1 - Транспонирование матрицы\n2 - Умножение матриц\n3 - Определение ранга матрицы (возможные размеры матриц: 2x2, 3x3)')
    while 1:
        choise = input()
        if choise.isdigit and choise in ['1', '2', '3']:
            if choise == '1':
                print(transpose(matrixInput()))
                break
            if choise == '2':
                matrix1 = matrixInput()
                matrix2 = matrixInput()
                print(multiply(matrix1, matrix2))

                break
            if choise == '3':
                while 1:
                    matrix = matrixInput()
                    print("Ранг матрицы: ", rang(matrix))
                    break
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
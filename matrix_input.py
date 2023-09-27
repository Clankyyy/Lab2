def matrix_input():
    matrix = []
    rows = 0
    columns = 0
    while 1:
        print('Введите кол-во строк в матрице (1, 2 или 3):')
        rows = input()
        if rows.isdigit():
            break
        else:
            continue
    while 1:
        print('Введите кол-во чисел в строке матрицы (1, 2 или 3):')
        columns = input()
        if columns.isdigit():
            break
        else:
            continue
    for i in range(int(rows)):
        row = []
        for j in range(int(columns)):
            print('Введите значение ' + str((j + 1)) + '-го элемента ' + str((i + 1)) + '-ой строки')
            element = int(input())
            row.append(element)
        matrix.append(row)
    return matrix
print(matrix_input())
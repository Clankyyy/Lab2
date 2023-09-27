a = [[234, 4563, 242, 54, 35], [7, 85, 53, 42, 5645]]
b = [[543, 24], [56, 9], [4, 35]]
def transpose(a):
    transpose_matrix = []
    for z in range(len(a[0])):
        transpose_matrix.append([])
        for i in range(len(a)):
            transpose_matrix[z].append(a[i][z])
    for i in range(len(transpose_matrix)):
        print(transpose_matrix[i])
transpose(a)
print("\n")
transpose(b)
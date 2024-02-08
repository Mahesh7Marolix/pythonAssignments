matrix=[]
for i in range(4):
    sub_matrix=[]
    for j in range(4):
        a=int(input("enter the matrix element"))
        sub_matrix.append(a)
    matrix.append(sub_matrix)
print(matrix)
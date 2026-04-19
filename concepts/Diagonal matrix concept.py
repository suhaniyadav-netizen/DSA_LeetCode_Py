
# General solution / approach 
m = int(input("enter the rows"))
n = int(input("enter the columns"))   
matrix = []
for i in range(n):
    l1 = []
    for j in range(m):
        temp = int(input("enter a number"))
        l1.append(temp)
    matrix.append(l1)
print(matrix)


# Print the diagonal elements of the matrix 
matrix = [ [2,5,6], [3,1,7], [5,2,1] ]
for i in range(len(matrix)):
    print(matrix[i][i], end="")
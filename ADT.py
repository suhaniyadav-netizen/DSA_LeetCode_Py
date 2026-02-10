# ADT : ABSTRACT DATA TYPES
# It is a datatype which defines what operations can be performed on data, but not how
# these operations are implemented.

# In Short : it defines what operations to perform but not how to perform them.

# Eg : ATM machine it defines deposit, withdraw and check balance operations but not the 
# internal code of bank server which performs these operations. 


l1 = []
temp = [3,4,5,7,2] , [4,6,3,9,2]
l1.append(temp)
print(l1)

for i in range(len(l1)):
    for j in range(len(l1[i])):
        print(l1[i][j])
    
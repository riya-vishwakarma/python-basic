# Author : Riya Vishwakarma
# Created Date : 15 July, 2021
# Description : list comprehension example
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k]for i in range(x) for j in range(y) for k in range(z)  if x+y+z!=n])


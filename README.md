# python-basic-exercises

Here's the set of exercises for beginner to practise while learning python.

## **Exercise**:

Question1:-Python program to add two numbers.

 ```python
#python program to add two numbers
    
a=b=10                 #take to variables and store 10 into them
print("sum= ",(a+b))   #display their sum
```

Question2:-Python program to add to complex number.

 ```python
#python program to add two complex numbers
    
x=5.6-6j 
y=4.2-0.9j
z=x+y
print("sum= ",z)   
```

Question3:-Python program to convert numbers from octal, binary and hexadecimal systems into decimal number system.

 ```python
#python program to convert into decimal number system
x=0o17             #octal nuumber
y=0B1110010        #binary number
z=0X1c2            #hexadecimal number

x1=int(x)
y1=int(y)
z1=int(z)
print("octal 17= ",x1)
print("binary 0B1110010= ",y1)
print("hexadecimal 0X1c2= ",z1)
```

Question4:-Python program using int() function to convert numbers from different number system into decimal system.

 ```python
#python program to convert into decimal number system
    
x='0o17'         #string x containing a octal number
y='0B1110010'    #string x containing a binary number
z='0X1c2'        #string x containing a hexadecimal number

x1=int(x,8)        #hence base is 8.convert x into int
y1=int(y,2)        #hence base is 2.convert y into int
z1=int(z,16)       #hence base is 16.convert z into int

print("octal 17= ",x1)
print("binary 0B1110010= ",y1)
print("hexadecimal 0X1c2= ",z1)
```

Question5:-Python program to create a byte type array, read and display the elements of the array.

 ```python
#python program to understand byte type array

#create a list of byte numbers
list=[1,4,6,0,20,30]

#convert the list into byte types array
X=bytes(list)

#retrive elements from X using loops and display
for i in X:
   print(i)
```

Question6:-Python program to create a bytearray type array and retrive elements.

 ```python
#python program to understand bytearray type array

#create a list of byte numbers
list=[1,4,6,0,20,30]

#convert the list into byte types array
X=bytearray(list)

#modify the first two elements of X
X[0]=22
X[1]=66

#retrive elements from X using loops and display
for i in X:
   print(i)    
```

Question7:-Python program to accept a string from keybord and display it.

 ```python
#python program to accept a string from keybord
    
str=input("enter your name: ")
print("Hellow ",str)
```

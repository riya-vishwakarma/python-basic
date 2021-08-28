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

Question8:-Python program to accept a single character as string.

 ```python
#python program to accept a single character from keyboard
    
char=input("enter a character: ")
print("Your character is: "+char[0])
```

Question9:-Python program to accept a integer from keybord.

 ```python
#python program to accept a integer from keybord
    
str=int(input("enter a number: "))
print("you entered",str)         #display int number
```

Question10:-Python program to accept a float number from keybord.

 ```python
#python program to accept a float number from keybord
    
str=float(input("enter a number: "))
print("you entered",str)         #display float number
```
Question11:-Python program to accept two numbers and finding their sum.

 ```python
#python program to accept two numbers and find their sum
    
x=int(input("enter your first number: "))
y=int(input("enter your second number: "))
print("The sum of",x,"and",y,"is",x+y)

#you can also write this statment as
print("The sum of {} and {} is {}" .format(x,y,x+y))
```

Question12:-Python program to find sum and product of two numbers.

 ```python
#python program to find sum and product of two numbers
    
x=int(input("enter your first number: "))
y=int(input("enter your second number: "))

#display sum
print("The sum of {0} and {1} is {2}" .format(x,y,x+y))

#display product
print("The product of {0} and {1} is {2}" .format(x,y,x*y))

#display sum and product
print("The sum of {0} and {1} is {2} and product of {0} and {1} is {3}" .format(x,y,x+y,x*y))
```


Question13:-Python program to convert numbers from other systems into decimal number system.

 ```python
#input from other number systems     
str=input("enter hexadecimal number: ")
n=int(str. 16)         #inform the number is base 16
print("hexadcimal to decimal= ",n)
```

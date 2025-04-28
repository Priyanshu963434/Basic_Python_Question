                              #control if else loop

# Write a Python program to check whether a number is positive, negative, or zero.
num = int( input("Enter A Number : ") )
if(num>0):
    print("Positive")
else:
    if(num<0):
        print("Negative")
    else:
        print("Zero")
     
# Write a program to find the largest among three numbers.
a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
c = int( input("Enter C Number : ") )
if( (a>b) and (a>c) ):
    print(a," is Greater!")
elif( (b>a) and (b>c) ):
    print(b," is Greater!")
else:
    print(c," is Greater!")

#Write a Python program to print all prime numbers between 1 and 100.
for i in range(2,101):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
            break
    if(count==0):
        print(i)

# Write a Python program to calculate the factorial of a number.
num = int( input("Enter A Number : ") )
fact = 1
for i in range(1,num+1):
    fact=fact*i
print("Factorial : ",fact)

#Write a Python program to print the Fibonacci sequence up to n terms.
a = 0 
b = 1
n = int( input("Enter Range : ") )
for i in range(n):
    c = a+b
    print(c,end=" ")
    a = b
    b =c
'
#Write a Python program to find the greatest common divisor (GCD) of two numbers.
num1 = int( input("Enter A Number : ") )
num2 = int( input("Enter B Number : ") )
gcd = 1
for i in range(1,num1+1):
    if( (num1%i==0) and (num2%i==0) ):
        gcd = i
   
#Write a Python program to print the sum of all numbers in a given range.
start = int( input("Enter Start Range : ") )
end = int( input("Enter End Range : ") )
add = 0
for i in range(start,end+1):
    add=add+i
print("Sum of All Natural Number : ",add)
print("GCD/HCF : ",gcd)

# Write a Python program to print all even numbers between 1 and 50.
print("All Even Numbers From 1 to 50")
for i in range(1,51):
    if(i%2==0):
        print(i,end=" ")

# Write a program to find whether a given number is Armstrong or not.
# if you have a number 153, 
# And you want to add the cube root of every digit like,
# Then it will again come the same number
# 1^3+5^3+3^3 == 153
# So, 153 is an Armstrong Number

num = int( input("Enter A Number : ") )
temp = num
total = 0
while(num>0):
    rem = num%10
    total = total+rem*rem*rem
    num = int(num/10)
if(temp==total):
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")


                                               #FUNCATIONS

#Write a Python function to check if a number is prime.
def checkPrime(num):
    for i in range(2,int(num/2)):
        if(num%i==0):
            return False
    return True
num = int( input("Enter A Number : ") )
if(checkPrime(num)):
    print("Number is Prime!")
else:
    print("Number is Nor Prime!")
    
#Write a Python function to calculate the sum of all elements in a list.
def sumOfList(list1):
    total = 0
    for i in list1:
        total=total+i
    return total
list1 = [ 23,4,67,34,3,3]
print("List : ",list1)
print("Sum of All Elements : ",sumOfList(list1))

#Write a Python function that returns the factorial of a number.
def findFact(num):
    fact = 1
    for i in range(2,num+1):
        fact=fact*i
    return fact
num = int(input("Enter A Number : "))
print("Factorial : ",findFact(num))

#Write a Python function to find the maximum of three numbers.
def findLargest(tuple1):
    return max(tuple1)
num1 = int( input("Enter A Number : ") )
num2 = int( input("Enter B Number : ") )
num3 = int( input("Enter C Number : ") )
print("------------------Largest Value : ",findLargest((num1,num2,num3)))

#Write a Python function to reverse a string.
def reverseString(str1):
    revStr = ""
    for i in range(len(str1),0,-1):
        revStr = revStr+str1[i-1]
    return revStr
str1 = input("Enter A String : ")
print("Reverse String : ",reverseString(str1))

#  Write a function to check if a number is a perfect square.
def checkPerfectSquare(num):
    a = 1
    while(a*a<=num):
        if(a*a==num):
            return True
        a=a+1
    return False
num = int(input("Enter A Number : "))
if(checkPerfectSquare(num)):
    print("It's A Perfect Square Number!")
else:
    print("It's Not A Perfect Square Number!")

# Write a function that returns the greatest common divisor (GCD) of two numbers.
def findGCD(num1,num2):
    a = 1
    gcd = a
    while(a<=num1):
        if( num1%a==0 and num2%a==0 ):
            gcd=a
        a=a+1
    return gcd
num1 = int(input("Enter A Number : "))
num2 = int(input("Enter B Number : "))
print("GCD : ",findGCD(num1,num2))

# 48. Write a function to check if a number is a palindrome.
# HINT:-  if you reverse a number so, if new number is exactly matched 
# with old one is Palindrome.
def findReverse(num):
    rev = 0
    while(num>0):
        rem = num%10
        rev = rev*10+rem
        num=int(num/10)
    return rev
num = int(input("Enter A Number : "))
if(num==findReverse(num)):
    print("Number is Palindrome!")
else:
    print("Number is Not Palindrome!")

# Write a function to convert a decimal number to binary.
def convertToBinary(num):
    binary = ""
    while(num>0):
        rem = num%2
        binary = str(rem)+binary
        num=int(num/2)
    return binary
num = int(input("Enter A Decimal Number : "))
print("Binary Number : ",convertToBinary(num))

# Write a Python function that accepts a list and returns a new list with unique elements.
def findUnique(list1):
    return list(set(list1))
list1 = [2,5,3,7,8,5,9,7,6,9]
print("List : ",list1)
print("Unique List : ",findUnique(list1))









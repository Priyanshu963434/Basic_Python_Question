                                          #CONDITIONAL STATEMENT#

#WAP to calculate gross salary of an employ where hra is 20% da is 30% of basic
bs=float(input("enter basic salary: "))
if (bs>25000):
    hra=bs*20/100
    da=bs*30/100
else:
    hra=bs*25/100
    da=bs*35/100
gs=bs+hra+da
print("GROSS SALARY:",int(gs))

#WAP to check a number is ABSTRACT or not.
#hint:- a number which is fully divisible by 7 or a number which has last digit is 7
num=int(input("enter number: "))
if(num%7==0)or(num%7==7):
    print("ABSTRACT")
else:
    print("not abstract")

#WAP a programe that check if a number is even or odd.
num=int(input("enter number: "))
if(num%2==0):
    print("even")
else:
    print("odd")

#WAP to determine whether a person is eligible to vote (age >=18)or not.
age=int(input("enter age: "))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")

#WAP that asks for a user's score and prints "pass" if score is 40 or above, otherwise prints "fail".
score=int(input("enter score: "))
if(score>=40):
    print("pass")
else:
    print("fail")

#WAP to check whether a given year is a leap year or not.
num=int(input("enter number: "))
if(num%4==0):
    print("leap year")
else:
    print("normal year")

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
if(a>b):
    print("a is larger")
else:
    print("b is larger")

#WAP that takes a temperature as input and prints whether its cold (<=15c)warm(16-30c)or hot(>30c)
whether=int(input("enter the temperature: "))
if(whether<=15):
    print("its cold ")
elif(whether<=30):
    print("its warm")
else:
    print("its hot")

# write a program that calculates a person income tax based on these conditions:
#income<=50000 no tax,income 50001-100000:10%tax,income>100000:20%tax
income=int(input("enter the income: "))
if(income<=50000):
    print("NO TAX")
elif(income<=100000):
    print(income*10/100)
else:
    print(income*20/100)

# Write a program that reads an integer and prints its multiplication table.
num = int( input("Enter A Number : ") )
for i in range(1,11):
    print(num*i)

# Write a Python program to take a string as input and print it in reverse order.
string = input("Enter A String : ")
print(string[::-1])

# Write a Python program to find the length of a string.
string = input("Enter A String : ")
print("Length of String is : ",len(string))

# Write a program to take a list of numbers and print their sum.
list1 = [2,4,6,8,7]
sum = 0
for i in list1:
    sum=sum+i
print("Sum : ",sum)

# Write a Python program to take two integers as input and print their sum.
num1 = int( input("Enter A Number : ") )
num2 = int( input("Entre B Number : ") )
add = num1+num2
print("Addition : ",add) 


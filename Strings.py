                                  #STRINGS

#Write a Python program to count the number of vowels in a string.
str1 = input("Enter A String/Sentence : ")
print("Your String : ",str1)
count = 0
for i in str1:
    if(i in "aeiouAEIOU"):
        count=count+1
print("Occurences of Vowel is : ",count)

# Write a program to check if a string is a palindrome.
# HINT : An Sgring is Palindrome if any string is same if it is in its reverse form
# Example : MADAM , MADAM (Reverse) (Palindrome)
# Example : MOHAN , NAHOM (Reverse) (Not Palindrome)
str1 = input("Enter A String : ")
start = 0
end = len(str1)-1
flag = 1
while(start<end):
    if(str1[start]!=str1[end]):
        flag = 0
        break
    start=start+1
    end=end-1
if(flag==1):
    print("It's A Palindrome String!")
else:
    print("It's Not A Palindrome String!")
 
#Write a Python program to find the frequency of characters in a string.
str1 = "aman is my best friend forever"
print("String : ",str1)
tempList = [ ]
for i in list(str1):
    if(i != " "):
        if i not in tempList:
            print("Occurency of ",i," is : ",str1.count(i))
            tempList.append(i)
          
#Write a python program to remove all spaces from a string.
str1 = "We Are Learning Python"
print("String : ",str1)
strList = str1.split(" ")
str2 = ""
for i in strList:
    str2=str2+i
print("Removed All Spaces : ",str2)

#Write a Python program to check if two strings are anagrams.
# HINT : If all the characters are same in both string even occurency.
# so, pair of this strings are Anagram
str1 = "LISTEN"
str2 = "SILENT"
list1 = list(str1)
list2 = list(str2)
if(len(list1)==len(list2)):
    count = 0
    for i in list1:
        if(i in list2):
            count=count+1
            list2.remove(i)
    if(count==len(list1)):
        print("Strings Are Anagram!")
    else:
        print("Strings Are Not Anagram!")
else:
    print("Strings Are Not Anagram!")

#Write a program to capitalize the first letter of each word in a string.
str1 = "we are learning python programming"
print("String : ",str1)
strList = str1.split(" ")
str2 = ""
for i in strList:
    str2=str2+i[0].upper()+i[1:]+" "
print("New String : ",str2)

#Write a Python program to reverse the words in a given sentence.
str1 = "We Are Leaning Python Programming"
print("String : ",str1)
strList = str1.split(" ")
revStr = ""
for i in strList:
    i=list(i)
    i.reverse()
    for j in i:
        revStr = revStr+j
    revStr=revStr+" "
print("Reversed String : ",revStr)

 #Write a program to find the longest word in a sentence.
str1 = "We Are Learning Programming in Python"
print("String : ",str1)
strList = str1.split(" ")
maxStr = ""
for i in strList:
    if(len(maxStr)<len(i)):
        maxStr=i
print("Longest String : ",maxStr)

#Write a Python program to replace all occurrences of a substring in a string.
str1 = "Hello India Hello World!"
print("String : ",str1)
str2 = str1.replace("Hello","Namaste")
print("New String : ",str2)

#Write a Python program to count the number of words in a string.
str1 = "We Are Learning Python Programming"
strList = str1.split(" ")
print("String : ",str1)
print("Number of Words in String : ",len(strList))










    

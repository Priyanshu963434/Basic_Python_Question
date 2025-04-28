                                #LIST AND TUPLES
'''
#Write a program to find the maximum and minimum numbers in a list.
list1 = [ 3,45,67,8,67,43,23,4,56,78,98,56,43,23,21,23 ]
min = list1[0]
max = list1[0]
for i in list1:
    if(i<min):
        min=i
    if(i>max):
        max=i
print("List : ",list1)
print("Minium Value : ",min)
print("Maximum Value : ",max)

#Write a Python program to reverse a list.
list1 = [ 2,4,6,9,5,7,3,0 ]
print("List : ",list1)
list1.reverse()
print("Reverse List : ",list1)

#Write a Python program to find the sum of all elements in a list.
list1 = [ 2,3,5,7,8,7,5,4,3,2,6 ]
sum = 0
for i in list1:
    sum=sum+i
print("List : ",list1)
print("Sum of All Elements of A List : ",sum)

#Write a Python program to count the number of occurrences of an element in a list.
list1 = [2,4,6,3,2,3,5,5,4,3,2,4,5,3,3,3,2,4,3,2]
print("List : ",list1)
num = int( input("Enter Element To Find Occurence : ") )
count = 0
for i in list1:
    if(i==num):
        count=count+1
print("Occurences : ",count)
print("Occurences : ",count)

# Write a program to merge two lists into a single list.
list1 = [2,3,4,5,6,7,8,3]
list2 = [4,2,6,8,6,4,3,6]
list3 = list1+list2
print("List1 : ",list1)
print("List2 : ",list2)
print("Merged List : ",list3)

#Write a Python program to remove duplicates from a list.
list1 = [ 2,5,7,5,4,2,5,7,4,2,4,6,3,1,4,6,4 ]
print("List : ",list1)

# 1st Way
# for i in range(0,len(list1)):
#     j = i+1
#     while(j<len(list1)):
#         if(list1[i]==list1[j]):
#             list1.pop(j)
#         j=j+1

# 2nd Way
# list1 = list(set(list1))

# 3rd Way
uniqueList = [ ]
for i in list1:
    if i not in uniqueList:
        uniqueList.append(i)
print("Removed Duplicate Values List : ",uniqueList)

 
# Write a Python program to check if an element exists in a list.
list1 = [ 32,5,78,6,4,32,43,65,78,67,34,23,45 ]
print("List : ",list1)
num = int( input("Enter A Number : ") )
if(num in list1):
    print("Item Exists!")
else:
    print("Item is not exist in List!")

# Write a Python program to find the second largest number in a list.
list1 = [ 2,6,78,43,23,56,85,90,56,23,2,6,3 ]
print("List : ",list1)
if(len(list1)>1):
    list1.sort(reverse=True)
    print("Second Largest Value : ",list1[1])
else:
    print("List has less than 2 elements only!")

 #Write a program to find the intersection of two lists.
# HINT : common elements in both List
list1 = [ 2,4,6,4,7,3,2,4,4,7,3,2 ]
list2 = [ 2,5,7,9,6,3,6,8,6,4,3,7 ]
print("List1 : ",list1)
print("List2 : ",list2)
list3 = [  ]
for i in list1:
    for j in list2:
        if(i==j):
            list3.append(j)
            list2.remove(j)
            break
print("List3 : ",list3)

# Write a Python program to convert a list of tuples into a dictionary.
list1 = [ ('a',23),('b',35),('c',35),('d',67),('e',36) ]
dict1 = dict(list1)
print("List1 : ",list1)
print("Dictionary : ",dict1)

# Output:
# List1 :  [('a', 23), ('b', 35), ('c', 35), ('d', 67), ('e', 36)]
# Dictionary :  {'a': 23, 'b': 35, 'c': 35, 'd': 67, 'e': 36}
'''




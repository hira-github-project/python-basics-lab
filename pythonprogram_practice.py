# -*- coding: utf-8 -*-

# Strings: String is data type that stores a sequence of characters.
#To Concatenate strings
str1="Hira Lal "
str2="Bhandari"
print(str1+str2)

#Length of str
#len(str)
str1="Hira Lal Bhandari"
len(str1)

str1="Hira Lal"
str2="Bhandari"
final_str=str1+" "+str2
print(final_str)
print(len(final_str))

#Indexing: helps to access character
#str="Hira Lal Bhandari"
#str[0] is 'H', str[1] is 'i' …
str="Hira Lal Bhandari"
ch = str[2]
print(ch)

#Slicing: Accessing parts of a string (very important for ML)
#Syntax: str[starting_idx: ending_idx] //ending idx is not included
#string output begins from initial index and reach upto index which is 1 index less than last one i.e. 0:5 refers H to r (less than last index) in this string
str="Hira Lal Bhandari"
print(str[0:5])
#Backward counting i.e. negative indexing for string slicing
print(str[-17:-1])

#endswith() function generates either it is "True" or "False"
str = "i am studying python for my future career."
print(str.endswith("er."))
print(str.endswith("eer"))
#capatalize() function is used to make capital letter of the string i.e. capitalize the first letter of the string
print(str.capitalize())
print(str)
#But we want to have changed in the original string we have to assign that changed variable into string variable
str=str.capitalize()
print(str)

#replace(old, new) replaces all occurrences of old i.e. for character or substring replacement
str = "I am studying python for my future career."
print(str.replace("o", "a"))
print(str.replace("far", "for"))

#find(word) returns 1st index of 1st occurrer (first letter occurance)
str = "I am studying python for my future career."
print(str.find("o"))
print(str.find("for"))

#count(word) returns how much time is it occurred?
str = "It is my first study time for python as it will be boon for my future career."
print(str.count("my"))

#To count letter
print(str.count('o'))

#Let's Practice
#WAP to input user's first name & print its length.
name=input("Enter your name: ")
print("Length of your name is", len(name))

#WAP to find the occurrence of '$' in a String
name=input("enter a string to check occurance of $ sign: ")
print("Display count", name.count('$'))

#Conditional statment practices
age = int(input("Enter your age:"))
if(age>=18):
  print("The age is valid for citizenship card.")
else:
    print("The age is not valid for citizenship card.")

#Conditional Statements
light =  input("Enter a light signal: ")
if(light == "red"):
  print("stop")
elif(light == "green"):
  print("go")
elif(light == "yellow"):
  print("look")
print("End of code")

#Find the grade using conditional statement
marks = int(input("Enter your grade: "))
if(marks>=90 and marks<=100):
	print("Grade is A")
elif(marks>=80 and marks<90):
	print("Grade is A-")
elif(marks>=70 and marks<80):
	print("Grade is B+")
elif(marks>=60 and marks<70):
	print("Grade is B")
elif(marks>=50 and marks<60):
	print("Grade is B-")
else:
	print("Non grade")

#Nesting
#if(condition):
#	if(condition):
#		print()
age=40
if(age>=18):
	if(age<=80):
		print("Age is eligible for citizenship card")
	else:
		print("can not eligible for driving")
else:
	print("Not eligible for driving")

#WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))
if (num % 2 == 0):
  print("It is even")
else:
  print("It is odd")

#WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter any three numbers "))
num2 = int(input("Enter any three numbers "))
num3 = int(input("Enter any three numbers "))
if(num1>num2 and num1>num3):
  print("Greatest number is",num1)
elif(num2>num1 and num2>num3):
  print("Greatest number is",num2)
else:
  print("Greatest number is: ",num3)

#WAP to find the greatest of 4 numbers entered by the user.
num1 = int(input("Enter any three numbers "))
num2 = int(input("Enter any three numbers "))
num3 = int(input("Enter any three numbers "))
num4 = int(input("Enter any three numbers "))
if(num1>num2 and num1>num3 and num1>num4):
  print("Greatest number is",num1)
elif(num2>num1 and num2>num3 and num2>num4):
  print("Greatest number is",num2)
elif(num3>num1 and num3>num2 and num3>num4):
  print("Greatest number is",num3)
else:
  print("Greatest number is: ",num4)

#WAP to check if a number is a multiple of 7 or not.
num = int(input("Enter a number"))
if(num % 7 == 0):
  print("Number is multiple of 7")
else:
  print("Number is not multiple of 7")

#Chapter 3: Tuples and List
'''List in Python
A built-in data type that stores set of values
It can store elements of different types(integer, float, string, etc.)'''
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
#To print marks of particular index
print(marks[0])
#To find length of list marks
print(len(marks))

#We can store elements of different data type in a python list
student = ["Karan", 85, "Delhi"]
print(student[0])
#Python list allows to change value of specific index
student[0] = "arjun"
#To print new list after change
print(student)

#List Slicing
#Similar to String Slicing
marks = [85, 94, 76, 63, 48]
print(marks[1:4])
#slicing
print(marks[-3: -1])

'''
List Slicing
Similar to String Slicing
list_name[starting_idx: ending_idx] ending idx is not included
'''
marks = [85, 94, 76, 63, 48]
print(marks[-3:-1])

#List specific methods
'''
list.append(4)
list.sort(reverse=True)
list.reverse()
list.insert(idx, el)
'''
#To append new element in the list i.e. also known as mutation
list = [2, 1, 3]
list.append(4)
print(list)

# To sort list elements
list = [2, 1, 3]
print(list.sort()) #It does not return any value
#Now we run this below statement to display the members of the list
print(list)

#To print list in reverse order
list = [2, 1, 3]
print(list.sort(reverse=True))
print(list)
# To sort string type of list
list = ["banana", "litchi", "apple"]
print(list.sort(reverse=True))#prints list in descending order
print(list)

#prints list in ascending order
list = ["banana", "litchi", "apple"]
print(list.sort())
print(list)

# To sort characters of the list
list = ['a', 'd', 'e', 'f', 'c', 'b']
print(list.sort(reverse=True))
print(list)

#To reverse characters of the list
list = ['a', 'd', 'e', 'f', 'c', 'b']
list.reverse()
print(list)

#To add new element in a list whereever we want
list = ['2', '1', '3']
list.insert(0, 7)#inserting the value 5 in the second index i.e. list[1]
print(list)

#To remove an element of a list
list = ['2', '1', '3']
list.pop(2)#to remove a indicated value
print(list)

#Tuples in Python
#A built-in data type that lets us create immutable sequence of values.
tup = (2, 1, 3, 1)
print(type(tup))
#To print value according to index with tuple
print(tup[0])
print(tup[1])
#We can not assign new value in the tuple as done in list

#To print value of different index
tup = (1, 2, 3, 3, 2)
print(tup.index(2))
#To count the particular element of tuple
print(tup.count(2))

#WAP to ask the user to enter names of their 3 favorite movies & store them in a list

# Create an empty list
strings = []

# Take 3 strings as input from the user
for i in range(3):
    s = input(f"Enter string {i + 1}: ")
    strings.append(s)

# Display the list of strings
print("\nThe list of entered strings is:")
print(strings)

#WAP to ask the user to enter name of their 3 favourite movies & store them in a list without using loop
movies = [] #At first array is empty
movie1 = input("Enter first movie:")
movie2 = input("Enter second movie:")
movie3 = input("Enter third movie:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#WAP to check if a list contains a palindrome of elements
# e.g. [1,2,3,2,1] ,[1,"abc","abc",1]
list1 = [1,2,1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
	print("palindrome")
else:
	print("Not palindrome")

#WAP to check if a list contains a palindrome of elements
# e.g. [1,2,3,2,1] ,[1,"abc","abc",1]

list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
	print("palindrome")
else:
	print("Not palindrome")

#WAP to count the number of students with the "A" grade in the following tuple.
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

'''
Dictionary and set data structure type in python
Dictionary in Python
Dictionaries are used to store data values in key:value pairs
They are unordered, mutable(unchangeable) & don't allow duplicate keys
'''
info = {
	"key" : "value",
	"name" : "Thapathali Campus",
  "subjects" : ["python", "C", "Java"],
  "topics" : ("dict", "set"),
	"learning" : "coding",
	"age" : 35,
	"is_adult" : True,
	"marks" : 94.4
}
print(type(info))
info["name"] = "Shradha"
info["surname"] = "Khapra"
print(info)

#If we want to print individual dictionary type, write the following
print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info["age"])

#Nested Dictionary in python
student = {
	"name" : "Rahul Kumar",
	"subjects" : {
		"phy" : 97,
		"chem" :98,
		"math" : 95
	}
}
print(student["subjects"])
print(student)

'''
Dictionary Methods
myDict.keys() return all keys
myDict.values() returns all values
myDict.items() returns all (key, val) pairs as tuples
myDict.get("key") returns the key according to value
myDict.update(newDict) inserts the specified items to the diction
'''

student = {
    "name" : "Sunil Kumar Pandeya",
    "subjects" : {
        "Physics" : 97,
        "Chemistry" : 98,
        "Mathematics" : 95
		  }
}
print(student.keys())
print(list(student.keys()))

#myDict.values returns all values
print(student.values())

#myDict.items() returns all (key, val) pairs as tuples
print(student.items())
print(list(student.items()))

#If we want to access value of particular index of key value,we simply do
pairs = list(student.items())
print(pairs[0])
print(pairs[1])

#If we put wrong key inside double quote, first line give error but second line of code give 'None' if there doesn't exist value
print(student["name"])
print(student.get("name"))

#myDict.update(newDict) inserts the specified items to the dictionary
student.update({"city": "Delhi"})
print(student)


new_dict = {"age" : 16}
student.update(new_dict)

'''
Next data structure in Python is set
Set is the collection of the onordered items.
Each element in the set must be unique & immutable.
'''
#To declar empty set we use the following syntax
collection = set()
collection = {1, 2, 3, 4, "Namaste", "Suman"}
print(collection)
print(type(collection))
print(len(collection)) # print toal number of items

'''
Set methods
set.add()
set.remove()
set.clear()
set.pop
'''
collection = set()
collection.add(1)
collection.add(2)
collection.add("ram")
collection.add("Sita")
#we can also pass tuple here
collection.add((4,5,6))
#collection.remove(2)

#Before removing the elements
print(collection)
#To remove all the elements of the set, we use
collection.clear()

#After removing
print(collection)
print(len(collection))

# To remove random value of set
collection = {"hello", "Zebra College", "hi!", "sample code", "Python"}
print(collection.pop())

'''
Let's Practice
Store following word meaning in a python dictionary:
table: "a piece of furniture", "list of facts & figures"
cat: "a small animal"
solution:
'''
dictionary = {
	"cat" : "a small animal",
	"table" : ["a piece of furniture", "list of facts & figures"]
}
print(dictionary)

'''
print(dictionary)
You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
"Python", "Java", "C++", "Javascript", "J
'''
subjects = {
	"Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"
}
print(subjects)
print(len(subjects))

m1 = int(input("Mark of first subject: "))
m2 = int(input("Mark of first subject: "))
m3 = int(input("Mark of first subject: "))
marks = {
	"marks1" : m1,
	"marks2" : m2,
	"marks3" : m3
}
print(marks)

'''
WAP to enter marks of 3 subjects from the user and store them in a dicctionary.
Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
'''

marks = {}
x = int(input("Enter marks for English: "))
marks.update({"English":x})

x = int(input("Enter marks for Mathematics: "))
marks.update({"Mathematics":x})

x = int(input("Enter marks for Science: "))
marks.update({"Science":x})

print(marks)

#Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)


values = {
	("float", 9.0),
	("int", 9)
}
print(values)

count = 1
while count <= 5:
  print("hello")
  count = count + 1

#print numbers from 1 to 5
num = 1
while num <= 5:
  print(num)
  num =  num + 1

#print numbers from 5 to 1 in decreasing order
num = 5
while num >= 1:
  print("num is: ", num)
  num =  num - 1

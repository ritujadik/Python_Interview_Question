"""Daily 10 Interview Question Series"""

#Que:1-what is python and what are some of its key features?
# Ans: Python is the high level language which is interpreted and user-friendly and it is used in all the fields such as
#data science,data analysis,gaming,website development etc

#Que:2 what is the difference between list and tuple
#Answer-list is the mutuable data type while tuple is the immutable data type
# we denoted the list by [] while we denoted  the tuple in ()
# list is slow performance wise while tuple is fast
# we can perform the CRUD operation with list while we cannot perform the same with tuple
# Example
# x = [1,2,3,4]
# y = (1,2,3)
# print(type(x)) #to know the type of x
# print(type(y)) #to know the type of y

#Que:3 what is the difference between in set and dictionary?
#Answer: set is the unique collection of elements while dictionary is the collection of key-value pair
#set and dictionary denoted by the same way { }
#Example:
# x = set()
# y = dict()
# print(type(x)) #to know the type of x
# print(type(y)) #to know the type of y

#Que:4 what is the use of 'self' keyword in python?
#Answer:"self" refers to the instance of a class that a method calls.it is typically used with in a method to refer a instance variable
#or contact other instance methods.when a method calls on an instance of a class,the self keyword access the instance attributes or methods"

# "easy definition is self is a reference to the current instance of the class"
# Example
# class Stationery():
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
#     def item(self):
#         print(f"{self.name} is {self.price} per unit")
#
# new_item = Stationery("Pencil",40)
#
# new_item.item()
# Que:5 what is a lambda function in python
# lambda function is an anonymous function which we create to execute once and we cannot reuse the same like normal function also it
# writes in a one line
#Example-square of the numbers 1 to 10
# x = lambda i:i*i
# square_number = [x(i) for i in range(1,11)]
# print(square_number)
#Que:6 what is the purpose of init method in python
#Answer:init method is like a constructor which is used for instantiating the objects of a class.
#Example
# class Stationery():
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
#     def item(self):
#         print(f"{self.name} is {self.price} per unit")
#
# new_item = Stationery("Pencil",40)
#
# new_item.item()

#Ques-7 How you can check the type of a variable?
#Answer: we can use 'type' built in method to check type of any variable
#example
# x=5
# print(type(x))
#Que-8 what is the difference between "is" and "=="?
#Answer: "is" keyword check both the object are refering the same memory allocation or not if yes then it return true else it return false
# "==" check like both the object has same value or not
#Example
# x=[1,2,3]
# y = [1,2,3]
# print(y is x)# O/P is false as memory allocation is different
# print(x==y)#O/P is true as value of x and y is same

#Que:9 what is the decorators in python and how are they used
# Answer: decorators are the function in which we use yield instead of return it pause the function after generated one output and wait for the next
# example
# def table(x):
#     for i in range(1,11):
#         yield x*i
#
# x = 5
# table_gen = table(x)
# print(next(table_gen))
# print(next(table_gen))

#Que:10 How do you create a function in python?
#Answer: we use below structure to create a function in python
# example
# def myfunction(x):
#     return x*x
#
# y = myfunction(2)
# print(y)









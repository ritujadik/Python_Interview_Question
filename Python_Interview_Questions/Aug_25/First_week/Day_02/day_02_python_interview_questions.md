1.What is the difference between is and == in python?

Answer:"is"-operator known as identity operator and it check wether two variables point the same object in the memory.
it return True if both refers to the exact same object.

like a = 2, b = a then we can say that a is b then answer would be true

"==" it is a comparison operator which helps to compare the value of two objects
etc.it always returns a True if both the object has same value no matter they are saved in different space in memory
like x = 2,y=2
print(x==y)
O/P-True

2.what is the difference between list and tuple in python?

Answer:List-a)List is a mutuable object
b)We can perform CRUD operation like add,delete or update the object.
c)It is most often used data type in python.
d)We always use [] brackets for list
e)Performance wise it is fast incomparison of list
Tuple-a)Tuple is unmutuable object
b)We cannot perform any changes like CRUD operatin once it has been created.
c)Performance wise it is fast incomparison of list.
d)We use () brackets for tuples.

3.What are python decorators and how are they used?Give a brief explanation?

Answer-decorators are the special type of functions who take the other function as an argument
and modify the behaviour of that function without changing in their originality.
* They are used to wrap another function to extend or modify its behaviour
* The @decorator_name syntax is shorthand to apply a decorator to a function.
Ex- def decorator(func):
       def wrapper():
            print("before the function runs")
            result = func()
            print("after the function runs)
        return wrapper
    
@ decorator
def greet():
    return "Hello"

print(greet())

O/P-before the function runs
    Hello
    after the function runs 

4. what is the difference between deep copy and shallow copy in python?

Answer:Shallow copy in python when we make a copy of an object it will save at the different memory address and if we do the changes
in the copies object it will not change in the orignal object but when we do the changes in the nested element of an object
that will change in the original object too since nested object will have one reference.
we use the below syntax:

import copy

x = [1,2,4,[5,6]]

y = copy.copy(x)

y[3][1] = 9

print(x)

print(y)

O/P-x = [1,2,4,[5,9]]
    y = [1,2,4,[5,9]]

deepcopy-will help to save the copied object on difference memory location so if we will do changes in any of them either 
original or copied that update does not impacted other one

import copy

x = [1,2,4,[5,6]]

y = copy.deepcopy(x)

y[3][1] = 9
print(x)=>[1,2,4,[5,6]]
print(y)=>[1,2,4,[5,9]]**

Question-5 what is the difference between @staticmethod and @classicmethod in python?
Answer:@static method:A static method does not take any implicit first argument(neither selif nor cls)
* it behaves like a normal function but belongs to the class's namespace
* used when we want to logically group a function with a class but the function
doesn't need access to the class or instance variables.
Ex-class MyClass:
      @staticmethod
      def greet(name):
        return f"Hello,{name}"
    print(MyClass.greet("Alice"))
O/P- Hello Alice
@Classic method-A class method takes cls as its first argument
* can access or modify class-level attributes
* used when we want to define a method that should operate on the class rather than the instance
Example:
Class MyClass:
    count = 0
    @classicmethod
    def increment_count(cls):
        cls.count+=1
        return cls.count
print(MyClass.incrementcount()) =>1 
print(MyClass.incrementcount()) =>2

# Coding questions of Day 2 are given below:
1)Check given string is palindrome or not
2)Take a list of numbers and written a second largest number.
3)Count the vowels in the given string.
4)Take a string and return the dictionary with their count as a value
5)Given number is prime or not

All the codes are written in code_file




      

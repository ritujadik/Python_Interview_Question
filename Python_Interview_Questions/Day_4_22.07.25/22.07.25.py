"""
Ques-1 what is __init__?
Answer: __init__ work as a constructor in python.it automatically called to allocate memory when the new object/instance is created.
All the classes have a __init__ method associated with them.it helps in distinguishing methods and attributes of a class from the local variable
Ex- class Stationery
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def new_item(self,qty):
         self.qty = qty


x = Stationery(science,32)
print(x.name) name => science
print(x.price) price => 32
print(x.new_item(10)) => O/P is qty 10


Ques-2 what is the difference between python array and list
Answer: python array takes a homogeneous data type while python list takes the hetrogeneous data type
it is a thin wrapper aroun c language array so it consume less memory compare to the list.
Ex- import array
    arr = array.array([1,2,3])
    for i in arr:
      print(i)

Ques-3 how can you make a python script executable on Unix?
Ans: script file must begin with #!/usr/bin/envpython

Ques-4 what is slicing in python?
Answer: slicing is the specific part of the particular thing
syntax = [start,stop,step]
x = [1,2,3,4,5,6]
n = len(x)
x_new = x[0:n:2]
print(x_new)
O/P-[1,3,5]

Ques-5 what is unit tests in python
Answer: Unit test is a unit testing framework in python
Unit testing means test the different components of software separately

Ques-6 what are the global,protected and private attributes in python?
Answer:Global variables are public variables those are defined the global scope.to use the variable in the global scope inside a function
we use the global keyword

Protected attributes are the attributes which define with an underscore prefixed to their identifiers ex _ritu
they can still accessible and modified from out side the class

Private attributes are the attributes who have double underscore as a prefix so that they cannot seeing by anyone ex __ritu
they cannot accessed and modified from outside the class

Ques-7 what is PEP8 and why it is important?
Answer PEP 8 stands for Python Enhancement Propsal.A PEP 8 is a official design document providing information to the python community
or describing a new feature for python or its process.

Ques-8 what is interpreted language?
Answer Interpreted language excutes the statement line by line,such as python,R,JS

Ques-9 what is dynamically typed language?
Answer dynamically typed language are those language in which we dont have to define the data tpes before the execution and it is automatically understand by the language

Ques-10 what are negative indexes and why are they used?
Answer Negative indexes are the indexes which start from the end of the list or tuple or string
Ex-arr = [1,2,3,4]
print(arr[::-1])
O/P = [4,3,2,1]

"""
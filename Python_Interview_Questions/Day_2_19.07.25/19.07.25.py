"""Que-1 what is the concept of shallow copy and deep copy"""
import copy

"""Ans:shallow copy is the copy of original object and saved in another memory address but when we talk about nested object it refer the same memory location"""
new_x = [1,[2,3],4]
new_y = new_x.copy()
new_x.append(9)
print(new_x)
print(new_y)
new_x[1].append(5)
print(new_x)
print(new_y)

"""
Deep copy create the new_object on different memory address
"""
# x = [1,2,3]
# y = copy.deepcopy(x)
# x.append(4)
# y.append(6)
# print(x)
# print(y)

"""Que-2 How is multithreading achieved in python?"""
"""Ans:Multithreading is achieved through the use of the threading module,which allows for concurrent execution of multiple threads
However due to the GIL(Global Interpreter lock) only one thread can execute python bytecodes at a time even on multicore system.
this means while the threads are created and can run concurrently they do not achieve true parellelism when executing the CPU bound tasks.
"""
import threading
def print_numbers():
    for i in range(1,10):
        print(i)
def print_letters():
    for letter in "abcdef":
        print(letter)

thread1 = threading.Thread(target=print_letters)
thread2 = threading.Thread(target=print_numbers)

thread1.start()
thread2.start()

"""Question-3 what is pickling and unpickling"""
"Ans""Pickling is the process where we convert actual object in to a byte stream.this process also known as serialization and reverse of the same is called unpickling"

"""Question-4 how is memory managed in python"""
"Ans" "In python memory managed by heap memory where the object is saved and GC helps to allocate and disallocate the memory"

"""Question-5 Are argument in python passed by value or passed by reference
Ans: In python argument is passed by the reference.

Question-6 How would you generate random number in python 
Answer: we can generate the random number by importing random library and use the syntax like random.random

Question-7 what does the // operator do?
Answer: In python the / operator perform division and returns the quotient in the float
Ex- 5/2 return 2.5
while // operator return the quotient in an integer
Ex-5//2 will return 2

Question-8 what does the 'is' operator do?
Answer: 'is' operator compares the id of the objects
list_1 = [1,2,3]
list_2 = [1,2,3]
list_1 == lsit_2 
O/P would be true or false

Question-9 what is the purpose of the Pass statement?
Answer: The pass statement is used when there's a syntatic but not an operational requirement.
Ex- def myname(x):
       pass
       
x = [1,2,3]
y = myname(x)
print(y)
o/p should be nothing

Question-10 How will you check if all the characters in the string are alphanumeric
Answer: for that we can use isalnum() in built method of python.it will give response in true or false

Question-11 How will you merge the elements in a sequence data tpye
Ex- list_1 = [1,2,3,4]
list_2 = [4,5,6,7]
list_1 + list_2 = [1,2,3,4,4,5,6,7]
tuple_1 = (2,3,7)
tuple_2 = (4,5,6)
tuple_1 + tuple_2 = (2,3,7) + (4,5,6)
o/p = (2,3,7,4,5,6)
str_1 = "Ritu"
str_2 = "ja"
str_1 + str_2 = "Rituja"       
"""
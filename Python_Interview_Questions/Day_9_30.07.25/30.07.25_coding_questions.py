#1.what will be the output
# a = [1,2,3]
# b = a
# b.append(4)
# print(a)
# # O/P = [1,2,3,4]

# #2.what's wrong with this code
# def add_to_list(val,my_list=[]):
#     my_list.append(val)
#     return my_list
#
# print(add_to_list(4,my_list=[]))
#correct way to write the above code
def add_to_list(val,my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(val)
    return my_list
def foo(x=[]):
    x.append(1)
    return x
print(foo())
print(foo())


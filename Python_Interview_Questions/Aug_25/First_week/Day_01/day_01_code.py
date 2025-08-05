#1.Reverse a string-Program
# def reverse_string(x):
#     x_new = list(x)
#     start = 0
#     end = len(x_new)-1
#     while start<end:
#         x_new[start],x_new[end] = x_new[end],x_new[start]
#         start+=1
#         end-=1
#     return ''.join(x_new)
# x = "sita is a Ram wife"
# print(reverse_string(x))

#2.You are given a list of numbers from 1 to N, but one number is missing. Write a Python function to find the missing number in the list.
# def missing_number(x):
#     total = sum(x)
#     n = len(x) + 1
#     sum_of_n_number = n * (n+1)//2
#     missing_num = sum_of_n_number - total
#     return missing_num
#
# x = [1,2,3,4,5,6,7,9]
# print(missing_number(x))



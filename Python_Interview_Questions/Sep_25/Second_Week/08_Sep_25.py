# #1. how we can replace a string space with a given character in python?
# # str = l vey u
# # output-love you
#
# def str_man(str,char):
#     result = ''
#     for i in str:
#         if i == ' ':
#             i = char
#         result+=i
#     return result
#
#
#
# str = 'l vey u'
# char = 'o'
# print(str_man(str,char))

# 2.Given a postive integer num,write a function that returns True if num is a perfect square else False

# def perfect_num(num):
#     square = int(num**0.5)
#     check = square **2 == num
#     return check
#
#
# x = perfect_num(10)
# print(x)
# y = perfect_num(25)
# print(y)

#3. Given an integer n, return the number of trailing zeroes in n factorial n!

# def trailing_zeros(num):
#     if num<0:
#         return ("Please enter a positive number")
#     count = 0
#     while num>=5:
#         num//=5
#         count+=num
#
#     return count

#4. Can the String Be Split into Dictionary Words
# def can_string(s,dictionary):
#     for i in range(1,len(s)+1):
#         first_str = s[0:i]
#         if first_str in dictionary:
#             second_str = s[i:]
#             if (
#                 not second_str
#                 or second_str in dictionary
#                 or can_string(second_str,dictionary)
#             ):
#                 return True
#     return False
#
# s = "datacamp"
# dictionary = ["camp", "cam", "lack"]
# print(can_string(s,dictionary))


#5.Remove duplicates from a sorted array

# def remove_duplicate(arr):
#     result = []
#     for i in arr:
#         if i not in result:
#             result.append(i)
#     return result
#
# arr = [2,4,5,2,1]
# print(remove_duplicate(arr))









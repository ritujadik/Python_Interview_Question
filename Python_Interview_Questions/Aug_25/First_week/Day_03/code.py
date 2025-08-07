#1.create a list of squares from 1 to 5
#
# new_list = [x**2 for x in range(1,6)]
# print(new_list)

#2.Count frequency of characters in string
# def freq_char(x):
#     new_dict = {}
#     for i in x:
#         new_dict[i] = new_dict.get(i,0)+1
#
#     return new_dict
#
# x= "shyamana"
# print((freq_char(x)))

# #3.sort a list of tuples by the second element
# data = [(1,3),(3,1),(5,2)]
# data.sort(key=lambda x:x[1])
# print(data)

# #4.Remove duplicates from a list
# nums = [1,2,3,3,4,4,5]
# unique_nums = list(set(nums))
# print(unique_nums)

#5.combine two list into a dictionary
keys = ['name','age','city']
values = ['Alice',25,'Newyork']
combined = dict(zip(keys,values))
print(combined)

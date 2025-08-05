"""1.Write a Python function to check if a string is palindrome"""

def palindrome(string_org):
    string_fine = string_org.lower()
    string_new = string_fine[::-1]
    if string_fine == string_new:
        return ("Yes the given string is palindrome",{string_org})
    else:
        return ("This is not a Palindrome",{string_org})



x = 'Naman'
print(palindrome(x))


"""2.Write a Python function that takes a list of numbers and returns the second largest number"""

def second_largest_number(x):
    unique_numbers = list(set(x))
    if len(unique_numbers)<2:
        return ("list must be contain atleast 2 unique elements")
    unique_numbers.sort()
    return("The second largest_number is:",unique_numbers[-2])


x = [1,8,-4,2,3,7,6]
print(second_largest_number(x))

""" 3 Write a python function that counts the number of vowels in a given string.The function should be case in sensitive"""
def find_vowels(x):
    vowels = "aeiou"
    count = 0
    for i in x.lower():
        if i in vowels:
            count+=1
    return count


x = "Rahula"
print(find_vowels(x))

"""4.Write a function that takes a string as input and returns a dictionary with the count of each character in the string"""

def string_to_dict(x):
    new_dict = {}
    for i in x:
        if i in new_dict:
            new_dict[i] +=1
        else:new_dict[i] = 1

    return new_dict

x = "Ramesh"
print(string_to_dict(x))

"""5.write a python function that checks whether a number is prime or not"""
def prime_number(x):
    if x<=1:
        return ('number should be greater than 1')
    for i in range(2,int(x**0.5)+1):
        if x%i != 0:
            return ("This is a prime number:",{x})

    return ("This is not a prime number:",{x})

x = 5
print(prime_number(x))



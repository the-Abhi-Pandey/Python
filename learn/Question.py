

# 3. How do you check if a given string `s` starts with the letter 'A'?

# name = str(input("Enter any String : "))
'''
SmallName = name.lower()
for n in SmallName:
    if n == 'a':
        print ("this String starts with A")
    else:
        print(f"this String start with {n}")
    break'''

'''if name.startswith("A"):
    print("String starts with letter A")

if s[0].isalpha():
    print("The first character is an alphabet letter")'''

# 4. Write a function `is_even` that takes an integer and returns `True` if the number is even and `False` otherwise.

'''def is_even(a):
    if a % 2 == 0:
        return True
    else:    
        return False
print(is_even(4))
'''

# 5. How do you create a list of numbers from 1 to 10 using a list comprehension?


'''new = [i for i in range(1,10)]
print(new)'''


# 6. Write a Python script to find the maximum number in a list of numbers.

'''def find_max_number(numbers):
    max_number = numbers[0]
    
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    
    return max_number

numbers_list = [10, 25, 8, 42, 17, 30]
max_num = find_max_number(numbers_list)
print(f"The maximum number in the list is: {max_num}")'''


# 7. How do you remove the first occurrence of the value `3` from the list `numbers = [1, 2, 3, 4, 3, 5]`?

'''
numbers = [1, 2, 3, 4, 3, 5]
numbers.remove(3)
print(numbers)
'''

# 8. Write a `for` loop that prints all the keys in the dictionary `data = {'a': 1, 'b': 2, 'c': 3}`.
'''
data = {'a': 1, 'b': 2, 'c': 3}
for i in data.values():
    print(i)

for key in data:
    print(key)'''


# 10. Write a Python program to count the number of vowels in a given string.

# count vowels
'''
def cnt_str(strings):
    vowel = list("aeiouAEIOU")
    vow_conunt = 0
    for vow in strings:
            if vow in vowel:
             vow_conunt += 1
    return vow_conunt
        

user_input = input("Enter a string: ")
result = cnt_str(user_input)
print(f"Number of vowel in the string: {result}")'''


# count consonants
'''
def conso(strings):
    vowels = set("aeiouAEIOU")
    count_conso = 0

    for con in strings:
        if con.isalpha() and con not in vowels:
            count_conso +=1
    return count_conso

user_input = input("Enter a string: ")
result = conso(user_input)
print(f"Number of consonent in the string: {result}")
'''

# count both
'''
def count_vowels_and_consonants(s):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

user_input = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(user_input)
print(f"Number of vowels in the string: {vowels} and consonants in the string: {consonants}")

'''

# 11. How do you reverse the string `hello`?
'''
string = 'hello'
print (string[::-1])'''

# 12. Create a tuple containing the numbers from 1 to 5 and unpack them into separate variables.
'''
a = tuple("12345")
for i in a:
    print (i)
'''

# 13. How do you convert a list `['1', '2', '3']` of strings to a list `[1, 2, 3]` of integers?
'''
strings = ["1","2","3"]
ints = [ int(num) for num in strings]
print(ints)

'''

# 14. Write a function `factorial` that calculates the factorial of a given number.

'''
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

a = int(input("Enter a number: "))
print(f"The factorial of {a} is {fact(a)}")
'''

# 15. How do you merge two dictionaries `dict1` and `dict2` in Python 3.5+?
'''
a = {"key1": 1,"key2": 2}
b = {"key3": 3, "key4": 4}

z = {**a, **b} #python 3.5+

print(a|b)  #python 3.9+ 
print(z)'''


# 16. Write a Python program to print all prime numbers between 1 and 100.
'''
for num in range(1, 101):
    count = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            break
    if count == 0 and num != 1:
        print(num, end=' ')

'''

# 20. Write a `while` loop that prints the numbers from 10 to 1.

# i = 10

# while i >= 1:
#     print(i)
#     i -=1


# def outer():
#         x = "local"
#         def inner():
#             nonlocal x
#             x = "nonlocal"
#             print("inner:", x)
#         inner()
#         print("outer:", x)
# outer()


import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
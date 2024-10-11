#-----------------------------Print multiple Line-----------------------

"""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

"""

#----------------------------Access elements of the string---------------------------------
'''
a="hello world"
print (a[1])

'''

#--------------------------Looping through the Strings--------------------------------------

'''
for x in " Abhishek":
    print(x)
print(len(x))     #give the length of world

'''

#--------------------------Check Particular String prenset in Value----------------------------
'''
str ="this is a string that is wirtten by Abhishek"

print("Abhishek" in str)    #Boolean result = True/False
print("6" in str)

if "Abhishek" in str:
    print("yes: 'Abhishek' is present")

if "6" not in str:
    print("NO: '6' is not present")

'''

#----------------------------Slicing/ Upper/ Lower/ Strip/ Modify/ Split----------------------------------------

'''
str =" Abhishek pandey"
print(str[:5])
print(str.upper())
print(str.lower())
print(str.strip())            # Remove space from before and after the text
print(str.replace("e","m"))           
print(str.split())

'''

#-----------------------------String Format-------------------------------------------------

'''
a = 5
# print("let divide 10 by " + a)  --> Str can not concatinate with Int 
print( f"let divide 10 by {a}")
print( f"let divide 10 by {a:.2f}")
print( f"let divide 10 by {3*2}")

'''


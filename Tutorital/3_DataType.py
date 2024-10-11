
'''

x = str("Hello World")                       #Text
print(type(x))

x = int(5)                                   #Numerice
print(type(x))

x = float(20.5)                              #Numerice-----------Also be Scientific (35e3 / 12E4 / -87.7e100)
print(type(x))

x = complex(1j)                              #Numerice----------(3+5j /-5j)
print(type(x))

x = list(("apple", "banana", "cherry"))      #Sequence      
print(type(x))

x = tuple(("apple", "banana", "cherry"))     #Secquence
print(type(x))

x = dict(name="John", age=36)                #Mapping
print(type(x))

x = set(("apple", "banana", "cherry"))       #Set
print(type(x))

x = frozenset(("apple", "banana", "cherry"))  #Set
print(type(x))

x = bool(5)                                  #Boolean
print(type(x))

x = bytes(5)                               #Binary Type
print(type(x))

x = bytearray(5)                           #Binary Type
print(type(x))

x = memoryview(bytes(5))                   #Binary Type
print(type(x))

'''

#--------------------------------------Random Numbers----------------------------------------

import random
print(random.randrange(1,49))


#--------------------------------------------------Insert in list-------------------------------

'''
list1 =["apple","banana","papaya"]
list2 =["As2","PS2A"]

a = list1.insert(2,"mango")
print(list1)

a = list1.append("mango")    #add item at the end
print(list1)

list1.extend(list2)          #add 2nd list
print(list1)

list1.remove("mango")        #remove first occurrence
print(list1)

list1.pop(1)                 #remove the index no 'pop(1)' // if it is empty, will remove the last value
print(list1)

del list1                    #remove the list / same as work { `pop[1]` == `del list1[1]` }
print(list1)

list1.clear()                 #empties the list
print(list1)

'''

#------------------------------------------------ List Comprehension-------------------------------------------

'''
data = [["UK", "LONDON", "EUROPE"], ["US", "WASHINGTON", "AMERICA"], ["EG", "CAIRO", "AFRICA"], ["JP", "TOKYO", "ASIA"]]
Newlist =[continant for continant ,area, country in data]
print(Newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[x for x in fruits if "a" in x]
print(newlist)

'''

#-----------------------------------------------List Sorting----------------------------------------

'''
thislist = ["orange", "Mango", "Kiwi", "pineapple", "banana"]
thislist2 =[1,3,4,5]

thislist.sort()                           #Default it contain Captial letter and then small
print(thislist)

thislist.sort(key =str.lower)
print(thislist)                          #correct approach to sort a list


list2 = thislist.copy()
print( f"this is copied list from `thislist ` {list2} ")


for x in thislist2:                        #Add 2 list // [Alternatinve : thislist.extend(thislist2)]
    thislist.append(x)
print(thislist)   

'''




#-----------------------------------change Tuple Value------------------------------------


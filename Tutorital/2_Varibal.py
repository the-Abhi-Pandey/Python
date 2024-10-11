#---------------------------------------Casting-----------------------

'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

'''

#--------------------------------------------------Type----------------------------



'''
x =str(3)
print(type(x))   #<class 'str'>


'''

#------------------------------------------------- multiple variable in a single line-----------------------

'''
x, y, z = "Ram" ,5 , 3.0
print(x)
print(y)
print(z)

'''
#-------------------------------------One Value to multiple Variable-----------------------

'''

x=y=z="The Abhi"
print(z)
print(y)
print(x)

'''

#---------------------------Unpack a collection-----------------------------------

'''

fruit =["Apple", "Banana", "Mango"]   #Pack_of_Values
x,y,z= fruit                          #UnPack
print(z)
print(y)
print(x)

print(x,y,z)                         #Print_Multiple_Variable
print(x+y+z)                         #Result = AppleBananaMango

'''

#---------------------------Global Variable('All the above variable are G.V')-------------------------------------------

x = "Good"                         #Global_Variable

def myfunc():
    global x                        #To_make_Local_Variable,Global
    x= "Awesome"                    #Local_Variable
    print("Python is :"+ x)
myfunc()

print("Python is :"+ x)
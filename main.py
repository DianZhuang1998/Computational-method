# 
#
print("hello world!")
myName = "Dian"
myAge = 24
print ("myName")
print ("myAge")
print (type(myName))
capital = { "cat" : "xiaoru","dog" : "Dian"}
animals = ["dog" , "cat" , "snake"]
for c in animals :
    print (c)
def sum(a, b):
    result = a + b
    return result
def multiply(a, b):
    result = a * b
    return result
def squareNumber(a):
    return a**2
print(sum(10,200))
print(multiply(10,200))

import numpy as np

arrld = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (arrld)
print (arrld.shape)
print ("\n")

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (arr2d)
print (arr2d.shape)
print ("\n")
#Shallow copying is only one-level deep while deep copying is recursive.
#Using deep copying, you create the copies of every single child object, grandchild object and so on.
#In other words, deep copies are fully independent.
#However, shallow copies take original one's elemets, attributes etc 
#and give the exact same features to a completely different (in terms of id) copy.
#Therefore, their elements will have the same id s despite deep copying.
#Nevertheless, if you add an element to original one, even shallow copy cannot copy it unless you copy them again.
#Using copy module, it's possible to copy everything deeply or shallowly, even classes can be copied.

import copy

def display():
    global myList
    global shallowCopy1

    print("Original: ",myList)
    print("Shallow1: ",shallowCopy1)
    print("Shallow2: ",shallowCopy2)
    print("Deep1: ",deepCopy1)
    print()


myList = [[1,2,3],[4,5,6],[7,8,9]]
shallowCopy1 = list(myList)
shallowCopy2 = copy.copy(myList)
deepCopy1 = copy.deepcopy(myList)

display()

myList[0][0] = 111

display()

myList[1] = [444,555,666]
myList.append([10,11,12])

display()

shallowCopy1[1] = [44,55,66]
shallowCopy1.pop()

display()

shallowCopy2.append([111,222,333])
shallowCopy2[2] = [777,888,999]

display()

shallowCopy1[0][1] = 222
shallowCopy1[0][2] = 333

display()

print(myList is shallowCopy1)
print(myList is shallowCopy2)
print(myList is deepCopy1)

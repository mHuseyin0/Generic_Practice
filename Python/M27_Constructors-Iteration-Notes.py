from functools import singledispatchmethod
from math import pi
from math import sqrt
class Circle():
    @singledispatchmethod
    def __init__(self, radius: float, *, angle=360):
        self.radius = radius
        self.angle = angle
    
    @__init__.register(int) #Either pass the types here or use type annotations below
    def _fromCircumference(self, circumference, *, angle=360):
        self.radius = (360*circumference/angle)/(2*pi)
        self.angle = angle

    @__init__.register(str)
    def _fromArea(self, area, *, angle=360):
        self.radius = sqrt((360*float(area)/angle)/pi)
        self.angle = angle
    
    @classmethod
    def fromDiameter(cls, diameter: float, *, angle=360):
        return cls(diameter / 2, angle=angle)
    
#To use single dispatch method, input types should be different.(e.g. date, int, str)
#Therefore it's not the best option for a circle class
#Using optional arguments through setting default values may be useful to have multiple constructors
#Also, we can check the input type in a single constructors with conditionals(e.g. list, str)

circle1 = Circle.fromDiameter(6.0)
circle2 = Circle(str(pi))
print(circle1.radius)
print(circle2.radius)

#Iterators power and control the iteration process,
#while iterables typically hold data that you want to iterate over one value at a time.
#It's impossible to know the length of a iterator.Also, you can't go backwards.(There is only next() method, no prev().)
#Therefore, indexing and slicing operator ([]) does not work with iterators.

numbers = frozenset([0,1,2,3,4,5,6,7,8,9])
#Most useful features of frozensets that they can be used as dictionary keys

itr = iter(numbers)
#list(itr) #It's recommended to do this, because iterators are lazy.(List, set, tuple etc can be used)
#That means they do not generate all the items when they are created.
itr2 = iter(numbers) #This will remain at the first element, even if the other one is iterated over.
#All iterators are independent from each other
#However, you can define an iterator which redefines itself (in the __next__ method) when it reaches the StopIteration.

for i in iter(numbers): #Nevertheless, this will create an anonymous object, so numbers can be used again.
    print(i)

for i in range(0,10):
    print("i is: " + str(i))
    if i==3:
        continue
    if i==7:
        break
    print(next(itr)) #Once this iterator is iterated, it cannot be iterated again, so it will be EXHAUSTED.
else:
    print("Done!") #Will not be executed when loop terminated with a break statement.

print(next(itr, "This iterator is exhausted.")) #Default value will return and prevent the exception, IF iterator is exhausted.

#Definite iteration: When a loop is executed exact number of times.
#Indefinite iteration: When a loop is executed until a condition is met.(While loops)
#Iterators are memory efficient when they are compared with regular functions, sequences, and comprehensions.
#This is because their laziness.(They do not store all the data at the same time, but they store the data needed.)
#Also, only iterators can create infinite data.

#Generator
#The generator function is the function that you define using the yield statement.
#The generator iterator is what this function returns.
#Generator functions are special types of functions that allow you to create iterators using a functional style.
"""def iteratorFunc():
    print("Phase 1 has been executed.")
    yield 5
    print("Phase 2 has been executed.")
    yield
    print("Phase 3 has been executed.")
    yield
#Thanks to yield statements, functions are able to remember their states between two times they called.
#Yield keyword is very similar to return keyword.However, function isn't terminated completely.It just stops to resume any time in the future.
iterator1 = iteratorFunc()

while True:
    a = input()
    if a=="0":
        next(iteratorFunc())
        try:
            next(iterator1)
        except Exception:
            print("You cannot iterate over iterator1 anylonger.")"""

#The difference between a coroutine and generator is that a coroutine can accept arguments 
#after it's been initially called, whereas a generator can't.
#They can both accept a sequence initially, or they can generate data.
#To iterate over a given sequence, for loops can be used instead of while loops inside the function.
#To terminate a generator, return statement can be used.

#ONLY FOR EDUCATIONAL PURPOSES
from random import randint
"""def coroutineFunc():
    acceptedValue = 0
    while True:
        num = randint(0,100) + acceptedValue
        print("Your random:", num)
        acceptedValue = (yield num)  #Accepted value comes from send function.
        if acceptedValue is not None:
            print("Your number:", acceptedValue)
        yield
#Yield is an expression rather than a statement here.
iterObj = coroutineFunc()
for j in iterObj:
    if j < 50:
        iterObj.throw(ValueError("An error occured while choosing a random integer."))
    if j >200:
        iterObj.close()
    else:
        iterObj.send(x:= j+int(input("Please input an integer to add to the random integer: ")))
        if x >200:
            iterObj.close()"""

from random import choice
from random import uniform
from time import sleep
from collections.abc import Iterator

#This is a class-based iterator.Function-based iterators (generators) usually more simple to write and understand.
class myEndlessIterator(Iterator):
    def __init__(self, stop: int =None): #If you want iterator to accept a sequence, you can pass it in the constructor.
        self._index = 0            #This iterator will generate items (like fibonacci numbers).
        self.stop = stop
        self.current = 0
        self.isPositive = False
        try:
           self.isPositive = stop > 0
        except Exception:
            pass
            

    """def __iter__(self): #This function should be defined in all iterators.(Especially for loops need this to work)
        return self        #Iterator super class will implement this. 
    """

    def __next__(self): #This function is also essential for an iterator
        if type(self.stop) is int and self.isPositive:
            if self._index < self.stop:
                self.current = uniform(self.current,100)
                self._index +=1
                return self.current
            else:
                raise StopIteration #For loops will stop with this.They will handle the exception.
        else: #This is the endless part.
            self.current = uniform(self.current,10)
            self._index +=1
            sleep(1)
            return self.current
        
myIter = myEndlessIterator(5)
for i in myIter:
    print(myIter._index,"=", i)

print([item for item in [0,1,2,3,4,5,6,7,8,9]]) #List Comprehension

dict1 = dict(zip([number for number in numbers],[number*10 for number in numbers]))

for k, v in dict1.items():
    print(k,": ", v, sep="")

generatorExpression = (figure for figure in [1,2,3,4,5]) #Generator expression, returns iterator
for i in generatorExpression:
    print(i)

#In Python, a protocol is a set of dunder methods that allows you to support a given feature in a class.

#An iterable is an object implementing the .__iter__() special method or the .__getitem__() and __len__() methods as part of the sequence protocol.

#The .__iter__() method fulfills the iterable protocol.
#This method must return an iterator object, which usually doesn’t coincide with self unless your iterable is also an iterator.

#An iterable is a an object that can be passed to the iter() function to get an iterator from it.
#iter(), all(), any(), enumerate(), max(), min(), len(), zip(), sum(), map(), and filter() functions can accept iterables
#Iterables cannot passed in the next() method unless they are also iterators.
#However, if they are iterators, they cannot be iterated over multiple times, so think carefully to decide if you need them as iterators.
#To support multiple iterations through the data, you must be able to obtain multiple independent iterators from it.

#reversed() function will reverse an inputted iterable and return it as an iterator.

#Sequence protocol includes __getitem__() and __len__() methods. Lists, tuples and strings implement this protocol.(Indexing operator can be used.)
#dictionaries also implement .__getitem__() and .__len__().However, they’re considered mapping data types rather than sequences
#because the lookups use arbitrary immutable keys rather than integer indices.

#for loops always pass the data to iter() function.If data is not an iterator or iterable, an error raises.

"""xd = [1,2,3,4,5,6,7,8,9,0]
def test():
    yield from xd #Will return a generator object which contains xd iterator.

while True:
    if input()!="0":
        for i in test():
            print(i)"""

testString = "This is a test string."

print(testString.startswith('This'))
print(testString.endswith('.'))

import math
print(math.inf == float("inf"))
print(math.ceil(4.4))
print(math.floor(4.5)) 
print(math.trunc(-4.5)) #Always eliminates the decimal part and keeps integer part
#Even if math.pow() function is faster than built-in pow() and ** operator, it cannot handle complex number while the others can.
#Also ** operator is slightly faster than pow() function.
#math.fsum() function is more accurate than built-in sum() function.
print(math.gcd(12,20))
print(math.lcm(3,4))
print(math.hypot(5,12))

#Since string are immutable, assigning a value to an index is not possible.However replace() function can be used. (myString.replace("a","b"))
#upper(), lower(), swapcase(), capitalize() (which returns a copy of string in which just the first letter is uppercase), and
#title() (which returns a copy of string in which first letter of each word is uppercase) functions are also useful
#count() function returns the count of a substring in a string

del dict1[9] #del is a keyword
#Only hashable objects can be keys in dictionaries.Most of the immutable types are hashable.Nevertheless, tuples containing mutable types are not hashable.

dict1 |= {10: 100} # | (union) operator is used to sum two dictionaries to make a new one.

#Sets are like dictionaries that only keep keys instead of key-value pairs.
#Therefore, items in a set must be unique and hashable.
#Python’s sets also implement operations from the original mathematical sets, including union, intersection, difference, and symmetric difference.

#When a function accepts a mutable type like a list, it should avoid changing it.Because this may cause unexpected results in the user's code.
#It's better to avoid do not accept a specific mutable type, and more significantly DO NOT SET A MUTABLE TYPE AS A DEFAULT ARGUMENT.
#If you do define a mutable default argument, function becomes stateful like generators.Nonetheless, you should avoid.
#To handle this, the default value can be set None and a condition can be added in the function.For example, arg = [] if arg==None 

#Similarly, it's a bad practice to store mutable types in tuples.This can cause problems in the future.

#If you don't want user to add new INSTANCE ATTRIBUTES dynamically, you can set __slots__ to a tuple which contains types only you want.
#Using a list will do the exact same thing because __slots__ is set when class body is processed.
#However, do not use it because user may think they can change __slots__.
#Also, setting __slots__ doesn't prevent adding class attributes and methods dynamically.

#__setattr__ and __delattr__ methods can be overridden to prevent any type of attribute to be set and deleted.(Raising an error is preferable.)
#However, if your attribute is a mutable type like a list, you can change its elements.
#Properties and descriptors are other ways of changing mutability.
#NamedTuples, DataClasses, and Enums are like immutable classes ready to use.

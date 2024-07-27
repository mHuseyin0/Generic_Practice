from collections import namedtuple
from dataclasses import dataclass
from typing import Any
myPointClass = namedtuple('Point','x y z',defaults=[0]) #['x','y'] is also possible
myPointObject = myPointClass(4, 6)
print(myPointObject.x)
print(myPointObject[1])
print(issubclass(myPointClass,tuple))
print(myPointObject._asdict())
myPointObject = myPointObject._replace(x=9)
print(myPointObject)
print(myPointClass._fields)
print(myPointClass._field_defaults)

myPointClass4D = namedtuple('myPointClass4D',[*myPointClass._fields,"t"],defaults=[2,0])

myPoint4D = myPointClass4D(1,2)
print(myPoint4D)

for field, value in zip(myPoint4D._fields,myPoint4D):
    print(field, " = ", value)

@dataclass
class myDataClass:
    field1: str
    field2: Any
    field3: int = 0 #Default parameters always must be at the end in Python.
    
    def dataFunc():
        pass
    #It's possible to define functions.Data classes are normal classes.
#Type hints never enforce to use hinted types.They are just suggestions in Python.
dataObject1 = myDataClass("data1",1)
print(dataObject1.field2)

@dataclass(frozen = True)
class myImmutableClass:
    pass
#Even if namedtuples and frozen data classes are immutable, 
# it's possible to change their mutable fields like lists.
# This is true for all nested data structures in Python.

@dataclass
class parentDataClass:
    attr1: str
    attr2: int = 5

@dataclass
class childDataClass(parentDataClass):
    attr3: float = 9 #Since default values have to be at the end,
                     #all new defining fields MUST HAVE DEFAULT VALUES in child classes
    attr2: str = "xd"

dataObject2 = childDataClass("data2")
print(dataObject2.attr2)
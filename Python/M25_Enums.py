from enum import Enum, IntEnum, StrEnum, IntFlag, Flag

class myEnum(Enum):
    PI = 3.14
    E = 2.718
    C = 3 * (10**5)
    #Enums cannot be instantiated (Cannot create objects from outside or dynamically like normal classes) 
    #One enum can have different data types but it's not recommended due to type safety
    #"pass", "...", or docstring (triple double quotes) can be used in order to create a empty enum
    #Docstring is more recommended in terms of readability
    #Only empty enums can be inherited (Functions doesn't prevent inheritance)

mySecondEnum = Enum(
    "mySecondEnum", ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    #Values will be given automatically by starting from 1.(NOT 0 because of boolean reasons)
)
print(list(mySecondEnum))

myThirdEnum = Enum(
    value="myThirdEnum",
    #names does not have to contain values.In that case enumaration will be start from 1 as usual
    #Also, it's possible to set a starting value mto enumeration through start=200 (will continue: 200-201-202...)
    names = [
        ("First",200),
        ("Second",400),
        ("Third",400)
    ],
    #start = 200
)
print()
print(myThirdEnum.__members__) #Use this to get aliases 
print(list(myThirdEnum))
print()
print(myEnum.E)
print(myEnum.PI.value)
print(mySecondEnum.MONDAY.value)
print(myThirdEnum.First.name)

#Objects which have the same value and different names in the same enum are equal
#Objects which belong to different enums are NOT equal, even if they have the same value and the same name
#Objects are not equal their values (myEnum.PI == 3.14 will return false)
#These all are valid for all "==, !=, is, is not" operators
#All enum objects have differnet id s (id(myEnum.PI) will return the id of an object) 

def dayOfWeek(day):
    match (day):
        case mySecondEnum.MONDAY:
            print("Today is Monday.")
        case mySecondEnum.TUESDAY:
            print("Today is Tuesday.")
        case mySecondEnum.WEDNESDAY:
            print("Today is Wednesday.")
        case mySecondEnum.THURSDAY:
            print("Today is Thursday.")
        case mySecondEnum.FRIDAY:
            print("Today is Friday.")
        case mySecondEnum.SATURDAY:
            print("Today is Saturday.")
        case mySecondEnum.SUNDAY:
            print("Today is Sunday.")

dayOfWeek(mySecondEnum.TUESDAY)

print(myEnum.PI in myEnum)

#How to sort enums according to their names or values:

print(sorted(mySecondEnum, key=lambda day:day.name))

class myIntEnum(IntEnum):#This is equals to (int,Enum). Every object will behave as int, so operators like > >= < <= can be used
    ...
    #When the value of an object cannot be converted to int, python will raise an ValueError
    #"4" is acceptable but "4.p" is not

class myStrEnum(StrEnum):
    """
    This class inherits str and Enum
    """ 

class myFlag(Flag):
    pass
    #These objects will not behave as integers. They cannot be added or subtracted like IntFlag objects

class myNumbers(IntFlag):
    RATIONAL = 1
    IRRATIONAL = 2
    REEL = RATIONAL | IRRATIONAL
    IMAGINARY = 4
    """
    To use this pattern, sets don't have to be discrete. 
    However, their intersection shouldn't produce a new set which has different features from intersecting sets.
    For example, RGB colors are not appropriate for this scheme.
    """

COMPLEX = myNumbers.REEL | myNumbers.IMAGINARY
print(type(COMPLEX)) #COMPLEX object is a member of myNumbers class as well
print(type(myNumbers.IMAGINARY))
print(COMPLEX+1)
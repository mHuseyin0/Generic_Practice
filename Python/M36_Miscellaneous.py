a = [1,2,3,4]
print(all(a))
a = [1,2,3,0]
print(all(a))

b = [0,0,0,1]
print(any(b))
b = [0,0,0,0]
print(any(b))

print(bool(""))

print(bin(-10))

class c():
    pass

def d():
    def e():
        pass
    return e

f = lambda x: x+1

g = "Not Callable"

print(callable(c))
print(callable(d))
print(callable(d()))
print(callable(f))
print(callable(g))

print(chr(233))
print(ord(" "))
print(ord("a"))

print(complex("54+56j"))
print(complex(67,45))

class h():
    def __init__(self):
        self.attr1 = 35

i = h()

print(i.attr1)
delattr(i, "attr1")
#print(i.attr1) will raise an exception

setattr(i, "attr1", 40)
print(getattr(i, "attr1"))
del i.attr1 #Does exact same thing

print(hasattr(i, "attr1"))

print(dir(), end="\n\n")
import time
print(dir(time), end="\n\n")
print(dir(int), end="\n\n")

print(divmod(50,7)) #returns tuple

#exec(input("Please enter a code to execute: ")) #Seperate lines with a semicolon
#Unlike eval() function, using exec(), it's possible to execute statements, not just expresssions.For example, assigning values. 
#Sample input to exec():
#Please enter a code to execute: x = 10;y = input("Please input something to add to x: ");print(x+int(y))

#subprocess.run(filePath) or os.startfile(filePath) can be used to execute an exe. The former is better.

print(float("-inf"))
print(float(5))

print(format(7,"b")) #binary value

print(globals())

#help(float)

print(hex(0)) #Hexadecimal representation of an integer
print(oct(0)) #Octal representation of an integer

j = 10
k = j
l = k + 5 - 5

print(id(j))
print(id(k))
print(id(l))

print(locals() == globals())
print(__file__)
print(locals()["__file__"]) #locals() returns a dictionary

seperator = "-"

stringsToJoin = ("1","2","3","4","5") #That must be an iterable

print(seperator.join(stringsToJoin))
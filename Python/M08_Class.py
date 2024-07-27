from typing import Any


class Rectangle:
    def __init__(self,c,l,w):
        self.color=c
        self.length=l
        self.width=w
    def area(self):
        self.area=self.length*self.width
        return self.area
    def per(self):
        self.perimeter=2*(self.length+self.width)
        return self.perimeter
    def diagonal(self):
        self.diag=(self.length**2+self.width**2)**(1/2)
        return self.diag
    def volume(self,h):
        self.height=h
        self.vol=self.area*self.height
        return self.vol
        
myRect1=Rectangle('green',3,4)
myRect2=Rectangle('blue',5,12)

print(myRect1.color)
print(myRect1.area())
print(myRect1.per())
print(myRect1.diagonal())
print(myRect1.volume(5))
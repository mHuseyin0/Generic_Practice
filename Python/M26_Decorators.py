from functools import wraps
from random import randint
from time import perf_counter
def repeatFunc(times):
    def decoratorRepeat(func):
        @wraps(func)
        def wrapperRepeat(*args, **kwargs):
            values = []
            for _ in range(times):
                value = func(*args, **kwargs)
                values.append(value)
            return values
        return wrapperRepeat
    return decoratorRepeat

@repeatFunc(5)
def func(min, max=1000):
    a = randint(min, max)
    return a

#func = repeatFunc(5)(func)

print(func(100,180))

class Decorator():
    def __init__(self,objID: int):
        self.objID = objID
    def __call__(self, func):
        if self.objID == 1:
            def startFinish(*args, **kwargs):
                print("Starting to execute " + func.__name__)
                func(*args, **kwargs)
                print("Finished to execute " + func.__name__)
            return startFinish
        if self.objID == 2:
            def executeTime(*args, **kwargs):
                start = perf_counter()
                func(*args, **kwargs)
                time = perf_counter() - start
                print(time)
            return executeTime



decorator1 = Decorator(1)
decorator2 = Decorator(2)

@decorator2
def testFunc(*args):
    a = sum(args)
    print(a)
    return a

testFunc(8,9)
import time
import pickle
import random

testList = list()

currentTime = time.perf_counter()
for i in range(1000):
    a = random.random()
    b = random.random()
    c = random.random()
    testList.append(tuple([a,b,c]))

with open("PickleTest1Dump.pkl", "ab") as file:
    pickle.dump(testList, file)
del testList
currentTime = time.perf_counter() - currentTime

print(f"Dumping 1 time completed in {currentTime} seconds.")

testList = list()

currentTime = time.perf_counter()
for i in range(1000):
    a = random.random()
    b = random.random()
    c = random.random()
    testList.append(tuple([a,b,c]))
    if ((i + 1) % 200) == 0:
        with open("PickleTest5Dumps.pkl", "ab") as file:
            pickle.dump(testList, file)
        testList = list()

del testList
currentTime = time.perf_counter() - currentTime

print(f"Dumping 5 times completed in {currentTime} seconds.")




testList = list()

currentTime = time.perf_counter()
for i in range(1000):
    a = random.random()
    b = random.random()
    c = random.random()
    testList.append(tuple([a,b,c]))
    if ((i + 1) % 100) == 0:
        with open("PickleTest10Dumps.pkl", "ab") as file:
            pickle.dump(testList, file)
        testList = list()

del testList
currentTime = time.perf_counter() - currentTime

print(f"Dumping 10 times completed in {currentTime} seconds.")


currentTime = time.perf_counter()
testList = list()

for i in range(1000):
    a = random.random()
    b = random.random()
    c = random.random()
    testList.append(tuple([a,b,c]))
    if ((i + 1) % 10) == 0:
        with open("PickleTest100Dumps.pkl", "ab") as file:
            pickle.dump(testList, file)
        testList = list()

del testList
currentTime = time.perf_counter() - currentTime

print(f"Dumping 100 times completed in {currentTime} seconds.")

currentTime = time.perf_counter()
for i in range(1000):
    a = random.random()
    b = random.random()
    c = random.random()
    with open("PickleTest1000Dumps.pkl", "ab") as file:
        pickle.dump(tuple([a,b,c]), file)
currentTime = time.perf_counter() - currentTime

print(f"Dumping 1000 times completed in {currentTime} seconds.")

print()

currentTime = time.perf_counter()
with open("PickleTest1Dump.pkl", "rb") as file:
    list1 = pickle.load(file)
currentTime = time.perf_counter() - currentTime
print(f"Loading 1 time completed in {currentTime} seconds.")

currentTime = time.perf_counter()
list5 = list()
with open("PickleTest5Dumps.pkl", "rb") as file:
    for i in range(5):
        list5.append(pickle.load(file))
currentTime = time.perf_counter() - currentTime
print(f"Loading 5 times completed in {currentTime} seconds.")

currentTime = time.perf_counter()
list10 = list()
with open("PickleTest10Dumps.pkl", "rb") as file:
    for i in range(10):
        list10.append(pickle.load(file))
currentTime = time.perf_counter() - currentTime
print(f"Loading 10 times completed in {currentTime} seconds.")

currentTime = time.perf_counter()
list100 = list()
with open("PickleTest100Dumps.pkl", "rb") as file:
    for i in range(100):
        list100.append(pickle.load(file))
currentTime = time.perf_counter() - currentTime
print(f"Loading 100 times completed in {currentTime} seconds.")

currentTime = time.perf_counter()
list1000 = list()
with open("PickleTest1000Dumps.pkl", "rb") as file:
    for i in range(1000):
        list1000.append(pickle.load(file))
currentTime = time.perf_counter() - currentTime
print(f"Loading 1000 times completed in {currentTime} seconds.")

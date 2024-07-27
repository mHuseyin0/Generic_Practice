from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import math

def func(l):
     return np.float64(2 * math.pi * math.sqrt(l/9.8))

stringLengths = [round(i,2) for i in linspace(0.05, 0.25, 5)]
measuredPeriods = [.67, .83, .92, 1, 1.13]
expectedPeriods = [.45, .63, .78, .9, 1]

for i in range(5):
    measuredPeriods[i] = np.float64(measuredPeriods[i])

axisLimit = np.linspace(0, 1.2, 200)
fig, ax = plt.subplots()
#ax.plot(axisLimit, axisLimit)

plt.scatter(stringLengths, measuredPeriods)
plt.plot(linspace(0, .25, 200), [func(i) for i in linspace(0, .25, 200)], label="Expected", color="black")

model1 = np.poly1d(np.polyfit(stringLengths, measuredPeriods, 1))
model2 = np.poly1d(np.polyfit(stringLengths, measuredPeriods, 2))
model3 = np.poly1d(np.polyfit(stringLengths, measuredPeriods, 3))
model4 = np.poly1d(np.polyfit(stringLengths, measuredPeriods, 4))
model5 = np.poly1d(np.polyfit(stringLengths, measuredPeriods, 5))

polyline = np.linspace(0, .25, 300)

plt.plot(polyline, model3(polyline), label="Measured", color='blue')

plt.title("Period of a Simple Pendulum Depending on the Length of Oscillating String")
plt.xlabel("String Length (m)")
plt.ylabel("Pendulum Period (s)")

plt.legend()
plt.grid()
plt.show()

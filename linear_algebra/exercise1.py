import math 
import numpy as np
#1-a
def function1():
    value=0
    for i in range(1,1000+1):
        value+=i
    return value

#1-b
def function2(m):
    value=0
    for i in range(1,m+1):
        value+=i
    return value
    
#2
def function3():
    value=0
    for i in range(1,100+1):
        value+=math.sqrt(i*math.pi/100)*math.sin(i*math.pi/100)
    return value

print(function1())
print(function2(1000))
print(function3())
# 500500
# 500500
# 77.51389798916512

#oriented object programming
class physic_calculation:
    def __init__(self):
        pass

    def function_a(self):
        value1=0
        for i in range(1,1000+1):
            value1+=i
        return value1

    def function_b(self,m):
        self.m=m
        value2=0
        for i in range(1,self.m+1):
            value2+=i
        return value2

    def function_c(self):
        value3=0
        for i in range(1,100+1):
            value3+=math.sqrt(i*math.pi/100)*math.sin(i*math.pi/100)
        return value3

pc=physic_calculation()
print("---------------OOP----------------")
print(pc.function_a())
print(pc.function_b(1000))
print(pc.function_c())
# 500500
# 500500
# 77.51389798916512

print("---------------numpy----------------")
a=np.arange(1,26).reshape(5,5)
print(a)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
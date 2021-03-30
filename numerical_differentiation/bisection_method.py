import numpy as np 
import matplotlib.pyplot as plt 


def f(x):
    return (x**2)-3*x-10


# a:left bound
# b:right bound
# eps: the distance between a and b
def bisection(a,b,eps):
    #calculate the iteration time
    iteration=0
    while(1):
        x_0=0.5*(a+b)
        if f(a)*f(x_0)<0:
            b=x_0
        else:
            a=x_0
        
        iteration+=1

        if abs(a-b)<eps:
            break

    return a, iteration

root,iteration=bisection(4.2,6.5,0.0000001)


#to generate the different eps
error=[]
for i in range(5,15):
    error.append((10**-i))

      
#to stroe the different iteration with the different eps
iteration_eps=[]

#to store the root of different eps
root=[]

for i in error:
    rt,it=bisection(4.2,6.3,i)
    root.append(rt)
    iteration_eps.append(it)


plt.plot(error,iteration_eps)
plt.show()
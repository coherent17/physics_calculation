import numpy as np
import matplotlib.pyplot as plt

N=11
x=np.linspace(0,10,N)
y=np.linspace(0,10,N)
xx,yy=np.meshgrid(x,y)


#BC
V=np.zeros((11,11),dtype=float)

#set the plate capacitor voltage as constant
for i in range(1,N-1):
    for j in range(1,N-1):
        if j==3 and i>=3 and i<=7:
            V[j,i]=1
        elif j==7 and i>=3 and i<=7:
            V[j,i]=-1

V_old=V
#update the voltage by relaxation method
iteration=0
while(True):
    V_new=V_old
    for i in range(1,N-1):
        for j in range(1,N-1):
            #setting the parallel plate capacitor as the constant
            if j==3 and i>=3 and i<=7:
                continue
            elif j==7 and i>=3 and i<=7:
                continue
            #relaxation method to solve the pde
            else:
                V_new[j,i]=0.25*(V_old[j,i-1]+V_old[j-1,i]+V_old[j+1,i]+V_old[j,i+1])
    iteration+=1
    #setting the condition to break the while loop
    # #check the error before and after the iteration
    if iteration%5==0: #per 5 loops to check the error
        error=np.zeros((N,N),dtype=float)
        error=abs(V_new-V_old)
        print(error)
        if error.all()<=0:
            print(iteration)
            break
        else:
            V_old=V_new

#visualize
fig=plt.figure(figsize=(18,6))
ax=fig.add_subplot(121)
z=V_new
plt.contourf(xx,yy,z,cmap='rainbow',levels=51)
plt.colorbar()
ax.set_title('V plane contour')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax1=fig.add_subplot(122)
ax1.plot(x,V[:,3])
plt.show()   
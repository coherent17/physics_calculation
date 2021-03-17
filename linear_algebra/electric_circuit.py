import numpy as np

A=np.array([[1,-1,1]
           ,[-1,1,-1]
           ,[4,2,0]
           ,[0,2,5]])

B=np.array([[0]
           ,[0]
           ,[8]
           ,[9]])


#if there is any row filling with 0 
#delete it
def del_zero(A,B):
    zero_row=[]
    for i in range(0,len(A)):
        flag=0
        for j in range(0,np.shape(A)[1]):
            if A[i,j]==0:
                flag+=1
        if flag==np.shape(A)[1]:
            zero_row.append(i)
    A=np.delete(A,zero_row,axis=0)
    B=np.delete(B,zero_row,axis=0)
    return A,B

def GE(A,B):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[j,i]!=0:
                lam=A[j,i]/A[i,i]
                A[j,:]=A[j,:]-lam*A[i,:]
                B[j]=B[j]-lam*B[i]
                A,B=del_zero(A,B)
                break
        else:
            continue
        break
        
    print(np.c_[A,B],"\n")
    return A,B

#back substitution
def BS(A,B):
    sol=np.zeros((len(A)))
    sol[len(A)-1]=B[len(A)-1]/A[len(A)-1,len(A)-1]

    for i in range(len(A)-2,-1,-1):
        sol[i]=(B[i]-np.dot(A[i,i+1:len(A)],sol[i+1:len(A)]))/A[i,i]
    # sol[1]=(B[1]-A[1,2]*sol[2])/A[1,1]
    # sol[0]=(B[0]-A[0,2]*sol[2]-A[0,1]*sol[1])/A[0,0]
    for j in range(0,len(A)):
        print("i_",j+1,"=",sol[j],end="   ")
    print("\n")

#avoid the original A matrix has invalid value
A,B=del_zero(A,B)

#keep doing GE until the matrix are all the same
for _ in range(1000):
    A,B=GE(A,B)
    C=np.c_[A,B]
    A,B=GE(A,B)
    D=np.c_[A,B]
    if (C==D).all():
        break

BS(A,B)
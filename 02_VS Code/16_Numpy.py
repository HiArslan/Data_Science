import numpy as np
#1-D arrays
a=np.array([1,2,3,4,5])
print(a)
#2-D arrays
b=np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
print(b)
# With specific range
c=np.arange(1,20)
print(c)
# With specific range and intervals
d=np.arange(1,20,2)
print(d)
e=np.ones(5)
print(e)
f=np.zeros(5)
print(f)
g=np.linspace(1,20,num=5)
print(g)
#Like Matrices
h=np.ones((5,6)) 
print(h)
i=np.zeros((5,6))
print(i)
# 3-D arrays
j=np.arange(24).reshape(2,3,4)
print(j)




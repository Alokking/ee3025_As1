import numpy as np
import matplotlib.pyplot as plt
X=np.array([1,1,2,4,3,1])
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
X=np.pad(X,(0,20-len(X)),'constant')
a=np.arange(20)
Y=np.zeros(20)
for i in range(20):
	Y[i]=X[i]+X[i-2]-0.5*Y[i-1]
plt.figure(1)
plt.ylabel("X(n)")
plt.xlabel("n")
plt.title("Input")
plt.stem(a,X)
plt.axis([-5,20,-1,4.5])
plt.grid()
plt.figure(2)
plt.ylabel("Y(n)")
plt.xlabel("n")
plt.title("Output")
plt.stem(a,Y)
plt.axis([-5,20,-1,4])
plt.grid()
plt.show()

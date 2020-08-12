import numpy as np
a=np.random.dirichlet(np.ones(200))*100000
# print(a)
sum=0
for i in a:
    print(int(i))
    sum=sum+int(i)
print(sum)
#%%
import math
from operator import imod
print(math.sqrt(25))
#%%
import math as m 
print(math.floor(2.7)) #returns smaller integer
print(math.ceil(2.7))  #returns greatest integer

#%%
from math import pow,sqrt,cos
print(sqrt(36))
print(pow(2,8))
print(cos(45))
#print(help('math'))

#%%
#To check number prime or not
num =11
for i in range(2,num):
    if num%i==0:
        print("Number is Non-prime")
        break
else:
    print("Number is prime")
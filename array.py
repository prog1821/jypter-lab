from array import *
nums=array('i',[])
n=int(input("enter the number : "))


for i in range(n) :
    x=int(input("enter the value : "))
    nums.append(x)
k=0
e=int(input("enter the number to search : "))
for i in range(n) :
    if nums[i]==e :
        print(k)
        break
    k=k+1
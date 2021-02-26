from functools import reduce

lst=[]

n=int(input("enter the number of elements : "))

for i in range(n) :
    k=int(input())
    lst.append(k)

even=list(filter(lambda i : i%2==0,lst))

add=list(map(lambda k : k+2,lst))

sum=reduce(lambda a,b :a+b,lst )
print(sum)

print(add)

print(even)


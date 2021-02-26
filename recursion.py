def fact (n) :

    if n==0 :
        return 1


    return n*fact(n-1)

m=int(input("enter the number : "))
result=fact(m)
print(result)
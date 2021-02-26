
def count(lst):
    even =0
    odd=0
    for i in lst :
        if i%2==0 :
            even=even+1
        else :
            odd=odd+1

    return even,odd







lst=[12,13,16,54,22,56,43,445,333,5667]
even,odd=count(lst)
print("even : {} and odd : {} ".format(even,odd))
print(even)
print(odd)
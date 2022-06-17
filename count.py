def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
lst=[2,3,4,5,6,785,453,34,65,7,43,3,658,34]
even,odd=count(lst)
print(even)
print(odd)
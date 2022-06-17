from functools import reduce


num=[1,2,3,4,5,6]

evens= list(filter(lambda e : e%2==0, num))
print (evens)

odds= list(filter(lambda o : o%2!=0, num))
print(odds)
##
evendouble=list(map(lambda e:e*2,evens))
print(evendouble)

oddtriple=list(map(lambda o:o*3,odds))
print(oddtriple)
##
sumeven= reduce(lambda a,b:a+b,evendouble)
print(sumeven)

sumodd= reduce(lambda a,b:a+b,oddtriple)
print(sumodd)
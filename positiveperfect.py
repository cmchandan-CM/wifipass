def positive(value):
    m=(value/2)
    s=0
    for i in range(int(m)):
        if(value%(i+1)==0):
           s+=(i+1)
    return s
no=int(input("enter the value for find positive perfect number   :"))
j=positive(no)
if(no==j):
    print("yes")
else:
    print("no")
list=[]
str2=""
dict1={1:{'a','b'},2:{'c','d'}}
n=int(input("enter key value n"))
k=int(input("enter key value n"))
for i in dict1[n]:
    for j in dict1[k]:
        str2=i+j
        list.append(str2)
for i in range(len(list)):
    print(list[i])
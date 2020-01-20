name=input("enter name : ")
date=input("enter date of birth ddmmyyyy : ")
wifi=[]
def split(word):
    return [char for char in word]

li=split(date)
add=0
for i in range(len(date)):
    add=add+int(li[i])
td=add
def adds(td):
    f=0
    while td > 0:
       su = int(td) % 10
       f = f + int(su)
       td = int(td)/ 10
    return int(f)
f1=0
while td>9:
    td=adds(td)
g4=str(td)
wifi.append(g4)
print(wifi)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@end@@@@@@@@@@@@@@@@@@@@@@dob
fact=0
g=len(name)
if(g>9):
   while g>=0 :
    fact=fact+g
    g=g-1
   #print(f"total indaex number =={fact}")
   while fact>9:
     fact=adds(fact)
   wifi.append(fact)
else:
    wifi.append(9)
print(wifi)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@even odd @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 #name="chandan kashyap"
st=split(name)
st.remove(' ')
list=[]
for i in range(len(st)):
    if i%2==0 :
        list.append(st[i])
list.sort()
wifi.append(list[0])
print(wifi)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@special character used
sc=['!','@','#','$','%','^','&','*','(']
le=len(name)
while le>9 :
    le=adds(le)
wifi.append(sc[le-1])
print(wifi)
print("wifi password generate successful")
str1=""
for i in range(len(wifi)):
    str1+=str(wifi[i])
print(str1)




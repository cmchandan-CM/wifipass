dict={
    'empno':[1001,1002,1003,1004,1005,1006,1007],
    'empnam':['ashish','sushma','rahul','chahat','ranjan','suman','tanmay'],
    'descd':['e','c','k','r','v','e','c'],
    'department':['r&d','pm','account','front_desk','engg','manufacturing','pm'],
    'basic':[20000,30000,10000,12000,50000,23000,29000],
    'hra':[8000,12000,8000,6000,20000,9000,12000],
    'it':[3000,9000,1000,2000,20000,4400,10000]
}
dict1={
    'desc':{'e':20000,'c':32000,'k':12000,'r':15000,'m':40000},
    'designation':['engineer','consultant','clerk','receptionist','manager']
}
val=input("enter the designation code")
list=dict['descd']
temp=[]
for i in range(len(list)):
    if(list[i]==val):
        temp.append(i)
for i in range(len(temp)):
    sum = 0
    sum = dict["hra"][temp[i]] + dict["basic"][temp[i]] + dict["it"][temp[i]]+dict1["desc"][val]
    print(f"EMPLOYEE NUMBER = {dict['empno'][temp[i]]},NAME = {dict['empnam'][temp[i]]},DEPARTMENT={dict['department'][temp[i]]},HRA={dict['hra'][temp[i]]},BASIC={dict['basic'][temp[i]]},IT={dict['it'][temp[i]]},DA={dict1['desc'][val]},NET SALARY={sum}")



# list1=dict['empno']
# list2=dict['empnam']
# list3=dict['department']
# list4=dict['basic']
# list5=dict['hra']
# list6=dict['it']
# listp=[]
# ttl=0
# for i in range(len(temp)):
#     k=temp[i]
#     ttl=list5[int(k)]+list4[int(k)]+list6[int(k)]+dict1["desc"][val]
#     listp.append(ttl)
#
# print(ttl)
# print(listp)

def leap(val):
    if(val%4==0):
        return True
    else:
        return False

dob=input("Enter from_date in format:dd/mm/yy :")
today=input("Enter to_date in format:dd/mm/yy :")
dbl=dob.split('/')
tdl=today.split('/')
day=int(dbl[0])
mnth=int(dbl[1])
year=int(dbl[2])
tdl=today.split('/')
day2=int(tdl[0])
mnth2=int(tdl[1])
year2=int(tdl[2])
sum=0
dict={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict1={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
k = mnth
u=mnth+1
i=1
dm=0
if (year==year2):
    if(mnth==mnth2):
        sum += day2-day
    else:
        if (leap(year)):
            sum += dict[mnth] - day
            while u < mnth2:
                sum += dict[u]
                u+=1
        else:
            sum += dict1[mnth] - day
            while u < mnth2:
                sum += dict[u]
                u+=1
        sum += day2
    print(f"month  : {mnth2-mnth} days : {sum%30}")
    print(f"days  :{sum}")
    print(f"week   :{int(sum/7)} days  : {int(sum%7)}")

else:
    if (leap(year)):
        dm = (dict[mnth] - day)
        sum += dict[mnth] - day
        while k < 12:
            sum += dict[k + 1]
            k += 1
    else:
        dm = (dict1[mnth]) - day
        sum += dict1[mnth] - day
        while k < 12:
            sum += dict1[k + 1]
            k += 1

    if (leap(year2) == 1):
        sum += day2
        while i < mnth2:
            sum += dict[i]
            i += 1
    else:
        sum += day2
        while i < mnth2:
            sum += dict1[i]
            i += 1
    i = year + 1
    while i < year2:
        if (leap(i) == 1):
            sum += 366
            i += 1
        else:
            sum += 365
            i += 1
    uj = ((year2 - 1) - year) * 12 + (12 - mnth) + (mnth2 - 1) + (int((dm + day2) / 31))
    dj = (int((dm + day2) % 30))
    print(f"total year  ===== {int(uj / 12)}   Month ==== {int(uj % 12)}  Days ==== {dj} ")
    print(f"OR  total Month ===== {int(uj)},     Days  ==== {dj}                          ")
    print(f"OR  total week  ===== {int(sum / 7)},  Days  ==== {int(sum % 7)}                  ")
    print(f"OR  total days  ===== {sum}                                                  ")
    print(f"OR    hour        ===== {sum * 24}     minute  ==== {sum * 24 * 60}   second =====  {sum * 24 * 60 * 60}")


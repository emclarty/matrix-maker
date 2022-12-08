# first, generate random order list from 0-11, inclusive

from random import shuffle
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
shuffle(list1)


I_n = list1[0]*2 %12
n =0
list_i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    list_i[n]=(I_n-x)%12
    n=n+1
m=1

n=0
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list2[n] = (T_n+list1[n])%12
    n=n+1
m=m+1

n=0
list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list3[n] = (T_n+list1[n])%12
    n=n+1
m=m+1

n=0
list4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list4[n] = (T_n+list1[n])%12
    n=n+1
m=m+1

n=0
list5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list5[n] = (T_n+list1[n])%12
    n=n+1
m=m+1

n=0
list6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list6[n] = (T_n+list1[n])%12
    n=n+1
m=m+1
n=0
list7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list7[n] = (T_n+list1[n])%12
    n=n+1
m=m+1
n=0
list8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list8[n] = (T_n+list1[n])%12
    n=n+1
m=m+1
n=0
list9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list9[n] = (T_n+list1[n])%12
    n=n+1
m=m+1
n=0
list10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list10[n] = (T_n+list1[n])%12
    n=n+1
m=m+1
n=0
list11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list11[n] = (T_n+list1[n])%12
    n=n+1
m=m+1
n=0
list12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in list1:
    T_n = list_i[m]-list1[0]
    list12[n] = (T_n+list1[n])%12
    n=n+1
m=m+1

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)
print(list11)
print(list12)

print(I_n)
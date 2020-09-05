print('list intro')
list_mon_an = ['thit cho ','thit meo','bun cha']
#mon_an_moi=input()
#list_mon_an.append(mon_an_moi)
#list_mon_an.append('thit ga')#CREATE
#mon_thit_cho = list_mon_an[0]
#print(mon_thit_cho)
length = len(list_mon_an)
print(length)
for i in range(length):
    print(i,list_mon_an[i])
print('___')
#for item in list_mon_an:
for index ,item in enumerate(list_mon_an):
    print(item)

list_mon_an[0]="cho thit"#UPDATE
list_mon_an.remove('cho thit') #DELETE BY VALUE
list_mon_an.pop(0) #DELETE BY INDEX
list_mon_an.pop(0) #DELETE BY INDEX
print(list_mon_an)



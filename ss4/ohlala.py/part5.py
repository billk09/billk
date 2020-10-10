#1
a=['ST','BĐ','BTL','CG','ĐĐ','HBT']
b=[150300,247100,333300,266800,420900,318000]
print(a)
print(b)
#2
print('Dan so lon nhat :',b.index(max(b)))
print('Dan so be nhat:',b.index(min(b)))
# 3
c=int(b.index(max(b)))
print('Lon nhat la:',a[c])
d=int(b.index(min(b)))
print('Be nhat la:',a[d])

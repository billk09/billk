#1
user = ['blue','red','green']
#x = int(input("vi tri :"))
#userout = user[x]
#print(userout)

#2
#x = input("Muon xoa:")
#user.remove(x)
#print(user)
#x = int(input("Muon xoa:"))
#user.pop(x)
#print(user)

#3
from turtle import*
for i in range(len(user)):
    pencolor(user[i])
    forward(100)

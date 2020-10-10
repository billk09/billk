#1
x = [12,54,67,89,80]

#for num in x :
  #  if num %2 ==0 :
  #     print(num, end=",")

#2
b= input("Enter number :")
a=b.split(',')
for item in a :
  if int(item)%2 !=0:
    a.remove(item)
print("All even numbers are:")
for i in range (len(a)):
  print(a[i], end=",")




from math import sqrt
#a=23
#b=int(input("Enter your number :"))

#if b >a :
   # print("b greater than a")
#else:
   # print("b less than a")
#age= int(input("How old are u?="))
 
#if age <=6:
 #   print("Baby")
#elif 7<=age<=12 :
  #  print("Kids")
#elif 13<=age<=17:
  #  print("Teen")
#else:
    #print("Aldult")

a=int(input("Nhap canh ="))
c=int(input("Nhap canh ="))
b=int(input("Nhap canh ="))

p=(a+b+c)/2


if a==b or a==c or b==c:
    print("tam giac can")
    s1=sqrt(p*(p-a)*(p-b)*(p-c))
    print(s1)
elif (a**2) +(c**2)==(b**2):
    print("tam giac vuong")
    s2=1/2*(a*c)
    print(s2)
elif  a==b==c:
    print("tam giac deu")
    s1=sqrt(p*(p-a)*(p-b)*(p-c))
    print(s1)
else :
   print("tam giac thuong")
   s3=sqrt(p*(p-a)*(p-b)*(p-c))
   print(s3)

print("Thank you")




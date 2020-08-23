#3.1
#n = int(input("Nhap so :"))
#if n >13:
 #   print("n lon hon 13")
#elif n<13:
  #  print("n be hon 13")
#else :
  #  print("n la 13")

#3.2
#n = int(input("Nhap so n :"))
#if n % 2 == 0 :
   # print("n la so chan")
#else :
   # print("n la so le")

#3.3
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
user = int(input("Enter month :"))
if user in a :
    print("thang", user ,"co 31 ngay")
elif user in b :
    print("thang", user, "co 30 ngay")
elif user > 12 :
    print("thang",user,"khong ton tai")
elif user <1:
    print("thang",user,"khong ton tai")
else :
    print("thang", user, "co 28 ngay")
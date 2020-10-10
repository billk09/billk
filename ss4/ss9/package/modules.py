#1
# a =int(input("So thu nhat :"))
# b = int(input("So thu hai:"))

def sosanh(number1,number2):
  if number1 > number2 :
      print("So thu nhat lon hon so thu hai")
  elif number1 <number2 :
      print("So thu nhat nho hon so thu hai")
  else :
      print("Hai so bang nhau")

#2
a = int(input("Nhap mot so:"))
def chanle():
     if a %2 == 0 :
       print("La so chan")
     else:
       print("La so le")

chanle()
#3
a = int(input("Nhap mot nam :"))

def kiemtranam():
    if a %4 == 0 :
        print("Day la nam nhuan")
    else :
        print("Day khong la nam nhuan")

kiemtranam()

#4
listnumber = [12,46,True,'C4T',100]
result = 0
def Tongdayso():
  for numb in listnumber:
     if type(numb) is int :
      result += numb 
print(result)

#5
def converstStringToList(text):
    result = text.split(',')
    result.sort()
    return result



userinput = input("Enter everythings:")

lastresult = converstStringToList(userinput) 

print(lastresult)

if __name__ == "__main__":
    sosanh()
    # chanle()
    # kiemtranam()
    # Tongdayso()
    # converstStringToList(text)

    







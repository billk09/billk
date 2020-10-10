from turtle import*
#userInput = int(input("Nhap so vong tron ban muon ve :"))
#speed(-1)

#def drawTimesCircle(times):
  #  for i in range(userInput):
   #     circle(100)
   #     left(i*10)




#drawTimesCircle(userInput)

#mainloop()

#Hoi nguoi dung la hinh ve nguoi ta muon ve hinh gi ? va so luong hinh ma nguoi dung muon ve
userInput = input("Muon ve vuong hay tron :")
a = int(input("Ve bao nhieu hinh:"))
speed(-1)
if userInput == "vuong" :
    for x in range(a):
        for i in range(4):
            forward(100)
            left(90)
        left(10)
elif userInput == "tron":
    b = int(input("Ban kinh :"))
    for i in range(a):
      circle(b)
      left(b*10)
        
            

mainloop()
        
        


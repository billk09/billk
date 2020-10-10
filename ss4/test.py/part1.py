#1.1
computer = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
print(computer)
#1.2
print("So luong MACBOOK co trong kho:",computer["MACBOOK"])
#1.3
userInput = input("Nhap hang may:")
if userInput in computer:
    print("So luong co trong kho:",computer[userInput])
else:
    print("khong co")
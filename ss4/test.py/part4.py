#4.1
computer = {
    "HP":600,
    "DELL":650,
    "MACBOOK":12000,
    "ASUS":400,
    "ACER":350,
    "FUJITSU":900,
    "ALIENWARE":1000
}
print(computer)
#4.2
print(computer["ACER"])
#4.3
a = input("Nhap hang may:")

if a in computer:
    print("So luong co trong kho:",computer[a])

else:
    print("khong co")
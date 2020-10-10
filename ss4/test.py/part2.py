#2.1
computer = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
    }

computer.update({'TOSHIBA':10})
print(computer)
#2.2
a = input("Nhap hang may:")
b = int(input("Nhap so luong:"))

computer.update({a:b})
print(computer)
#2.3
computer["DELL"] += 10
print(computer)

computer["MACBOOK"] -= 10
print(computer)
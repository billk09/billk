#3.1
computer = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
for key,value in computer.items():
    print(key,":",value)
#3.2
a=sum(computer.values())
print(a)
#3.3
computer.update({'FUJITSU':15,'ALIENWARE':5})
print(computer)
#3.4
b=sum(computer.values())
print(b)

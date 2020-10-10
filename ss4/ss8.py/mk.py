#function

myList = ["Mom","Me","Dad"]

def reverserList():
    print("Hello World")
    print("My family",myList)
    return myList

reverserList()

def checkage(age):
    if (0<age<6):
        return("Baby")
    elif (7<age<15):
       return("Children")
    elif (16 <age<18):
        return("Teen")
    else:
        return("Aldult")
yourAge = int(input('Enter your age:'))
result = checkage(yourAge)

print('Hello ' + result)


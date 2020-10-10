def converstStringToList(text):
    result = text.split(',')
    result.sort()
    return result



userinput = input("Enter everythings:")

lastresult = converstStringToList(userinput) 

print(lastresult)

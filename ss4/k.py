books = [
    "Books 1","Harry Potter","Romeo and juliet","Su tich cay khe","Thach Sanh"
    ]

while True :
   userInput = input("Enter here:")
    #for book in books:
     #   if userInput == book.lower() :
     #       print(book)
     #        break
     #  else:
     #      print("Not found")

   if userInput in books :
      index= books.index(userInput)
      print(books[index])
      break
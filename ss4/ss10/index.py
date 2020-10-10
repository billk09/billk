from tkinter import *
from tkinter import messagebox
#from turtle import*
window = Tk()


def popupmessagebox():
    print('username')


def validateinfo():
    username = userInput.get()
    psw = passwordInput.get()
    result = ''
    if (username == 'mindx'):
        if(psw == '1234'):
            result = "success"
        else:
            result = "cannot found"
    showresult(result)


def showresult(result):
    resultlabel = Label(text=result)
    resultlabel.grid(row=4, column=1)
# window.geometry("800x600")


window.title('From Sign In / Sign Up')

greeting = Label(text="Welcome to my app", bg="red")
greeting.grid(row=0, column=12)

btnSignIn = Button(text="Sign in", bg="pink", padx="16",
                   pady="8", command=lambda: [validateinfo()])
# TODO : Click button to sign in =>Popup message "You have clicked"
userlabel = Label(window, text="username")
userInput = Entry(window, textvariable=StringVar())
userlabel.grid(row=1, column=0)
userInput.grid(row=1, column=1)

passwordlabel = Label(window, text="password")
passwordInput = Entry(window, show="*")
passwordInput.grid(row=2, column=1)
passwordlabel.grid(row=2, column=0)

btnSignIn.grid(row=3, column=12)


window.mainloop()

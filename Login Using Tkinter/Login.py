import tkinter
from tkinter import *


def loginUser():
    name = str(username.get())
    password = str(Password.get())
    if name =='Jawad Ahmed' and password=='Bscs201959':
        root.destroy()
        print('Successfully Login')
        welcome=Tk()
        welcome.geometry("450x230")
        welcome.title('Welcome')
        newLabel=Label(welcome,text="Welcome Jawad Ahmed!")
        newLabel.pack(pady=30)
        welcome.mainloop()
    else:
        
        wrongPassword=Label(root,text="Try Again!!!!")
        wrongPassword.place(x='230', y='125')


root=tkinter.Tk()

root.title("Login Form")
root.geometry("450x230")
usernameLable=Label(root,text="Username: ")
usernameLable.place(x='70',y='50')


passwordLable=Label(root,text="Password: ")
passwordLable.place(x='70',y='80')

username=StringVar()
usernameBox=Entry(root,width='30',textvariable=username)
usernameBox.place(x='150',y='50')

Password=StringVar()
passwordBox=Entry(root,width='30',textvariable=Password)
passwordBox.place(x='150',y='80')

loginButton = Button(root, text="Login", command=loginUser)
loginButton.place(x='150', y='120',width='60')
root.mainloop()





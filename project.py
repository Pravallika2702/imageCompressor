from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import PIL
from PIL import Image,ImageTk
from tkinter.filedialog import *

root = Tk()
root.title("Image Compressor")
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

class ImageCompressor:
    def __init__(self, root):
        self.root=root
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()
        self.NAME = StringVar()
        self.Gmail = StringVar()
        
    def Show(self):
        a= Label(self.root, text="IMAGE COMPRESSOR",foreground="purple", width=30,font=("Times New Roman",26))  
        a.place(x=25, y=40)  

        b= Label(self.root, text="Click on upload to insert image",foreground="blue", width=40,font=("arial",12))  
        b.place(x=130, y=230)       
        btn=Button(self.root,text="Upload",bg="lightgreen", width=10,font=("arial",20))
        btn.place(x=220, y=280)
        btn.bind("<Button>",lambda event: self.logic())   
        def logic(self):
            file_path = askopenfilename()
            img = PIL.Image.open(file_path)
            myHeight, myWidth = img.size
            img = img.resize((myHeight, myWidth) , PIL.Image.LANCZOS)
            save_path = asksaveasfilename()
            img.save(save_path+" compressed.JPG")
            

    
    def Database(self):
        global cursor, con
        con = sqlite3.connect('data1.db')
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL,password TEXT NOT NULL,name TEXT NOT NULL,gmail TEXT NOT NULL)''')
    def Exit(self):
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()
    def LoginForm(self):
        width = 640
        height = 480
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        global LoginFrame, result
        LoginFrame = Frame(root)
        LoginFrame.pack(side=TOP, pady=80)
        lbl = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl.grid(row=1)
        lb = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lb.grid(row=2)
        result = Label(LoginFrame, text="", font=('arial', 18))
        result.grid(row=3, columnspan=2)
        username = Entry(LoginFrame, font=('arial', 20), textvariable=self.USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(LoginFrame, font=('arial', 20), textvariable=self.PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = Button(LoginFrame, text="Login", font=('arial', 18), bg="blue",width=10, command=self.Login)
        btn_login.grid(row=4, columnspan=2, pady=5)
        register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        register.grid(row=0, sticky=W)
        register.bind('<Button-1>', self.ToggleToRegister)

    def RegisterForm(self):
    
        global RegisterFrame, result2
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=40)
        lbl = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl.grid(row=1)
        password1 = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        password1.grid(row=2)
        ffirstname = Label(RegisterFrame, text="Name:", font=('arial', 18), bd=18)
        ffirstname.grid(row=3)
        llastname = Label(RegisterFrame, text="Gmail:", font=('arial', 18), bd=18)
        llastname.grid(row=4)
        result2 = Label(RegisterFrame, text="", font=('arial', 18))
        result2.grid(row=5, columnspan=2)
        username = Entry(RegisterFrame, font=('arial', 20), textvariable=self.USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=self.PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=self.NAME, width=15)
        firstname.grid(row=3, column=1)
        lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=self.Gmail, width=15)
        lastname.grid(row=4, column=1)
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 12), bg="green",width=15, command=self.Register)
        btn_login.grid(row=6, columnspan=2, pady=5)
        lbl_login = Label(RegisterFrame, text="Login", fg="blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', self.ToggleToLogin)
        
    def ToggleToLogin(self, event=None):
        RegisterFrame.destroy()
        self.LoginForm()

    def ToggleToRegister(self, event=None):
        LoginFrame.destroy()
        self.RegisterForm()

    def Register(self):
        self.Database()
        if self.USERNAME.get == "" or self.PASSWORD.get() == "" or self.NAME.get() == "" or self.Gmail.get == "":
            result2.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `users` WHERE `username` = ?", (self.USERNAME.get(),))
            if cursor.fetchone() is not None:
                result2.config(text="Username is already taken", fg="red")

            else:
                cursor.execute("INSERT INTO `users` (username, password, name, gmail) VALUES(?, ?, ?, ?)", (str(self.USERNAME.get()), str(self.PASSWORD.get()), str(self.NAME.get()), str(self.Gmail.get())))
                con.commit()
                self.USERNAME.set("")
                self.PASSWORD.set("")
                self.NAME.set("")
                self.Gmail.set("")
                result2.config(text="Successfully Created!", fg="black")
                exit()
            cursor.close()
            con.close()

    def Login(self):
        self.Database()
        if self.USERNAME.get == "" or self.PASSWORD.get() == "":
            result.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `users` WHERE `username` = ? and `password` = ?", (self.USERNAME.get(), self.PASSWORD.get()))
            if cursor.fetchone() is not None:
                result.config(text="You Successfully Login", fg="blue")
                exit()
            
            else:
                result.config(text="Invalid Username or password", fg="red")
                cursor.close()

 
    def Menu(self):
        btn1=Button(root,text="☰", width=1,height=1,foreground="black",font=("arial",20))
        btn1.place(x=10, y=30)
        btn1.bind("<Button>",lambda func:self.Yedava())
        root.mainloop()
    def Yedava(self):
        btn1=Button(root,text="Login/Sign up", width=15,height=1,foreground="blue",font=("arial",20))
        btn1.place(x=10, y=40)
        btn1.bind("<Button>",lambda event:self.LoginForm()) 
        btn2=Button(root,text="Exit", width=10,foreground="red",font=("arial",20))
        btn2.place(x=10, y=100)
        btn2.bind("<Button>",lambda event:self.Exit())


app = ImageCompressor(root)
app.Show()
app.Menu()
root.mainloop()
                
    
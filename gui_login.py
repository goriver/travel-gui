import tkinter as tk 
from tkinter import ttk
import tkinter.messagebox
from tkinter import simpledialog
from functools import partial
from domain import TravelEntity, ClubEntity
from controller import CommunityController, ClubController
import main_gui as mg


def login(email, pw):
    c_control = CommunityController()
    result = c_control.get_login(email, pw)
    if result == "로그인 성공":
        mg.main_ui()
    else:
        tkinter.messagebox.showinfo(title="error",message="로그인 정보 불일치\n 다시 입력해주세요")

def to_domain(email, password, nickname, phonenumber, birthday ,address ):
    c_control = CommunityController()
    result = c_control.register(TravelEntity(email, password, nickname, phonenumber, birthday ,address))
    tk.messagebox.showinfo(title = "회원가입 결과창", message=result)
    

def register():
    # 여기서 db랑 연결해서 넣기
    window = tk.Tk()
    window.title("회원가입")
    label = tk.Label(window,text="------------ 생생 여행 정보 커뮤니티 가입 ------------", bg="#58ACFA")
    label.grid(row=0, column=0)
    label1 = tk.Label(window, text = "email" ) 
    label1.grid(row=1, column=0)
    label2 = tk.Label(window, text = "password")
    label2.grid(row=2, column=0)
    label3 = tk.Label(window, text = "별명")
    label3.grid(row=3, column=0)
    label4 = tk.Label(window, text = "전화번호")
    label4.grid(row=4, column=0)
    label5 = tk.Label(window, text = "생일(19970302)")
    label5.grid(row=5, column=0)
    label6 = tk.Label(window, text = "선호 여행지")
    label6.grid(row=6, column=0)

    v_email = tk.StringVar()
    v_password = tk.IntVar()
    v_nickname = tk.StringVar()
    v_phonenumber = tk.StringVar()
    v_birthday = tk.IntVar()
    v_address = tk.StringVar()

    e_email = tk.Entry(window, textvariable=v_email)
    e_email.grid(row=1, column=1)
    e_password = tk.Entry(window, textvariable=v_password, show="*")
    e_password.grid(row=2, column=1)
    e_nickname = tk.Entry(window, textvariable=v_nickname)
    e_nickname.grid(row=3, column=1)
    e_phonenumber = tk.Entry(window, textvariable=v_phonenumber)
    e_phonenumber.grid(row=4, column=1)
    e_birthday =tk.Entry(window, textvariable=v_birthday)
    e_birthday.grid(row=5, column=1)
    e_address = ttk.Combobox(window, width=15, textvariable = v_address)
    e_address['values']= ('서울','경기도','부산','대구','인천','광주','울산',
                            '강원도','군산','포항','전라도','jeju','해외' )
    e_address.grid(row=6, column=1)
    action = ttk.Button(window, text="회원가입하기", command =lambda: to_domain( v_email.get(),v_password.get(), v_nickname.get(),v_phonenumber.get(),v_birthday.get(),v_address.get()))
    action.grid(row=8, column=1)
    action2 = tk.Button(window, text="로그인하러가기",command=lambda:bridge_to_loginpage(window))
    action2.grid(row=8, column=2)
    window.mainloop()

def bridge_login(username, password, window):
    window.destroy()
    login(username, password)

def bridge_register(window):
    window.destroy()
    register()

def bridge_to_loginpage(window):
    window.destroy()
    login_page()


def login_page():
#window
    tkWindow = tk.Tk()
    tkWindow.lift()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Tkinter Login Form - pythonexamples.org')

    #username label and text entry box
    usernameLabel = tk.Label(tkWindow, text="email")
    usernameLabel.grid(row=0, column=0)
    username = tk.StringVar(tkWindow)
    usernameEntry = tk.Entry(tkWindow, textvariable=username)
    usernameEntry.grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = tk.Label(tkWindow,text="Password")
    passwordLabel.grid(row=1, column=0)  
    password = tk.StringVar(tkWindow)
    passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*')
    passwordEntry.grid(row=1, column=1)  


    #login button
    loginButton = tk.Button(tkWindow, text="Login", command=lambda : bridge_login(username.get(), password.get(), tkWindow) )
    loginButton.grid(row=4, column=0)
    # 값이 클래스로 안넘어가는 이슈 발생


    # register button
    registerButton = tk.Button(tkWindow, text="회원가입", command=lambda:bridge_register(tkWindow))
    registerButton.grid(row=4,column=1)
    tkWindow.mainloop()


login_page()
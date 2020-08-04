import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import tkinter.messagebox
from tkinter import simpledialog

from domain import TravelEntity, ClubEntity
from controller import CommunityController, ClubController
import gui_board as gb
# import aaaa.jpg

def to_domain(club_name, club_info):
    club_control = ClubController()
    club_name_result =club_control.search_club(club_name) # club_name으로 상세 정보 검색  
    for i, club_name in enumerate(club_name_result):
        if '--null--' in club_name:
            del club_name_result[i]

    club_info_result = club_control.get_clubinfo(club_info) # keyword검색
    for i, club_info in enumerate(club_info_result):
        if club_info[i] == '--null--':
            del club_info_result[i]
    
    tkinter.messagebox.showinfo(title="::클럽명 검색결과::", message= club_name_result)
    tkinter.messagebox.showinfo(title="::추천 클럽::", message=club_info_result)

def PageOne():
    window = tk.Tk()
    window.title("search club")
    right_frame = tk.Frame(window)
    right_frame.pack(side="right", fill="both", expand=False)
    left_frame = tk.Frame(window)
    left_frame.pack(side="left", fill="both", expand=True)
    club_control = ClubController()
    treelist = club_control.get_all_entity_club()
    list_club = tk.Listbox(left_frame)
    list_club.pack(side="right")
    for item in treelist:
        club_name  = item["club_name"] 
        list_club.insert(tk.END,club_name )       
    # 변수 선언
    club_name = tk.StringVar()
    txt_clubname = tk.Label(right_frame, text="CLUB NAME:", font=('나눔고딕', 13), bd=15)
    txt_clubname.pack()
    club_name_entry = tk.Entry(right_frame, textvariable=club_name, width=30)
    club_name_entry.pack()
    txt_clubinfo = tk.Label(right_frame, text="CLUB INFO:", font=('나눔고딕', 13), bd=15)
    txt_clubinfo.pack()
    club_info = tk.StringVar() 
    club_info_entry = tk.Entry(right_frame, textvariable=club_info, width=30)
    club_info_entry.pack()
    # button
    send_button = tk.Button(right_frame, text = "검색", command =lambda : to_domain(club_name.get(), club_info.get() ) ,width = 10,height=3)
    send_button.pack(side="bottom")
    button2 = tk.Button(right_frame, text="홈으로" , command = lambda:to_home(window), width = 10, height=3 )
    button2.pack(side="bottom")
    window.mainloop()


def join_club(club_name, member_email, member_roll):
    club_control = ClubController()
    club_members = []
    membership_entity = club_control.get_entity_controller(club_name)
    print(membership_entity)
    for club in membership_entity:
        x = club["member_email"]
        club_members.append(x)
    if member_email in club_members:
        tkinter.messagebox.showwarning("join", "이미 가입한 고객이십니다." )
    else:
        result= club_control.join_club(ClubEntity(club_name,membership_entity[0]["club_info"], membership_entity[0]["manager_email"], member_email, member_roll))
        tkinter.messagebox.showinfo("join", result )
        
        
def PageTwo():
    window = tk.Tk()
    club_label1 = tk.Label(window, text = "가입하고자 하는 클럽명을 입력해주세요")
    club_label1.pack()
    join_text = tk.StringVar()
    entry01 = tk.Entry(window, textvariable= join_text)
    entry01.pack()
    email_label2 = tk.Label(window, text = "가입했던 이메일을 입력해주세요")
    email_label2.pack()
    join_email = tk.StringVar()
    entry02 = tk.Entry(window, textvariable= join_email)
    entry02.pack()
    roll_label2 = tk.Label(window, text = "원하는 역할을 선택해주세요")
    roll_label2.pack()
    v_roll = tk.StringVar()
    e_roll= ttk.Combobox(window, width=15, textvariable = v_roll)
    e_roll['values']= ('씨앗','새싹','잎새','가지','열매','나무' )
    e_roll.pack()
    button1 = tk.Button(window, text="제출" , command =lambda :join_club(join_text.get(), join_email.get(), v_roll.get()), width = 15,height=5 )
    button1.pack(side="left")
    button2 = tk.Button(window, text="홈으로" , command =lambda:to_home(window), width = 15,height=5 )
    button2.pack(side="left")


def make_club(club_name, club_info, manager_email, member_email):
    club_control = ClubController()
    result = club_control.register_club(ClubEntity(club_name, club_info, manager_email, member_email, "manager"))
    tkinter.messagebox.showinfo(title="클럽 생성", message=result )

def PageThree():
    window =tk.Tk()
    label1 = tk.Label(window, text = "생성하고자 하는 클럽명을 입력해주세요")
    label1.pack()
    club_name = tk.StringVar()
    entry01 = tk.Entry(window, textvariable= club_name)
    entry01.pack()
    label2 = tk.Label(window, text = "클럽에대한 설명을 입력해주세요")
    label2.pack()
    club_info = tk.StringVar()
    entry02 = tk.Entry(window, textvariable= club_info)
    entry02.pack()
    label3 = tk.Label(window, text = "manager님의 email을 발급을 위한 아이디를 적어주세요")
    label3.pack()
    manager_email = tk.StringVar()
    entry02 = tk.Entry(window, textvariable= manager_email)
    entry02.pack()
    label4 = tk.Label(window, text = "커뮤니티에 가입한 이메일을 적어주세요")
    label4.pack()
    member_email = tk.StringVar()
    entry03 = tk.Entry(window, textvariable= member_email)
    entry03.pack()
    button04 = tk.Button(window, text="생성하기" , command = lambda:make_club(club_name.get(),club_info.get(), "{0}@travel.com".format(manager_email.get()), member_email.get()), width = 15,height=3  )
    button04.pack(side="left")
    button2 = tk.Button(window, text="홈으로 가기" , command =lambda:to_home(window), width = 15,height=3 )
    button2.pack(side="left")

def PageFour():
    window = tk.Tk()
    window.title("my page")
    button1 = tk.Button(window, text="내 정보 수정하기", bg="#58ACFA", command=lambda:update())
    button1.pack(side="left")
    button2 = tk.Button(window, text="탈퇴하기", bg="#2ECCFA", command=lambda:quit())
    button2.pack(side="left")
    button3 = tk.Button(window, text="가입한 클럽 목록 보기", bg="#D8CEF6", command=lambda:my_club_list())
    button3.pack(side="left")
    button4 = tk.Button(window, text="생성한 클럽 관리하기", bg="#E0E6F8", command=lambda:for_club_manager())
    button4.pack(side="left")
    button4 = tk.Button(window, text="홈으로 이동하기", bg="black",fg = "red" ,command=lambda:to_home(window))
    button4.pack(side="left")

def update():
    commu_control = CommunityController()
    email = simpledialog.askstring("기본 이메일 확인","email")
    up_nickname = simpledialog.askstring("전화번호 입력","phonenumber")
    up_birthday = simpledialog.askstring("생일 입력","birthday")
    message = commu_control.update_controller(email, up_nickname, up_birthday)
    tkinter.messagebox.showinfo(title="개인정보 수정", message=message )

def my_club_list():
    window = tk.Tk()
    window.geometry("300x300")
    commu_control = CommunityController()
    email = simpledialog.askstring("이메일 확인","email")
    my_clubs = commu_control.select_community_by_email(email)
    if bool(my_clubs):
        list_club = tk.Listbox(window)
        list_club.pack()
        for item in my_clubs:
            club_name  = item["club_name"] 
            list_club.insert(tk.END,club_name )
    else:
        tkinter.messagebox.showinfo(title="error", message="입력받은 정보가 없거나, 가입한 클럽이 없어요~" )
    button2 = tk.Button(window, text="홈으로" , command =lambda:to_home(window), width = 15,height=5 )
    button2.pack(side="left")

def quit():
    email = simpledialog.askstring("이메일 확인","email")
    commu_control = CommunityController()
    result = commu_control.delete_controller(email)
    tkinter.messagebox.showinfo(title="::탈퇴하기::", message=result )

def show_insight(club_entity):
    window = tk.Tk()
    window.geometry("800x200+500+140")
    commu_control = CommunityController()
    insights = commu_control.for_insight(club_entity["club_name"] )
    treeview = ttk.Treeview(window, columns=["one","two","three","four","five"], displaycolumns =["five","four","three","two","one"])
    treeview.pack(side="left")

    treeview.column("one", width=100, anchor="center")
    treeview.heading("one", text="멤버 이메일", anchor="center")

    treeview.column("two", width=100, anchor="center")
    treeview.heading("two", text="멤버 등급", anchor="center")

    treeview.column("three", width=100, anchor="center")
    treeview.heading("three", text="전화번호", anchor="center")

    treeview.column("four", width=100, anchor="center")
    treeview.heading("four", text="생일", anchor="center")

    treeview.column("five", width=100, anchor="center")
    treeview.heading("five", text="선호하는 여행지", anchor="center")

    for i, insight in enumerate(insights):
        treeview.insert('','end',values = (insight['member_email'], insight['member_roll'], insight['phonenumber'], insight['birthday'], insight['address'])) 
    
    button2 = tk.Button(window, text="홈으로" , command =lambda:to_home(window), width = 15,height=5 )
    button2.pack(side="left")


def for_club_manager():
    manager_email = simpledialog.askstring("관리자 이메일","관리자 이메일을 입력하세요 \n ex)gamja@travel.com")
    club_name = simpledialog.askstring("관리할 클럽명","관리할 클럽명을 입력하세요")
    club_control = ClubController()
    clubs = club_control.get_all_entity_club()
    list_for_club=[]
    if len(clubs)>1:
        for club in clubs:
            # print(club)
            if (club["club_name"] == club_name) and (club["manager_email"] == manager_email):
                list_for_club.append(club)
        show_insight(list_for_club) # entity 다 보내기 한개의 클럽에 대한 중복제거된 값이다
        if len(list_for_club) ==0:
            tkinter.messagebox.showinfo(title="::error::", message="관리자님 관리할 멤버가 아직 없습니다. \n 또는 올바른 클럽명이 아닙니다" )

def main_ui():

    root = tk.Tk()
    myFrame=tk.Frame(root, bg = "#A9F5BC")
    myFrame.pack(side="left")
    myImage = tk.Frame(root)
    myImage.pack(side="right")
    label = tk.Label(myFrame, text="여행 정보 커뮤니티 & club", font=Font(family="나눔고딕 ExtraBold", size="20", weight="bold"))
    label.pack(side="top", fill="x", pady=10)
    button1 = tk.Button(myFrame, text="++++++++ CLUB 검색하기 ++++++++",font=Font(family="나눔스퀘어 Light", size="16"),
                        command=lambda:bridge_pageone(root))
    button2 = tk.Button(myFrame, text="++++++++ CLUB 가입하기 ++++++++",font=Font(family="나눔스퀘어 Light", size="16"),
                        command=lambda:bridge_pagetwo(root) )
    button3 = tk.Button(myFrame, text="++++++++ CLUB 생성하기 ++++++++",font=Font(family="나눔스퀘어 Light", size="16"),
                        command=lambda:bridge_pagethree(root) )
    button4 = tk.Button(myFrame, text="+++++++++ 마이페이지 +++++++++",font=Font(family="나눔스퀘어 Light", size="16"),
                        command=lambda:bridge_pagefour(root) )
    button5 = tk.Button(myFrame, text="++++++++++ 게시판 ++++++++++",font=Font(family="나눔스퀘어 Light", size="16"),
                        command=lambda:bridge_pagefive(root) )
    button6 = tk.Button(myFrame, text="+++++++커뮤니티 로그아웃+++++++",font=Font(family="나눔스퀘어 Light", size="16"),
                        command=lambda:close_window(root))
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    root.mainloop()

def bridge_pageone(window):
    window.destroy()
    PageOne()

def bridge_pagetwo(window):
    window.destroy()
    PageTwo()

def bridge_pagethree(window): 
    window.destroy()
    PageThree()

def bridge_pagefour(window):
    window.destroy()
    PageFour()

def bridge_pagefive(window):
    window.destroy()
    gb.main_board()

def to_home(window):
    window.destroy()
    main_ui()

def close_window(window):
    window.destroy()
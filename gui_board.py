import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import tkinter.messagebox
from tkinter import simpledialog

from domain import TravelEntity, ClubEntity, BoardEntity
from controller import BoardController, ClubController, CommunityController
import random
# import gui_main
## board 이전 데이터는 product git에 올려둠 참고!!!!

# ========================================================================
# 여기서 store로 이동하는데
# 게시글만 모아두는 db를 제작할 예정이다.
# column = 글넘버, 관리자 email, 클럽명, 제목, 게시글, 작성자 email
# 글 넘버는 domain에서 정함
# 필요한 service -> register : email을 입력받아서 email이 club에 있을 때 등록
# update :  email을 입력받아서 email이 있을 때 등록
# delete :  email을 입력 or 관리자 메일이 있을 때 삭제

# 글넘버 primary key
# 클럽명 forein key
# ========================================================================


def register_board(board_entity):
    controller = BoardController()
    result = controller.register_board(board_entity)
    tkinter.messagebox.showinfo("::결과창::",result)  
    print(result)

def PageOne():
    controller = BoardController()
    window = tk.Tk()
    title_font = Font(family="나눔고딕 ExtraBold", size="20", weight="bold")
    text_font = Font(family="나눔스퀘어 Light", size="16")
    club_name = simpledialog.askstring("::입장할 클럽명::","입장할 클럽명을 적어주세요")
    result_board_entity = controller.board_view_all(club_name) 
    print(result_board_entity)
    # 이제 다 가져옴
    manager_email = result_board_entity[0]["manager_email"]
    TopFrame = tk.Frame(window)
    TopFrame.pack(side="top")
    BottomFrame = tk.Frame(window)
    BottomFrame.pack(side="bottom")
    #top에 클럽 게시글 작성 entity
    title = tk.StringVar()
    writer = tk.StringVar()
    label1 = tk.Label(TopFrame, text = "제목",font=title_font)
    label1.pack(side="left")
    entry1 = tk.Entry(TopFrame, textvariable = title)
    entry1.pack(side="left")
    label2 = tk.Label(TopFrame, text = "작성자(community email)",font=text_font)
    label2.pack(side="left")
    entry2 = tk.Entry(TopFrame, textvariable = writer)
    entry2.pack(side="left")
    label2 = tk.Label(BottomFrame, text = "content \n (3000자 이내)",font=text_font)
    label2.pack()
    textExample=tk.Text(BottomFrame, height=15)
    textExample.pack()
    btnRead=tk.Button(BottomFrame, height=1, width=10, text="등록하기", 
                    command=lambda:register_board(BoardEntity((title.get()+str(random.randint(1,100))+writer.get()),title.get(),\
                    textExample.get("1.0","end"),writer.get(), manager_email, club_name)))
    btnRead.pack(side="right")
    homebutton = tk.Button(BottomFrame, text="home", command = lambda:to_home(window))
    homebutton.pack(side="right")
    window.mainloop()
        
# ++++++++ 게시판 글보기 ++++++++

def show_text(title, club_name):
    controller = BoardController()
    board_list = controller.get_all_board(club_name)
    # borad_view(따로 생성한 view창)
    # title만 필요하다.
    # 이거 나중에 title로 검색해서 내용 출력할 예정이다.
    titles = []
    for board in board_list:
        if board["title"]== title:
            titles.append(board["content"])
    if not len(titles):
        tkinter.messagebox.showinfo("::결과창::", "검색한 제목의 글이 없어요") 
    else:
        tkinter.messagebox.showinfo("::결과창::",titles)

def PageTwo():
    window = tk.Tk()
    club_name = simpledialog.askstring(":::club name:::",
                                         "입장하고자 하는 클럽명을 입력해주세요" )
    # 클럽명에 따라 manager email 가져오는 함수
    controller = BoardController()
    board_list = controller.get_all_board(club_name)
    if not bool(board_list):
        tkinter.messagebox.showerror("error","죄송합니다. 해당 클럽은 존재하지 않습니다.")
    else:
        print("deguging gui")
        TopFrame = tk.Frame(window, width=500, height=500)
        TopFrame.pack(side="top")
        BottomFrame = tk.Frame(window,width=500, height=300)
        BottomFrame.pack(side="bottom")

        treeview = ttk.Treeview(TopFrame, columns=["one","two"]) #, displaycolumns =["three","two","one"])
        treeview.pack(side="left")

        treeview.column("one", width=350, anchor="center")
        treeview.heading("one", text="작성자", anchor="center")

        treeview.column("two", width=100, anchor="center")
        treeview.heading("two", text="제목", anchor="center")

        controller = BoardController()
        board_list = controller.get_all_board(club_name)
        print(board_list)
        for i, board in enumerate(board_list):
            treeview.insert('','end',values = (board['title'], board['member_email']))

        label1 =tk.Label(BottomFrame, text="확인하고 싶은 게시판 글의 제목")
        label1.pack(side="left")
        title=tk.StringVar(window)
        entry1= tk.Entry(BottomFrame, textvariable=title)
        entry1.pack(side="left")
        button = tk.Button(BottomFrame, text="검색", command=lambda: show_text(title.get(), club_name))
        button.pack()
        homebutton = tk.Button(BottomFrame, text="home", command =lambda: to_home(window))
        homebutton.pack(side="right")
        window.mainloop()

# ++++++++ 게시판 글 수정하기 ++++++++
def PageThree():
    window=tk.Tk()
    label = tk.Label(window, text="기능 준비중입니다.....;)", highlightcolor="white", bg="black")
    label.pack()
    homebutton = tk.Button(window, text="home", command =lambda: to_home(window))
    homebutton.pack()
    window.mainloop()

# +++++++++ 게시판 글 삭제하기 +++++++++
def delete_by_email(title, board_list):
    # todo 고냥 sql문으로 받아와서 in keys( )로 돌려버리기
    controller = BoardController()
    list_of_titles = []
    for board in board_list:
        list_of_titles.append(board["title"])
    if title in list_of_titles:
        for i ,value in enumerate(list_of_titles):
            if title == value:
                message =controller.delete_board(board_list[i]["id"], board_list[i]["email"], board_list[i]["club_name"])
                tkinter.messagebox.showinfo("::result::", message)
    else:
        tkinter.messagebox.showinfo("::result::", "삭제할 글을 찾지 못하였습니다.")

def PageFour():
    try:
        window = tk.Tk()
        club_name = simpledialog.askstring(":::club name:::", "입장하고자 하는 클럽명을 입력해주세요")
        TopFrame = tk.Frame(window, width=500, height=500)
        TopFrame.pack(side="top")
        BottomFrame = tk.Frame(window,width=500, height=300)
        BottomFrame.pack(side="bottom")
        controller = BoardController()
        board_list = controller.get_all_board(club_name) #`id`, `content`,`title`,`member_email`   반환
        print(board_list)
        title_list = tk.Listbox(TopFrame, selectmode='extended', height=0)
        for i, board in enumerate(board_list):
            board_list.insert(i, board[i]["title"])
        title_list.pack()    
        label1 = tk.Label(BottomFrame, text = "삭제하고 싶은 게시글의 제목을 적어주세요")
        label1.pack(side="left")
        title = tk.StringVar()
        entry1 = tk.Entry(BottomFrame, textvariable = title)
        entry1.pack(side="left")
        button1 = tk.Button(BottomFrame,text="검색", command=lambda:delete_by_email(title, board_list))
        button1.pack(side="left")
        homebutton = tk.Button(window, text="home", command = to_home(window))
        homebutton.pack()
        window.mainloop()
    except:
        tkinter.messagebox.showerror("error","error : 죄송합니다. error가 발생했습니다. 빠른 정비 후 찾아뵙도록 하겠습니다.")


def main_board():
    root = tk.Tk()
    title_font = Font(family="나눔고딕 ExtraBold", size="20", weight="bold")
    myFrame=tk.Frame(root, bg = "#F6CEF5")
    myFrame.pack()
    label = tk.Label(root, text="여행 정보 커뮤니티 & club", font=title_font)
    label.pack(side="top", fill="x", pady=10)

    button1 = tk.Button(root, text="++++++++ 게시판 글쓰기 ++++++++",
                        command=lambda:bridge_pageone(root))
    button2 = tk.Button(root, text="++++++++ 게시판 글 보기 ++++++++",
                        command=lambda:bridge_pagetwo(root))
    button3 = tk.Button(root, text="++++++++ 게시판 글 수정하기 ++++++++",
                        command=lambda:bridge_pagethree(root))
    button4 = tk.Button(root, text="+++++++++ 게시판 글 삭제하기 +++++++++",
                        command=lambda:bridge_pagefour(root))
    button5 = tk.Button(root, text="+++++++++ exit +++++++++",
                        command=lambda:close_window(root) )
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
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

def to_home(window):
    window.destroy()
    main_board()

def close_window(window):
    window.destroy()

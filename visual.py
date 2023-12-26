from tkinter import *
from random import randint
from PIL import Image,ImageTk
buttons = []
#левый верхний угол имеит координату 0,0
def create_btn(number,x,y):#number - это то что написано на кнопке,x - координата по х , у = ккордината по У
    btn = Button(cnv,text=number,font=(None,24),width=10,bg="black",fg= "white")
    btn.place(x=x,y=y)#
    buttons.append(btn)
    btn.bind("<Enter>",lambda event :leave_button(btn))
    btn.bind("<Leave>",lambda event :enter_button(btn))
    btn.bind("<Button-1>",lambda event :click_number(btn))
def start_game():
    global name1,name2,game_start,btn_restart,btn_new_start
    name1 = entr1.get()
    name2 = entr2.get()

    if len(name1) == 0:
        lbl_error1["text"] = "///:error введите имя для  игрок1"
    else:
        lbl_error1["text"] = ""
    if len(name2) == 0:
        lbl_error2["text"] = "///:error введите имя для  игрок2"
    else:
        lbl_error2["text"] = ""
    if len(name1) == 0 or len(name2) == 0:
        return
    game_start = True
    entr1.destroy()
    entr2.destroy()
    lbl1.destroy()
    lbl2.destroy()
    btn1.destroy()
    lbl_name["text"] = name1
    #btn_restart.bind("<Button-1>",restart)
    print(type(btn_restart))
    btn_new_start = Button(cnv,text="restart",font=(None,24),bg="white",fg="black")
    btn_new_start.place(x = 500 ,y = 350)
    btn_new_start.bind("<Button-1>",restart)

def enter_button(btn):

    if btn["text"] == "" or game_start == False:
        return

    btn["bg"] = "black"

    btn["fg"] = "white"

def leave_button(btn):
    if btn["text"] == "" or game_start == False:
        return

    btn["fg"] = "black"
    btn["bg"] = "white"
def click_number(btn):
    global game_start,number_hod,btn_restart
    if game_start == False:
        return
    if btn["text"] == "":
        return
    if int(btn["text"]) == magic_number:
        cnv.itemconfigure(btn_restart,image = big_strela)
        btn["bg"] = "green"
        game_start = False
        name = ""
        if number_hod == 1:
            name = name1
        else:
            name = name2
        lbl_win["text"] = f"{name} you win"
        return
    btn["text"] = ""

    btn["bg"] = "black"
    if number_hod == 1:
        number_hod = 2
        lbl_name["text"] = name2
    else:
        number_hod = 1
        lbl_name["text"] = name1

def restart(event):
    global magic_number,game_start,number_hod
    magic_number = randint(1,20)
    number = 1
    for btn in buttons:
        btn["text"] = number
        number = number + 1
        btn["bg"] ="black"
        btn["fg"] ="white"
    game_start = True
    lbl_win["text"] = ""
    number_hod = 1

window = Tk()

window.resizable(0,0)
window.title("ugadayka")
cnv = Canvas(window,width=1200,height=650,bg="white")
cnv.pack()
x_kord = 50
y_kord = 600
for i in range(10):
    create_btn(i+1,x_kord,y_kord)
    y_kord -=65
x_kord = 950
y_kord = 600
for i in range(11,21):
    create_btn(i,x_kord,y_kord)
    y_kord-=65
game_start = False
name1 = ""
name2 = ""
number_hod = 1
lbl_name = Label(cnv,text="",font=(None,24))
lbl_name.place(x = 350 ,y = 30)

magic_number = randint(1,20)
print(magic_number)
lbl_win = Label(cnv,text="",fg="gold",bg= "white",font=(None,24))
lbl_win.place(x = 450 ,y = 200)

lbl_error1 = Label(cnv,text="",fg="red",bg= "white",font=(None,24))
lbl_error1.place(x= 350,y= 100)
lbl_error2 = Label(cnv,text="",fg="red",bg= "white",font=(None,24))
lbl_error2.place(x= 350,y= 250)
lbl1 = Label(cnv,text="игрок1",font=(None,24),bg= "white")
lbl1.place(x = 300 ,y =50 )
entr1 = Entry(cnv,font=(None,24))
entr1.place(x=550,y=50)
lbl2 = Label(cnv,text="игрок2",font=(None,24),bg="white")
lbl2.place(x = 300 ,y =200 )
entr2 = Entry(cnv,font=(None,24))
entr2.place(x=550,y = 200)
btn1 = Button(cnv,text="play",font=(None,36),bg= "white",fg= "black",command = start_game)
btn1.place(x = 530 ,y =500 )
btn1.bind("<Enter>",lambda event: enter_button(btn1))
btn1.bind("<Leave>",lambda event: leave_button(btn1))
img_restart2 = ImageTk.PhotoImage(Image.open("strela.png"))
big_strela =  ImageTk.PhotoImage(Image.open("big_strela.png"))
btn_restart = cnv.create_image(1155, 20, anchor=NW, image=img_restart2)
print(type(btn_restart))

btn_new_start = None
window.mainloop()

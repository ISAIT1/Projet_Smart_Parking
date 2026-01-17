from dis import show_code
from subprocess import call
from tkinter import *

import mysql
from mysql import connector
from PIL import Image, ImageTk
from tkinter import messagebox
from sqlalchemy import true

log = Tk()
log.title('Smart parking Center')
log.geometry('925x500+300+200')
log.configure(bg="#cce0ff")
log.resizable(False, False)

def signin() :
    con = mysql.connector.connect(user='root', password='', host='localhost', port=3308, database='smart_parking')
    cursor = con.cursor()
    uname = User.get()
    password = MDP.get()
    sql = "SELECT * FROM admin WHERE Nom_utilisateur=%s AND Mot_de_passe=%s"
    cursor.execute(sql, [(uname), (password)])
    result = cursor.fetchall()
    if result:
        messagebox.showinfo("Bienvenue","Bienvenue dans votre espace Smart Parking")
        log.destroy()
        call(["python", "main.py"])
        return True
    else:
        messagebox.showinfo("Invalid", " Nom d'utilisateur ou mot de passe Invalide !")
        return False


log.iconbitmap("images\IsaIt_icon.ico")
img = ImageTk.PhotoImage(Image.open("images/login_pic.png"))
Label(log, image=img, bg="#cce0ff").place(x=50,y=50)


Fr = Frame(log, width=350, height=450, bg="#cce0ff")
Fr.place(x=480, y=50)
Titre = Label(Fr,text="Se connecter", fg='#0073e6', bg='#cce0ff', font=('yu gothic ui ',25,'bold'))
Titre.place(x=45, y=2)

signIn_img = ImageTk.PhotoImage(Image.open("images\hyy.png"))
Label(Fr, image=signIn_img, bg="#cce0ff").place(x=80,y=50)

def endProgam():
    # log.quit()
    log.destroy()

def on_enter(e): User.delete(0,'end')
def on_leave(e): 
    name = User.get()
    if name =='' : User.insert(0, "Entrez votre nom utilisateur")
    
User_label=Label(Fr, text="Nom d'utilisateur", fg='#303030', border=0, bg='#cce0ff',font=('Microsoft Yahei UI light',11))
User_label.place(x=30,y=180)
User = Entry(Fr,width=25,fg='#303030', highlightthickness=0, relief=FLAT, border=0, bg='#cce0ff', font=('Microsoft Yahei UI light',11))
User.place(x=30,y=210)
User.bind('<FocusIn>', on_enter)
#User.bind('<FocusOut>', on_leave)
Frame(Fr,width=260,height=1, bg='#696969').place(x=25,y=230)

def on_enter(e): MDP.delete(0,'end') 
def on_leave(e): 
    mdp = MDP.get() 
    if mdp =='' : 
        MDP.insert(0, "Entrez votre mot de passe ")

MDP_label=Label(Fr, text="Mot de passe", fg='#303030', border=0, bg='#cce0ff',font=('Microsoft Yahei UI light',11))
MDP_label.place(x=30,y=260)
MDP= Entry(Fr, highlightthickness=0, relief=FLAT, width=25, fg='#303030', border=0, bg='#cce0ff', font=('Microsoft Yahei UI light',11), show="*")
MDP.place(x=30,y=290)
MDP.bind('<FocusIn>', on_enter)
#MDP.bind('<FocusOut>', on_leave)
Frame(Fr,width=260,height=1, bg='#696969').place(x=25,y=310)

#################show/hide password ###########################

show_image = ImageTk.PhotoImage \
            (file='images/show.png')
hide_image = ImageTk.PhotoImage \
            (file='images/hide.png')
            
def showP():
    hide_button = Button(Fr, image=show_image, command=hide, relief=FLAT, activebackground="#cce0ff" , borderwidth=0, background="#cce0ff", cursor="hand2")
    hide_button.place(x=270, y=290)
    MDP.config(show='') 

def hide():
    show_button = Button(Fr, image=hide_image, command=showP, relief=FLAT, activebackground="#cce0ff", borderwidth=0, background="#cce0ff", cursor="hand2")
    show_button.place(x=270, y=290)
    MDP.config(show='*')

    
show_button = Button(Fr, image=hide_image, command=hide, relief=FLAT, activebackground="#cce0ff", borderwidth=0, background="#cce0ff", cursor="hand2")
show_button.place(x=270, y=290)
    
#################################################################

Button(Fr, width=20, font=('Microsoft Yahei',14, ), pady=4,text="Me connecter",fg='white',bg='#0073e6', command=signin, border=0).place(x=35,y=340)

mdpo=Button(Fr,text='Mot de passe oublier !', border=0, cursor='hand2', font=('yu gothic ui',9), bg='#cce0ff', fg='gray')
mdpo.place(x=35,y=390)

log.mainloop()
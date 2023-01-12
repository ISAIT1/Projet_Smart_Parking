
from subprocess import call
from tkinter import *
from tkinter import messagebox
import mysql
import os
import ctypes
from mysql import connector
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("Smart parking Center")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.config(background='#b5c7de')

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        self.header = Frame(self.window, bg='#0d294b')
        self.header.place(x=300, y=0, width=1500, height=60)
        self.header_text = Label(self.window, text="Smart parking Center", fg='white', bg='#0d294b', font=('yu gothic ui ',25,'bold'))
        self.header_text.place(x=300, y=10)
        self.logout_btn = Button(self.header, text="Se déconnecter", bg='#b5c7de', font=("'Microsoft Yahei'", 13, "bold"), bd=0, fg='white',
                                    pady=4, width=20, command=self.logout, cursor='hand2', activebackground='#476d9e')
        self.logout_btn.place(x=800, y=12)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#e6f0ff', highlightcolor="white")
        self.sidebar.place(x=0, y=0, width=300, height=850)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        self.heading = Label(self.window, text='Dashboard', font=("", 24, "bold"), fg='#0d294b', bg='#b5c7de')
        self.heading.place(x=325, y=70)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=170, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#ff4000')
        self.bodyFrame3.place(x=680, y=170, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=170, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        self.logoImage = Image.open('imagesIc\\logo2.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#e6f0ff')
        self.logo.image = photo
        self.logo.place(x=20, y=110)

        # Name of person
        #self.brandName = Label(self.sidebar, text="Admin Panel", bg='#e6f0ff', font=("Copperplate", 30, "bold"))
        #self.brandName.place(x=30, y=90)

        # Dashboard
        self.dashboardImage = ImageTk.PhotoImage(file='images/dashboard.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#e6f0ff')
        self.dashboard.place(x=24, y=289)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#b5c7de', font=("", 15, "bold"), bd=0,
                                     cursor='hand2',width=20, activebackground='#b5c7de')
        self.dashboard_text.place(x=80, y=287)

        #PlaceParking
        self.PlaceParking = ImageTk.PhotoImage(file='images/placeP.png')
        self.PP = Label(self.sidebar, image=self.PlaceParking, bg='#e6f0ff')
        self.PP.place(x=24, y=340)

        self.PP_text = Button(self.sidebar, text="Gestion des places", bg='#e6f0ff',
                                    pady=4, width=15, font=("", 15, "bold"), bd=0,  cursor='hand2', activebackground='#b5c7de')
        self.PP_text.place(x=80, y=345)

        #Personne
        self.Parking = ImageTk.PhotoImage(file='images/parking.png')
        self.P = Label(self.sidebar, image=self.Parking, bg='#e6f0ff')
        self.P.place(x=24, y=395)

        self.Parking_text = Button(self.sidebar, text="Gestion Personne", bg='#e6f0ff', font=("", 15, "bold"), bd=0,
                            cursor='hand2', activebackground='#b5c7de')
        self.Parking_text.place(x=80, y=402)

        # Exit
        self.ExitImage = ImageTk.PhotoImage(file='images/exit.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#e6f0ff')
        self.Exit.place(x=24, y=452)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#e6f0ff', font=("", 15, "bold"), bd=0, command=window.quit,
                                cursor='hand2', activebackground='#b5c7de')
        self.Exit_text.place(x=80, y=462)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 2
        self.total_place = Label(self.bodyFrame2, text='140', bg='#009aa5', fg='white', font=("Microsoft Yahei", 30, "bold"))
        self.total_place.place(x=120, y=90)

        self.totalPlaceImage = ImageTk.PhotoImage(file='images/TotalPlace.png')
        self.totalPlace = Label(self.bodyFrame2, image=self.totalPlaceImage, bg='#009aa5')
        self.totalPlace.place(x=227, y=70)

        self.totalPlace_label = Label(self.bodyFrame2, text="Total des places en parking", bg='#009aa5', font=("Microsoft Yahei", 16, "bold"),
                                       fg='white')
        self.totalPlace_label.place(x=5, y=5)

        # Body Frame 3
        self.place_etudiant = Label(self.bodyFrame3, text='90', bg='#ff4000', fg='white', font=("Microsoft Yahei", 30, "bold"))
        self.place_etudiant.place(x=120, y=90)

        self.LeftImage = ImageTk.PhotoImage(file='images/personnel.png')
        self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#ff4000')
        self.Left.place(x=227, y=70)

        self.place_etudiant_label = Label(self.bodyFrame3, text="Total des place étudiants", bg='#ff4000', font=("Microsoft Yahei", 16, "bold"),
                                      fg='white')
        self.place_etudiant_label.place(x=5, y=5)

        # Body Frame 4
        self.place_personnel = Label(self.bodyFrame4, text='30', fg='white', bg='#ffcb1f', font=("Microsoft Yahei", 30, "bold"))
        self.place_personnel.place(x=120, y=90)

        self.place_personnel_image = ImageTk.PhotoImage(file='images/personnel1.png')
        self.place_personnelIcon = Label(self.bodyFrame4, image=self.place_personnel_image, bg='#ffcb1f')
        self.place_personnelIcon.place(x=227, y=70)

        self.placepersonnel_label = Label(self.bodyFrame4, text="Total des places personnels", bg='#ffcb1f', font=("Microsoft Yahei", 16, "bold"),
                                    fg='white')
        self.placepersonnel_label.place(x=5, y=5)

        # date and Time
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="#e6f0ff")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="#e6f0ff", fg="black")
        self.date_time.after(100, self.show_time)

    def logout(self):
        self.window.destroy()
        call(["python", "login.py"])





    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()





'''def user_show():
        con = mysql.connector.connect(user='root', password='', host='localhost', port=3308, database='smart_parking')
        cursor = con.cursor()
        uname = login.User.get()
        sql = "SELECT Nom_utilisateur FROM admin WHERE Nom_utilisateur=%s"
        cursor.execute(sql, [(uname)])
        result = cursor.fetchall()
        if result:
            call(["python", "Dashboard.py"])
            return True
        else:
            messagebox.showerror("Invalid", " Erreur")
            return False'''


def wind():
    window = Tk()
    window.iconbitmap("images\IsaIt_icon.ico")
    Dashboard(window)
    window.mainloop()




if __name__ == '__main__':
    wind()
from idlelib import tree
from subprocess import call
from detection.controlle import *
from detection.detection import *

import mysql
from PIL import Image, ImageTk
import pymysql
from datetime import *
import time
from mysql import connector

from controller import controller
from tkinter import ttk
from tkinter import messagebox

try:
    import tkinter as tk  # python 3
    from tkinter import font as tkfont, ttk, END  # python 3
except ImportError:
    import Tkinter as tk  # python 2
    import tkFont as tkfont  # python 2


class Dashboard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Smart parking Center")
        self.geometry("1366x768")
        self.resizable(0, 0)
        self.state("zoomed")
        self.config(background='#b5c7de')

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="right", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(window=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# ==========================================Page dashboard =====================================
# =========================================================================================================
class StartPage(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)
        self.controller = controller
        self.configure(bg="#b5c7de")
        controller.title("Smart parking Center")
        controller.geometry("1366x768")
        controller.resizable(0, 0)
        controller.state("zoomed")

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        header = tk.Frame(self, bg='#0d294b')
        header.place(x=300, y=0, width=1500, height=60)
        header_text = tk.Label(self, text="Smart parking Center", fg='white', bg='#0d294b',
                               font=('yu gothic ui ', 25, 'bold'))
        header_text.place(x=300, y=10)
        logout_btn = tk.Button(self, text="Se déconnecter", bg='#b5c7de',
                               font=("'Microsoft Yahei'", 13, "bold"), bd=0, fg='white',
                               pady=8, width=30, command=self.logout, cursor='hand2', activebackground='#476d9e')
        logout_btn.place(x=1200, y=7)
        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        sidebar = tk.Frame(self, bg='#e6f0ff', highlightcolor="white")
        sidebar.place(x=0, y=0, width=300, height=850)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        heading = tk.Label(self, text='Dashboard', font=("", 24, "bold"), fg='#0d294b', bg='#b5c7de')
        heading.place(x=325, y=70)

        # body frame 2
        bodyFrame2 = tk.Frame(self, bg='#009aa5')
        bodyFrame2.place(x=328, y=170, width=310, height=220)

        # body frame 3
        bodyFrame3 = tk.Frame(self, bg='#ff4000')
        bodyFrame3.place(x=680, y=170, width=310, height=220)

        # body frame 4
        bodyFrame4 = tk.Frame(self, bg='#ffcb1f')
        bodyFrame4.place(x=1030, y=170, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        logoImage = Image.open('imagesIc\\logo2.png')
        photo = ImageTk.PhotoImage(logoImage)
        logo = tk.Label(sidebar, image=photo, bg='#e6f0ff')
        logo.image = photo
        logo.place(x=20, y=110)

        # Dashboard
        dashboardI = Image.open('images/dashboard.png')
        dashboardImage = ImageTk.PhotoImage(dashboardI)
        dashboard = tk.Label(sidebar, image=dashboardImage, bg='#e6f0ff')
        dashboard.image = dashboardImage
        dashboard.place(x=24, y=289)

        dashboard_text = tk.Button(sidebar, text="Dashboard", bg='#b5c7de', font=("", 15, "bold"), bd=0,
                                   cursor='hand2', width=20, activebackground='#b5c7de')
        dashboard_text.place(x=80, y=287)

        # PlaceParking
        PlaceParking = tk.PhotoImage(file='images/placeP.png')
        PP = tk.Label(sidebar, image=PlaceParking, bg='#e6f0ff')
        PP.image = PlaceParking
        PP.place(x=24, y=340)

        PP_text = tk.Button(sidebar, text="Gestion des places", bg='#e6f0ff',
                            pady=4, command=lambda: controller.show_frame("PageOne"), width=15, font=("", 15, "bold"),
                            bd=0, cursor='hand2', activebackground='#b5c7de')
        PP_text.place(x=80, y=345)

        # Personne
        Parking = ImageTk.PhotoImage(file='images/parking.png')
        P = tk.Label(sidebar, image=Parking, bg='#e6f0ff')
        P.image = Parking
        P.place(x=24, y=395)

        Parking_text = tk.Button(sidebar, text="Gestion Personne", bg='#e6f0ff', font=("", 15, "bold"), bd=0,
                                 cursor='hand2', command=lambda: controller.show_frame("PageTwo"), activebackground='#b5c7de')
        Parking_text.place(x=80, y=402)

        # Exit
        ExitImage = ImageTk.PhotoImage(file='images/exit.png')
        Exit = tk.Label(sidebar, image=ExitImage, bg='#e6f0ff')
        Exit.image = ExitImage
        Exit.place(x=24, y=452)

        Exit_text = tk.Button(sidebar, text="Exit", bg='#e6f0ff', font=("", 15, "bold"), bd=0,
                              command=controller.destroy,
                              cursor='hand2', activebackground='#b5c7de')
        Exit_text.place(x=80, y=462)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        total_place = tk.Label(bodyFrame2, text='140', bg='#009aa5', fg='white',
                               font=("Microsoft Yahei", 30, "bold"))
        total_place.place(x=120, y=90)

        totalPlaceImage = ImageTk.PhotoImage(file='images/TotalPlace.png')
        totalPlace = tk.Label(bodyFrame2, image=totalPlaceImage, bg='#009aa5')
        totalPlace.image = totalPlaceImage
        totalPlace.place(x=227, y=70)

        totalPlace_label = tk.Label(bodyFrame2, text="Total des places en parking", bg='#009aa5',
                                    font=("Microsoft Yahei", 16, "bold"),
                                    fg='white')
        totalPlace_label.place(x=5, y=5)

        # Body Frame 2
        place_etudiant = tk.Label(bodyFrame3, text='90', bg='#ff4000', fg='white',
                                  font=("Microsoft Yahei", 30, "bold"))
        place_etudiant.place(x=120, y=90)

        LeftImage = ImageTk.PhotoImage(file='images/personnel.png')
        Left = tk.Label(bodyFrame3, image=LeftImage, bg='#ff4000')
        Left.image = LeftImage
        Left.place(x=227, y=70)

        place_etudiant_label = tk.Label(bodyFrame3, text="Total des places étudiants", bg='#ff4000',
                                        font=("Microsoft Yahei", 16, "bold"),
                                        fg='white')
        place_etudiant_label.place(x=5, y=5)

        # Body Frame 3
        place_personnel = tk.Label(bodyFrame4, text='30', fg='white', bg='#ffcb1f',
                                   font=("Microsoft Yahei", 30, "bold"))
        place_personnel.place(x=120, y=90)

        place_personnel_image = ImageTk.PhotoImage(file='images/personnel1.png')
        place_personnelIcon = tk.Label(bodyFrame4, image=place_personnel_image, bg='#ffcb1f')
        place_personnelIcon.image = place_personnel_image
        place_personnelIcon.place(x=227, y=70)

        placepersonnel_label = tk.Label(bodyFrame4, text="Total des places personnels", bg='#ffcb1f',
                                        font=("Microsoft Yahei", 16, "bold"),
                                        fg='white')
        placepersonnel_label.place(x=5, y=5)

        # date and Time
        clock_image = ImageTk.PhotoImage(file="imagesIc\\time.png")
        date_time_image = tk.Label(sidebar, image=clock_image, bg="#e6f0ff")
        date_time_image.place(x=88, y=20)

        self.date_time = tk.Label(controller)
        self.date_time.place(x=115, y=15)
        self.show_time()

    def show_time(self):
        timer = time.strftime("%H:%M:%S")
        dater = time.strftime('%Y/%m/%d')
        set_text = f"  {timer} \n {dater}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="#e6f0ff", fg="#00294B")
        self.date_time.after(100, self.show_time)

    def logout(self):
        self.controller.destroy()
        call(["python", "login.py"])


# ==========================================Page de gestion des places ====================================
# =========================================================================================================
class PageOne(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)
        self.controller = controller
        self.configure(bg="#b5c7de")
        controller.geometry("1366x768")
        controller.resizable(0, 0)
        controller.state("zoomed")

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        header = tk.Frame(self, bg='#0D294B')
        header.place(x=0, y=0, width=1550, height=60)

        # ================== BUTTONS ===================================================

        back_btn = tk.Button(self, text="Retour", bg='#b5c7de', cursor='hand2', activebackground='#476d9e',
                             font=("'Microsoft Yahei'", 13, "bold"), bd=0, fg='white',
                             pady=8, width=30, command=lambda: controller.show_frame("StartPage"))
        back_btn.place(x=800, y=7)

        # ================== BODY ===================================================
        con = pymysql.connect(host="localhost", port=3308, user="root", password="", database="smart_parking")
        cur = con.cursor()
        cur.execute("SELECT * FROM parking")
        result = cur.fetchall()
        for i in result:
            # id=i[0]
            capacite = i[1]
            nbr_places_occ = i[2]
            heading = tk.Label(self, text="Capacité du parking", font=("Calibri", 50, "bold"), fg='#0D294B',
                               bg='#b5c7de')
            heading.place(x=600, y=120)
            heading = tk.Label(self, text=capacite, font=("Calibri", 50, ""), fg='yellow', bg='#b5c7de')
            heading.place(x=810, y=270)

            heading = tk.Label(self, text="Nombre de places occupées", font=("Calibri", 50, "bold"),
                               fg='#0D294B', bg='#b5c7de')
            heading.place(x=500, y=500)
            heading = tk.Label(self, text=nbr_places_occ, font=("Calibri", 50, ""), fg='yellow', bg='#b5c7de')
            heading.place(x=850, y=650)
            cur.close()

    def main(self):
        con = pymysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="", database="smart_parking")
        cur = con.cursor()

        cur.execute("SELECT * FROM parking")
        result = cur.fetchall()
        for i in result:
            # id=i[0]
            capacite = [1]
            nbr_places_occ = [2]
            print(capacite, nbr_places_occ)
        cur.close()

    def logout(self):
        self.controller.destroy()
        call(["python", "login.py"])


# ==========================================Page de gestion des personnes ====================================
# ============================================================================================================
class PageTwo(tk.Frame):

    def __init__(self, window, controller):
        tk.Frame.__init__(self, window)
        self.controller = controller
        self.configure(bg="#b5c7de")
        controller.geometry("1366x768")
        controller.resizable(0, 0)
        controller.state("zoomed")

        button = tk.Button(self, text="Retour",
                               command=lambda: controller.show_frame("StartPage"))
        button.pack()
        # ---------Header de la fenetre------
        header = tk.Frame(self, bg='#00294B')
        header.place(x=300, y=0, width=1300, height=60)

        retourImage = Image.open('imagesIc\\retour.png')
        photo = ImageTk.PhotoImage(retourImage)
        retour = tk.Label(self, image=photo, bd=0)
        retour.image = photo
        retour.place(x=1460, y=15)

        retour_text = tk.Button(self, text='retour', bg='#b5c7de', font=("", 13, "bold"), bd=0, fg='#0D294B',
                                  cursor='hand2', activebackground='#b5c7de')
        retour_text.place(x=1500, y=15)

        # ----------------- Variable -------------

        id_var = tk.StringVar()
        nom_var = tk.StringVar()
        prenom_var = tk.StringVar()
        email_var = tk.StringVar()
        matricule_var = tk.StringVar()
        fonction_var = tk.StringVar()
        dell_var = tk.StringVar()
        se_by = tk.StringVar()
        se_var = tk.StringVar()
        # ----------------------------------
        # -----------------------------------
        # ---------Sidebar------------------
        sidebar = tk.Frame(self, bg='#e6f0ff')
        sidebar.place(x=0, y=0, width=300, height=850)

        # --------- time---------------
        clock_image = Image.open('imagesIc\\time.png')
        photo = ImageTk.PhotoImage(clock_image)
        date_time_image = tk.Label(sidebar, image=photo, bg='#e6f0ff')
        date_time_image.image = photo
        date_time_image.place(x=70, y=20)

        date_time = tk.Label(controller)
        date_time.place(x=130, y=20)
        self.show_time()

        date_time.configure(text=self.set_text, font=("", 13, "bold"), bd=0, bg='#e6f0ff', fg="#00294B")
        date_time.after(1000, self.show_time)


        # -----logo--------
        logoImage = Image.open('imagesIc\\logo2.png')
        photo = ImageTk.PhotoImage(logoImage)
        logo = tk.Label(sidebar, image=photo, bg='#e6f0ff')
        logo.image = photo
        logo.place(x=20, y=110)

        # -----Formulaire--------
        # Label
        tk.Label(text="Nom", font=("", 13, "bold"), fg="#0D294B").place(x=15, y=250)
        tk.Label(text="Prénom", font=("", 13, "bold"), fg="#0D294B").place(x=15, y=280)
        tk.Label(text="Email", font=("", 13, "bold"), fg="#0D294B").place(x=15, y=310)
        tk.Label(text="Matricule", font=("", 13, "bold"), fg="#0D294B").place(x=15, y=340)
        tk.Label(text="Fonction", font=("", 13, "bold"), fg="#0D294B").place(x=15, y=370)

        # Entry
        nom_entry = tk.Entry(sidebar, textvariable=id_var, font=("", 13, "bold"), fg="#0D294B", width=20)
        nom_entry.place(x=100, y=200)
        nom_entry = tk.Entry(sidebar, textvariable=nom_var, font=("", 13, "bold"), fg="#0D294B", width=20)
        nom_entry.place(x=100, y=250)
        prenom_entry = tk.Entry(sidebar, textvariable=prenom_var, font=("", 13, "bold"), fg="#0D294B",
                                  width=20)
        prenom_entry.place(x=100, y=280)
        email_entry = tk.Entry(sidebar, textvariable=email_var, font=("", 13, "bold"), fg="#0D294B",
                                 width=20)
        email_entry.place(x=100, y=310)
        matricule_entry = tk.Entry(sidebar, textvariable=matricule_var, font=("", 13, "bold"), fg="#0D294B",
                                     width=20)
        matricule_entry.place(x=100, y=340)

        # combobox

        combo_fonction = ttk.Combobox(sidebar, textvariable=fonction_var, )
        combo_fonction['value'] = ('Etudiant', 'Directeur', 'Professeur', 'Chef département', 'Scolarité')
        combo_fonction.place(x=100, y=370, width=185, height=24)

        # -----Buttons--------

        add_btn = tk.Button(sidebar, text='Ajouter', bg='#21951C', command=self.add_personne)
        add_btn.place(x=15, y=480, width='130', height='40')

        update_btn = tk.Button(sidebar, text='Modifier', bg='#1C9595', command=self.update)
        update_btn.place(x=150, y=480, width='130', height='40')

        del_btn = tk.Button(sidebar, text='Supprimer', bg='#AB111F', command=self.delete)
        del_btn.place(x=15, y=540, width='130', height='40')

        clear_btn = tk.Button(sidebar, text='Vider', bg='#A42A9F', command=self.clear)
        clear_btn.place(x=150, y=540, width='130', height='40')
        # ----------------------------------
        # -----------------------------------
        # --------- Le corps------------------

        heading = tk.Label(window, text='Gestion des personnes', font=("", 13, "bold"), fg='#0D294B',
                             bg='#eff5f6')
        heading.place(x=325, y=70)

        # --------- Frame TreeView------------------
        self.frame_treeview = tk.Frame(self, bg='#F7FAFA')
        self.frame_treeview.place(x=320, y=110, width=1250, height=640)

        self.personne_table = ttk.Treeview(self.frame_treeview,
                                           columns=('id', 'nom', 'prenom', 'email', 'matricule', 'fonction'))
        self.personne_table.place(x=10, y=20, width=1230, height=500)

        self.personne_table['show'] = 'headings'
        self.personne_table.heading('id', text='ID')
        self.personne_table.heading('nom', text='Nom')
        self.personne_table.heading('prenom', text='Prénom')
        self.personne_table.heading('email', text='Email')
        self.personne_table.heading('matricule', text='Matricule')
        self.personne_table.heading('fonction', text='Fonction')

        # Controler les dimension des colonnes
        self.personne_table.column('id', width=20)

        self.personne_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_all()
        # --------- fonctions------------------

    def show_time(self):
        timer = time.strftime("%H:%M:%S")
        dater = time.strftime('%Y/%m/%d')
        self.set_text = f"  {timer} \n {dater}"


    def clear(self):

        self.controller.nom_var.set('')
        self.controller.prenom_var.set('')
        self.controller.email_var.set('')
        self.controller.matricule_var.set('')
        self.controller.fonction_var.set('')

        # Récupérer les données

    def fetch_all(self):
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3308,
            database='smart_parking')
        cur = con.cursor()
        cur.execute('select * from personne')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.personne_table.delete(*self.personne_table.get_children())
            for row in rows:
                self.controller.personne_table.insert("", END, values=row)
            con.commit()
        con.close()

        # ----------------- Connexion et ajout -------------

    def add_personne(self):
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3308,
            database='smart_parking')
        cur = con.cursor()

        cur.execute("insert into personne values(%s,%s,%s,%s,%s,%s)", (

            self.controller.id_var.get(),
            self.controller.nom_var.get(),
            self.controller.prenom_var.get(),
            self.controller.email_var.get(),
            self.controller.matricule_var.get(),
            self.controller.fonction_var.get(),))

        con.commit()
        messagebox.showinfo("information", "L'ajout est effectué avec...")

        self.fetch_all()
        self.clear()
        con.close()

        # Vider

    def clear(self):
        self.controller.id_var.set('')
        self.controller.nom_var.set('')
        self.controller.prenom_var.set('')
        self.controller.email_var.set('')
        self.controller.matricule_var.set('')
        self.controller.fonction_var.set('')

        # Sélection

    def get_cursor(self, ev):
        cursor_row = self.controller.personne_table.focus()  # au moment du clique
        contents = self.controller.personne_table.item(
            cursor_row)  # Ramener ce que j'ai cliquer et mais le dans la variable contents
        # Récuperer les données que j'ai cliqué
        row = contents['values']
        # self.id_var.set(row[0])
        self.controller.id_var.set(row[0])
        self.controller.nom_var.set(row[1])
        self.controller.prenom_var.set(row[2])
        self.controller.email_var.set(row[3])
        self.controller.matricule_var.set(row[4])
        self.controller.fonction_var.set(row[5])

        # update

    def update(self):
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3308,
            database='smart_parking')
        cur = con.cursor()
        cur.execute("update personne set nom=%s, prenom=%s, email=%s, matricule=%s, fonction=%s WHERE id=%s", (

            self.controller.nom_var.get(),
            self.controller.prenom_var.get(),
            self.controller.email_var.get(),
            self.controller.matricule_var.get(),
            self.controller.fonction_var.get(),
            self.controller.id_var.get()))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        messagebox.showinfo("information", "La modification est effectué avec succès")

        # delete

    def delete(self):
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3308,
            database='smart_parking')
        cur = con.cursor()
        cur.execute("delete from personne WHERE id=%s", self.controller.id_var.get())
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        messagebox.showinfo("information", "La suppression est effectué avec succès")



if __name__ == "__main__":
    app = Dashboard()
    app.iconbitmap("images\IsaIt_icon.ico")
    app.mainloop()
    camera_controlle()
    plate_detection('capture_0.png')
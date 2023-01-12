from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
import pymysql

# ============= Connexion à la base de données (methode avec pymysql) ===================
def main():
   con = pymysql.connect(host="localhost",user="root",password="",database="smart_parking")
   cur = con.cursor()

   cur.execute("SELECT * FROM parking")
   result=cur.fetchall()
   for i in result:
        #id=i[0]
        capacite=[1]
        nbr_places_occ=[2]
        print (capacite,nbr_places_occ)
   cur.close()

# ============= Connexion à la base de données (methode avec sqlalchemy) ===================
 # IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
#from sqlalchemy import create_engine

# DEFINE THE DATABASE CREDENTIALS
#user = 'root'
#password = 'password'
#host = '127.0.0.1'
#port = 3306
#database = 'smart_parking'


# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
#def get_connection():
    #return create_engine(
        #url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            #user, password, host, port, database
        #)
    #)

#if __name__ == '__main__':

    #try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        #engine = get_connection()
        #print(
            #f"Connection to the {host} for user {user} created successfully.")
    #except Exception as ex:
        #print("Connection could not be made due to the following error: \n", ex)
# ============= Fin de Connexion à la base de données (sqlalchemy) ===================



class Dashboard2:

    def __init__(self, window):
        self.window = window
        self.window.title("Smart Parking System")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        # Window Icon Photo
        icon = PhotoImage(file='C:\\Users\\Destock\\Desktop\\Modules_S9\\ConduiteDeProjet_Rakrak\\LogoApp1.png')
        self.window.iconphoto(True, icon)

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        self.header = Frame(self.window, bg='#0D294B')
        self.header.place(x=0, y=0, width=1550, height=60)

        #self.logout_text = Button(self.header, text="Se déconnecter", bg='green', font=("", 13, "bold"), bd=0, fg='white',cursor='hand2', activebackground='red')
        #self.logout_text.place(x=1090, y=15)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=60, width=350, height=840)

        # ================== BODY ===================================================
        con = pymysql.connect(host="localhost", user="root", password="", database="smart_parking")
        cur = con.cursor()

        cur.execute("SELECT * FROM parking")
        result = cur.fetchall()
        for i in result:
            # id=i[0]
            capacite = i[1]
            nbr_places_occ = i[2]
            #print("La capacite:",capacite, nbr_places_occ)
            self.heading = Label(self.window, text="Capacité du parking", font=("Calibri", 50, "bold"), fg='#0D294B', bg='#eff5f6')
            self.heading.place(x=600, y=120)
            self.heading = Label(self.window, text=capacite, font=("Calibri", 50, ""), fg='yellow', bg='#eff5f6')
            self.heading.place(x=810, y=270)

            self.heading = Label(self.window, text="Nombre de places occupées", font=("Calibri", 50, "bold"), fg='#0D294B', bg='#eff5f6')
            self.heading.place(x=500, y=500)
            self.heading = Label(self.window, text=nbr_places_occ, font=("Calibri", 50, ""), fg='yellow', bg='#eff5f6')
            self.heading.place(x=850, y=650)
        cur.close()

        # ================== END BODY ===================================================


        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        #self.heading = Label(self.window, text='Gestion des matricules', font=("", 15, "bold"), fg='darkblue', bg='#eff5f6')
        #self.heading.place(x=325, y=70)

        #self.Nom = Label(self.window, text='Nom', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        #self.Nom.place(x=500, y=300)

        #self.Prénom = Label(self.window, text='Prénom', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        #self.Prénom.place(x=500, y=360)

        #self.name = Label(self.window, text='C.I.N', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        #self.name.place(x=500, y=420)

        #self.Fonction = Label(self.window, text='Fonction', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        #self.Fonction.place(x=500, y=480)

        #self.Adresse = Label(self.window, text='Adresse', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        #self.Adresse.place(x=500, y=540)

        #self.Matricule = Label(self.window, text='Matricule', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        #self.Matricule.place(x=500, y=600)

        #NomValue = StringVar
        #PrénomValue = StringVar
        #CINValue = StringVar
        #FonctionValue = StringVar
        #AdresseValue = StringVar
        #MatriculeValue = StringVar


        #NomEntry = Entry(self.window, textvariable = NomValue)
        #PrénomEntry = Entry(self.window, textvariable = PrénomValue)
        #CINEntry = Entry(self.window, textvariable = CINValue)
        #FonctionEntry = Entry(self.window, textvariable = FonctionValue)
        #AdresseEntry = Entry(self.window, textvariable = AdresseValue)
        #MatriculeEntry = Entry(self.window, textvariable = MatriculeValue)

        #NomEntry.place(x=700, y=300, width=700, height=30)
        #PrénomEntry.place(x=700, y=360, width=700, height=30)
        #CINEntry.place(x=700, y=420, width=700, height=30)
        #FonctionEntry.place(x=700, y=480, width=700, height=30)
        #AdresseEntry.place(x=700, y=540, width=700, height=30)
        #MatriculeEntry.place(x=700, y=600, width=700, height=30)
        
        #self.ajouter = Button(self.window, text="Ajouter", bg='green', font=("", 13, "bold"), bd=0, fg='white',cursor='hand2', activebackground='darkgreen')
        #self.ajouter.place(x=600, y=720, width=90, height=30)

        #self.modifier = Button(self.window, text="Modifier", bg='orange', font=("", 13, "bold"), bd=0, fg='white',cursor='hand2', activebackground='darkorange')
        #self.modifier.place(x=900, y=720, width=90, height=30)

        #self.supprimer = Button(self.window, text="Supprimer", bg='red', font=("", 13, "bold"), bd=0, fg='white',cursor='hand2', activebackground='darkred')
        #self.supprimer.place(x=1180, y=720, width=100, height=30)

        #messagebox.showinfo()

        # body frame 1
        # self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        # self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        # self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        # self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # body frame 3
        # self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        # self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # body frame 4
        # self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        # self.bodyFrame4.place(x=1030, y=495, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        #self.logoImage = ImageTk.PhotoImage(file='C:\\Users\\Destock\\team06.jpg')
        #self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        #self.logo.place(x=60, y=70)

        # Name of person
        #self.brandName = Label(self.sidebar, text='Administrateur', bg='#ffffff', font=("", 15, "bold"))
        #self.brandName.place(x=80, y=230)

        # Dashboard
        #self.dashboardImage = ImageTk.PhotoImage(file='')
        #self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        #self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Gestion des utilisateurs", bg='#ffffff', font=("Calibri", 18, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=287)

        # Manage
        #self.manageImage = ImageTk.PhotoImage(file='')
        #self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        #self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text="Gestion des matricules", bg='#ffffff', font=("Calibri", 18, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = ImageTk.PhotoImage(file='C:\\Users\\Destock\\Desktop\\Modules_S9\\ConduiteDeProjet_Rakrak\\place.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=16, y=402)

        self.settings_text = Button(self.sidebar, text="Gestion de places", bg='#b5c7de', font=("Calibri", 18, "bold"), bd=0,
                                    cursor='hand2', activebackground='#b5c7de')
        self.settings_text.place(x=80, y=402)

        # Exit
        #self.ExitImage = ImageTk.PhotoImage(file='C:\\Users\\Destock\\.png')
        #self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        #self.Exit.place(x=25, y=452)

        self.Exit_text = Button(self.sidebar, text="Historique", bg='#ffffff', font=("Calibri", 18, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff')
        self.Exit_text.place(x=85, y=462)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        # self.pieChart_image = ImageTk.PhotoImage(file='C:\\Users\\Destock\\pie-graph1.png')
        # self.pieChart = Label(self.bodyFrame1, image=self.pieChart_image, bg='#ffffff')
        # self.pieChart.place(x=690, y=70)

        # Graph
        # self.graph_image = ImageTk.PhotoImage(file='C:\\Users\\Destock\\graph.png')
        # self.graph = Label(self.bodyFrame1, image=self.graph_image, bg='#ffffff')
        # self.graph.place(x=40, y=70)

        # Body Frame 2
        # self.total_people = Label(self.bodyFrame2, text='230', bg='#009aa5', font=("", 25, "bold"))
        # self.total_people.place(x=120, y=100)

        # self.totalPeopleImage = ImageTk.PhotoImage(file='C:\\Users\\Destock\\left-icon.png')
        # self.totalPeople = Label(self.bodyFrame2, image=self.totalPeopleImage, bg='#009aa5')
        # self.totalPeople.place(x=220, y=0)

        # self.totalPeople_label = Label(self.bodyFrame2, text="Total People", bg='#009aa5', font=("", 12, "bold"),
        #                                fg='white')
        # self.totalPeople_label.place(x=5, y=5)

        # Body Frame 3
        # self.people_left = Label(self.bodyFrame3, text='50', bg='#e21f26', font=("", 25, "bold"))
        # self.people_left.place(x=120, y=100)

        # left icon
        # self.LeftImage = ImageTk.PhotoImage(file='C:\\Users\\Destock\\left-icon.png')
        # self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#e21f26')
        # self.Left.place(x=220, y=0)

        # self.peopleLeft_label = Label(self.bodyFrame3, text="Left", bg='#e21f26', font=("", 12, "bold"),
        #                               fg='white')
        # self.peopleLeft_label.place(x=5, y=5)

        # Body Frame 4
        # self.total_earnings = Label(self.bodyFrame4, text='$40,000.00', bg='#ffcb1f', font=("", 25, "bold"))
        # self.total_earnings.place(x=80, y=100)

        # self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#ffcb1f', font=("", 12, "bold"),
        #                             fg='white')
        # self.earnings_label.place(x=5, y=5)
        # Frame 4 icon
        # self.earningsIcon_image = ImageTk.PhotoImage(file='C:\\Users\\Destock\\earn3.png')
        # self.earningsIcon = Label(self.bodyFrame4, image=self.earningsIcon_image, bg='#ffcb1f')
        # self.earningsIcon.place(x=220, y=0)

        #logo of app
        self.logo_image = ImageTk.PhotoImage(file="C:\\Users\\Destock\\Desktop\\Modules_S9\\ConduiteDeProjet_Rakrak\\LogoApp1.png")
        self.logo_image1 = Label(self.sidebar, image=self.logo_image, bg="white")
        self.logo_image1.place(x=10, y=20)

        # date and Time
        #self.clock_image = ImageTk.PhotoImage(file="C:\\Users\\Destock\\time.png")
        #self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        #self.date_time_image.place(x=88, y=160)

        self.date_time = Label(self.window)
        self.date_time.place(x=110, y=220)
        self.show_time()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%d/%m/%Y')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("Calibri", 16, "bold"), bd=0, bg="white", fg="#b5c7de")
        self.date_time.after(100, self.show_time)


def wind():
       window = Tk()
       Dashboard2(window)
       window.mainloop()


if __name__ == '__main__':
       wind()

from tkinter import *
import mysql
from mysql import connector
import pymysql


# ============= Connexion à la base de données (methode avec pymysql) ===================
def main():
    con = pymysql.connect(host="localhost", port=3308, user="root", password="", database="smart_parking")
    cur = con.cursor()

    cur.execute("SELECT * FROM parking")
    result = cur.fetchall()
    for i in result:
        # id=i[0]
        capacite = [1]
        nbr_places_occ = [2]
        print(capacite, nbr_places_occ)
    cur.close()
class Dashboard2:

    def __init__(self, window):
        self.window = window
        self.window.title("Smart Parking System")
        self.window.geometry("1100x768")
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.config(background='#eff5f6')

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        self.header = Frame(self.window, bg='#0D294B')
        self.header.place(x=0, y=0, width=1550, height=60)

        self.logout_btn = Button(self.header, text="Se déconnecter", bg='#b5c7de',
                                 font=("'Microsoft Yahei'", 13, "bold"), bd=0, fg='white',
                                 pady=10, width=50, cursor='hand2', activebackground='#476d9e')
        self.logout_btn.place(x=800, y=12)

        # ================== BODY ===================================================
        con = pymysql.connect(host="localhost", port=3308, user="root", password="", database="smart_parking")
        cur = con.cursor()
        cur.execute("SELECT * FROM parking")
        result = cur.fetchall()
        for i in result:
            # id=i[0]
            capacite = i[1]
            nbr_places_occ = i[2]
            self.heading = Label(self.window, text="Capacité du parking", font=("Calibri", 50, "bold"), fg='#0D294B',
                                 bg='#eff5f6')
            self.heading.place(x=600, y=120)
            self.heading = Label(self.window, text=capacite, font=("Calibri", 50, ""), fg='yellow', bg='#eff5f6')
            self.heading.place(x=810, y=270)

            self.heading = Label(self.window, text="Nombre de places occupées", font=("Calibri", 50, "bold"),
                                 fg='#0D294B', bg='#eff5f6')
            self.heading.place(x=500, y=500)
            self.heading = Label(self.window, text=nbr_places_occ, font=("Calibri", 50, ""), fg='yellow', bg='#eff5f6')
            self.heading.place(x=850, y=650)
            cur.close()

def wind():
    window = Tk()
    window.iconbitmap("images\IsaIt_icon.ico")
    Dashboard2(window)
    window.mainloop()


if __name__ == '__main__':
    wind()

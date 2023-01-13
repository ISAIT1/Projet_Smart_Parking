from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
import os
from datetime import * 
import time
from tkinter import messagebox
import pymysql

class users:
    def __init__(self, window):
        self.window = window
        
        self.window.title("Gestion des personnes ")
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background='#b5c7de')

        #file_path = os.path.dirname(os.path.realpath(__file__))
        #image_1 = customtkinter.CTkImage(Image.open(file_path+'imagesIc/search_icon.png'), size=(35,35))


        #----------------------------------
        #-----------------------------------
        #---------icon de la fenetre------
        icon =PhotoImage(file='imagesIc\\parking.png')
        self.window.iconphoto(True, icon)


        #---------Header de la fenetre------
        self.header = Frame(self.window, bg='#00294B')
        self.header.place(x=300, y=0,width=1300, height=60)

        self.retourImage = Image.open('imagesIc\\retour.png')
        photo = ImageTk.PhotoImage(self.retourImage)
        self.retour = Label(self.window, image=photo, bd=0 )
        self.retour.image = photo
        self.retour.place(x=1460, y=15)

        self.retour_text = Button(self.window, text='retour', bg='#b5c7de', font=("",13,"bold"), bd=0, fg='#0D294B',
        cursor='hand2', activebackground='#b5c7de')

        self.retour_text.place(x=1500, y=15)


        #----------------- Variable -------------
        
        self.id_var=StringVar()
        self.nom_var=StringVar()
        self.prenom_var=StringVar()
        self.email_var=StringVar()
        self.matricule_var=StringVar()
        self.fonction_var=StringVar()
        self.dell_var=StringVar()
        self.se_by=StringVar() 
        self.se_var=StringVar() 

        #----------------------------------
        #-----------------------------------
        #---------Sidebar------------------
        self.sidebar = Frame(self.window, bg='#F7FAFA')
        self.sidebar.place(x=0, y=0,width=300, height=750)

              #--------- time---------------
        self.clock_image = Image.open('imagesIc\\time.png')
        photo = ImageTk.PhotoImage(self.clock_image)
        self.date_time_image= Label(self.sidebar, image=photo)
        self.date_time_image.image = photo
        self.date_time_image.place(x=70,y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=130, y=20)
        self.show_time()


        self.date_time.configure(text=self.set_text,font=("",13,"bold"), bd=0, bg="#F7FAFA", fg="#00294B")
        self.date_time.after(1000, self.show_time)

              #-----logo--------
        self.logoImage = Image.open('imagesIc\\logo2.jpg')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo)
        self.logo.image = photo
        self.logo.place(x=20, y=110)

               #-----Formulaire--------
        #Label
        Label(text="PersonID", font=("",13,"bold"), fg="#0D294B").place(x=15,y=250)
        Label(text="Nom", font=("",13,"bold"), fg="#0D294B").place(x=15,y=280)
        Label(text="Prénom", font=("",13,"bold"), fg="#0D294B").place(x=15,y=310)
        Label(text="Email", font=("",13,"bold"), fg="#0D294B").place(x=15,y=340)
        Label(text="Matricule", font=("",13,"bold"), fg="#0D294B").place(x=15,y=370)
        Label(text="Fonction", font=("",13,"bold"), fg="#0D294B").place(x=15,y=400)

        #Entry
        self.id_entry = Entry(self.sidebar,textvariable=self.id_var, font=("",10,"bold"), fg="#0D294B", width=26)
        self.id_entry.place(x=100, y=250)
        self.nom_entry = Entry(self.sidebar,textvariable=self.nom_var, font=("",10,"bold"), fg="#0D294B", width=26)
        self.nom_entry.place(x=100, y=280)
        self.prenom_entry = Entry(self.sidebar,textvariable=self.prenom_var, font=("",10,"bold"), fg="#0D294B", width=26)
        self.prenom_entry.place(x=100, y=310)
        self.email_entry = Entry(self.sidebar,textvariable=self.email_var, font=("",10,"bold"), fg="#0D294B", width=26)
        self.email_entry.place(x=100, y=340)
        self.matricule_entry = Entry(self.sidebar,textvariable=self.matricule_var, font=("",10,"bold"), fg="#0D294B", width=26)
        self.matricule_entry.place(x=100, y=370)
           #combobox

        #lst = ['Etudiant','Directeur','Professeur','Chef département','Scolarité']


        combo_fonction=ttk.Combobox(self.sidebar,textvariable=self.fonction_var,)
        combo_fonction['value']=('Etudiant','Directeur','Professeur','Chef département','Scolarité')
        combo_fonction.place(x=100, y=400, width=185, height=20)
        #combo_fonction.pack()
        


        #-----Buttons--------

        add_btn=Button(self.sidebar, text='Ajouter', bg='#21951C', command=self.add_personne)
        add_btn.place(x=15,y=480, width='130',height='40')

        update_btn=Button(self.sidebar, text='Modifier', bg='#1C9595', command=self.update)
        update_btn.place(x=150,y=480, width='130',height='40')

        del_btn=Button(self.sidebar, text='Supprimer', bg='#AB111F', command=self.delete)
        del_btn.place(x=15,y=540, width='130',height='40')

        clear_btn=Button(self.sidebar, text='Vider', bg='#A42A9F', command=self.clear)
        clear_btn.place(x=150,y=540, width='130',height='40')
      
        exit_btn=Button(self.window, text='Quitter', bg='#EDAD13', command=self.iExit)
        exit_btn.place(x=70,y=660, width='160',height='25')


        #----------------------------------
        #-----------------------------------
        #--------- Le corps------------------

        self.heading = Label(self.window, text='Gestion des personnes',font=("",13,"bold"), fg='#0D294B', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        #--------- Frame TreeView------------------
        self.frame_treeview = Frame(self.window, bg='#F7FAFA')
        self.frame_treeview.place(x=320, y=110,width=1250, height=640)

        self.personne_table=ttk.Treeview(self.frame_treeview,columns=('id','nom','prenom','email','matricule','fonction'))
        self.personne_table.place(x=10,y=20,width=1230, height=500)

        self.personne_table['show']='headings'
        self.personne_table.heading('id', text='ID')
        self.personne_table.heading('nom', text='Nom')
        self.personne_table.heading('prenom', text='Prénom')
        self.personne_table.heading('email', text='Email')
        self.personne_table.heading('matricule', text='Matricule')
        self.personne_table.heading('fonction', text='Fonction')

                 #Controler les dimension des colonnes
        self.personne_table.column('id',width=20)


        self.personne_table.bind("<ButtonRelease-1>",self.get_cursor)
       

    #----------------------------------
    #-----------------------------------
    #--------- fonctions------------------
    
        self.fetch_all()
    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date=time.strftime("%y/%m/%d")
        self.set_text = f"{self.time} \n{self.date}"

    def clear(self):
        
        self.nom_var.set('')
        self.prenom_var.set('')
        self.email_var.set('')
        self.matricule_var.set('')
        self.fonction_var.set('')

    #Récupérer les données   
    def fetch_all(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor()
        cur.execute('select * from personne')
        rows = cur.fetchall()
        if len (rows) !=0:
            self.personne_table.delete(*self.personne_table.get_children())
            for row in rows:
                self.personne_table.insert("",END, values=row)
            con.commit()
        con.close() 


    #----------------- Connexion et ajout -------------
        
    def add_personne(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor()

        cur.execute("insert into personne values(%s,%s,%s,%s,%s,%s)",(
            
            self.id_var.get(),
            self.nom_var.get(),
            self.prenom_var.get(),
            self.email_var.get(),
            self.matricule_var.get(),
            self.fonction_var.get(), ))

        con.commit()
        messagebox.showinfo("information", "L'ajout est effectué avec...")

        self.fetch_all()
        self.clear()
        con.close()
    #Vider
    def clear(self):
        self.id_var.set('')
        self.nom_var.set('')
        self.prenom_var.set('')
        self.email_var.set('')
        self.matricule_var.set('')
        self.fonction_var.set('')

    #Sélection
    def get_cursor(self,ev):
        cursor_row = self.personne_table.focus() #au moment du clique
        contents = self.personne_table.item(cursor_row) #Ramener ce que j'ai cliquer et mais le dans la variable contents
        #Récuperer les données que j'ai cliqué
        row= contents['values'] 
        #self.id_var.set(row[0])
        self.id_var.set(row[0])
        self.nom_var.set(row[1])
        self.prenom_var.set(row[2])
        self.email_var.set(row[3])
        self.matricule_var.set(row[4])
        self.fonction_var.set(row[5])

    #update
    def update(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor()
        cur.execute("update personne set nom=%s, prenom=%s, email=%s, matricule=%s, fonction=%s WHERE id=%s",(
                    
        self.nom_var.get(),
        self.prenom_var.get(),
        self.email_var.get(),
        self.matricule_var.get(),
        self.fonction_var.get(), 
        self.id_var.get() ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        messagebox.showinfo("information", "La modification est effectué avec succès")

        
    #delete
    def delete(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor()
        cur.execute("delete from personne WHERE id=%s",self.id_var.get())
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        messagebox.showinfo("information", "La suppression est effectué avec succès")

    
    def iExit(self):
        iExit = messagebox.showinfo("information", "êtes vous sur!")
        
        self.window.destroy()




def win():
    window = Tk()
    users(window)
    window.mainloop()

if __name__ == '__main__':
    win()



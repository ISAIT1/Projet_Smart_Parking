from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Matricule:
    #----------------- Fenetre -------------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x768')
        #self.root.geometry('1366x768')
        #self.root.state('zoomed')
        self.root.title('Gestion des matricules')
        self.root.configure(background="#B2BABB")
        self.root.resizable(False,False)
        title = Label(self.root ,
        text=' -- SMART PARKING --',
        bg="#283747",
        font=('monospace',14),
        fg='white'
        )
        title.pack(fill=X)

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

        #----------------- Tools -------------
        Manage_Frame = Frame(self.root, bg='white')
        Manage_Frame.place(x=2, y=30,width=210,height=400)

        lbl_name=Label(Manage_Frame, bg='white', text="Nom")
        lbl_name.pack()
        name_Entry=Entry(Manage_Frame,textvariable=self.nom_var, bd='2')
        name_Entry.pack()

        lbl_prenom=Label(Manage_Frame, bg='white', text="Prénom")
        lbl_prenom.pack()
        prenom_Entry=Entry(Manage_Frame,textvariable=self.prenom_var, bd='2')
        prenom_Entry.pack()

        lbl_email=Label(Manage_Frame, bg='white', text="Email")
        lbl_email.pack()
        email_Entry=Entry(Manage_Frame,textvariable=self.email_var, bd='2')
        email_Entry.pack()

        lbl_matricule=Label(Manage_Frame, bg='white', text="Matricule")
        lbl_matricule.pack()
        matricule_Entry=Entry(Manage_Frame,textvariable=self.matricule_var, bd='2')
        matricule_Entry.pack()

        lbl_fonction=Label(Manage_Frame, bg='white', text="Fonction")
        lbl_fonction.pack()


        combo_fonction=ttk.Combobox(Manage_Frame,textvariable=self.fonction_var,)
        combo_fonction['value']=('Etudiant','Directeur','Professeur','Chef département','Scolarité')
        combo_fonction.pack()

   
        
        lbl_sup=Label(Manage_Frame, bg='#ffddcc', text="Entrer le nom pour supprimer")
        lbl_sup.pack()
        delete_Entry = Entry(Manage_Frame, textvariable=self.dell_var,bd='2')
        delete_Entry.pack()

        #----------------- Button -------------
        btn_Frame = Frame(self.root, bg='white')
        btn_Frame.place(x=2, y=435,width=210, height='200')

        title1 = Label(btn_Frame, text="Gestion des personnes", font=('Deco,14'), fg='white',bg='#283747')
        title1.pack(fill=X)

        add_btn=Button(btn_Frame, text='Ajouter', bg='#B2BABB',command=self.add_personne)
        add_btn.place(x=33,y=33, width='150',height='30')

        del_btn=Button(btn_Frame, text='Supprimer', bg='#B2BABB', command=self.delete)
        del_btn.place(x=33,y=63, width='150',height='30')

        update_btn=Button(btn_Frame, text='Modifier', bg='#B2BABB', command=self.update)
        update_btn.place(x=33,y=93, width='150',height='30')

        clear_btn=Button(btn_Frame, text='Vider', bg='#B2BABB', command=self.clear)
        clear_btn.place(x=33,y=123, width='150',height='30')

        exit_btn=Button(btn_Frame, text='Quitter', bg='#B2BABB')
        exit_btn.place(x=33,y=153, width='150',height='30')
        
        #----------------- Search -------------
        search_Frame= Frame(self.root, bg='white')
        search_Frame.place(x=220,y=30,width=1260,height=50)
        
        lbl_search=Label(search_Frame, text='Recherche', bg='white')
        lbl_search.place(x=40,y=12)

        combo_search=ttk.Combobox(search_Frame)
        combo_search['value']=('nom','email','matricule')
        combo_search.place(x=130,y=12)

        search_Entry = Entry(search_Frame,textvariable=self.se_var,bd='2')
        search_Entry.place(x=280,y=12)

        se_btn = Button(search_Frame, text='Chercher',bg='#B2BABB',command=self.search)
        se_btn.place(x=420,y=12, width=100, height=23)

        re_btn = Button(search_Frame, text='retour',bg='#B2BABB',command=self.retour)
        re_btn.place(x=1050,y=12, width=100, height=23)



        #----------------- Résultats -------------
        resultats_Frame=Frame(self.root, bg='white')
        resultats_Frame.place(x=220,y=84, width=1260,height=600)
            # ---------- Scroll---------
        #scroll_x=Scrollbar(resultats_Frame, orient=HORIZONTAL)
        #scroll_y=Scrollbar(resultats_Frame,orient=VERTICAL)
            # ---------- Treeview---------
        self.personne_table=ttk.Treeview(resultats_Frame,
        columns=('id','nom','prenom','email','matricule','fonction'),
        #xscrollcommand=scroll_x.set,
        #yscrollcommand=scroll_y.set
        )
        self.personne_table.place(x=18,y=1,width=1230, height=500)
        #scroll_x.pack(side=BOTTOM, fill=X)
        #scroll_y.pack(side=RIGHT, fill=Y)
        #scroll_x.config(command=self.personne_table.xview)
        #scroll_y.config(command=self.personne_table.yview)

        self.personne_table['show']='headings'
        self.personne_table.heading('id', text='ID')
        self.personne_table.heading('nom', text='Nom')
        self.personne_table.heading('prenom', text='Prénom')
        self.personne_table.heading('email', text='Email')
        self.personne_table.heading('matricule', text='Matricule')
        self.personne_table.heading('fonction', text='Fonction')

        #Controler les dimension des colonnes
        self.personne_table.column('id',width=20)
        #self.personne_table.column('nom',width=125)
        #self.personne_table.column('prenom',width=30)
        #self.personne_table.column('email',width=65)
        #self.personne_table.column('matricule',width=65)
        #self.personne_table.column('fonction',width=125)

        self.personne_table.bind("<ButtonRelease-1>",self.get_cursor)



        
        
        #----------------- Connexion et ajout -------------
        self.fetch_all()

    
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

    #------- Récupérer les données   
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

    def delete(self): 
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor() 
        cur.execute('delete from personne where nom=%s',self.dell_var.get())
        messagebox.showinfo("information", "La suppression est bien réussi...")
        con.commit()
        self.fetch_all()
        con.close()

    def clear(self):
        
        self.nom_var.set('')
        self.prenom_var.set('')
        self.email_var.set('')
        self.matricule_var.set('')
        self.fonction_var.set('')
        
    def get_cursor(self,ev):
        cursor_row = self.personne_table.focus() #au moment du clique
        contents = self.personne_table.item(cursor_row) #Ramener ce que j'ai cliquer et mais le dans la variable contents
        #Récuperer les données que j'ai cliqué
        row= contents['values'] 
        #self.id_var.set(row[0])
        self.nom_var.set(row[1])
        self.prenom_var.set(row[2])
        self.email_var.set(row[3])
        self.matricule_var.set(row[4])
        self.fonction_var.set(row[5])

    def update(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor()

        cur.execute("UPDATE personne SET nom=%s, prenom=%s, email=%s, matricule=%s, fonction=%s WHERE id=%s", (
            
            self.id_var.get(),
            self.nom_var.get(),
            self.prenom_var.get(),
            self.email_var.get(),
            self.matricule_var.get(),
            self.fonction_var.get() 
             ))

        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    #-------recherche--------
    def search(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_parking')
        cur=con.cursor()
        cur.execute("select * from personne where " +
        str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
        
        rows = cur.fetchall()
        if len (rows) !=0:
            self.personne_table.delete(*self.personne_table.get_children())
            for row in rows:
                self.personne_table.insert("",END, values=row)
            con.commit()
        con.close() 
    #-------retour--------
    def retour(self):
        win =Toplevel()
        self.int1(win)
        self.root.withraw()
        win.deiconify()



root = Tk()
ob= Matricule(root)
root.mainloop()


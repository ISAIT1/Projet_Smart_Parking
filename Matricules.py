from tkinter import *
from tkinter import ttk

class Matricule:
    #----------------- Fenetre -------------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768')
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

        self.nom_var=StringVar()
        self.prenom_var=StringVar()
        self.email_var=StringVar()
        self.fonction_var=StringVar()
        self.matricule_var=StringVar()
        self.se_var=StringVar()
        self.dell_var=StringVar()

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


        lbl_fonction=Label(Manage_Frame, bg='white', text="Fonction")
        lbl_fonction.pack()
        combo_fonction=ttk.Combobox(Manage_Frame,textvariable=self.fonction_var,)
        combo_fonction['value']=('Etudiant','Directeur','Professeur','Chef département','Scolarité')
        combo_fonction.pack()

        lbl_matricule=Label(Manage_Frame, bg='white', text="Matricule")
        lbl_matricule.pack()
        matricule_Entry=Entry(Manage_Frame, bd='2')
        matricule_Entry.pack()
        
        lbl_sup=Label(Manage_Frame, bg='#ffddcc', text="Entrer le nom pour supprimer")
        lbl_sup.pack()
        delete_Entry = Entry(Manage_Frame, textvariable=self.dell_var,bd='2')
        delete_Entry.pack()

        #----------------- Button -------------
        btn_Frame = Frame(self.root, bg='white')
        btn_Frame.place(x=2, y=435,width=210, height='200')

        title1 = Label(btn_Frame, text="Gestion des personnes", font=('Deco,14'), fg='white',bg='#283747')
        title1.pack(fill=X)

        add_btn=Button(btn_Frame, text='Ajouter', bg='#B2BABB')
        add_btn.place(x=33,y=33, width='150',height='30')

        del_btn=Button(btn_Frame, text='Supprimer', bg='#B2BABB')
        del_btn.place(x=33,y=63, width='150',height='30')

        update_btn=Button(btn_Frame, text='Modifier', bg='#B2BABB')
        update_btn.place(x=33,y=93, width='150',height='30')

        clear_btn=Button(btn_Frame, text='Vider', bg='#B2BABB')
        clear_btn.place(x=33,y=123, width='150',height='30')

        exit_btn=Button(btn_Frame, text='Quitter', bg='#B2BABB')
        exit_btn.place(x=33,y=153, width='150',height='30')
        
        #----------------- Search -------------
        search_Frame= Frame(self.root, bg='white')
        search_Frame.place(x=220,y=30,width=1134,height=50)
        
        lbl_search=Label(search_Frame, text='Recherche', bg='white')
        lbl_search.place(x=40,y=12)

        combo_search=ttk.Combobox(search_Frame)
        combo_search['value']=('nom','email','matricule')
        combo_search.place(x=130,y=12)

        search_Entry = Entry(search_Frame,textvariable=self.se_var,bd='2')
        search_Entry.place(x=280,y=12)

        se_btn = Button(search_Frame, text='Cherccher',bg='#B2BABB')
        se_btn.place(x=420,y=12, width=100, height=23)

        #----------------- Résultats -------------
        resultats_Frame=Frame(self.root, bg='white')
        resultats_Frame.place(x=220,y=84, width=1100,height=560)
            # ---------- Scroll---------
        scroll_x=Scrollbar(resultats_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(resultats_Frame,orient=VERTICAL)
            # ---------- Treeview---------
        self.personne_table=ttk.Treeview(resultats_Frame,
        columns=('nom','prenom','email','fonction','matricule'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )
        self.personne_table.place(x=18,y=1,width=1080, height=480)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.personne_table.xview)
        scroll_y.config(command=self.personne_table.yview)

        self.personne_table['show']='headings'
        
        self.personne_table.heading('nom', text='Nom')
        self.personne_table.heading('prenom', text='Prénom')
        self.personne_table.heading('email', text='Email')
        self.personne_table.heading('fonction', text='Fonction')
        self.personne_table.heading('matricule', text='Matricule')
        


root = Tk()
ob= Matricule(root)
root.mainloop()


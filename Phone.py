#! -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
from threading import *
import socket, time
import datetime, random
from pygame import mixer
import webbrowser
to=datetime.datetime.now()
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
n=socket.gethostbyname(socket.gethostname())
adr=('localhost', 2019)

statut=False

class Mere:
    def __init__(self):
        self.echo=""
    def affiche(self, num):
        self.num=num
        #self.no=self.texta.insert(END, self.num)
        return self.num
    def nopl(self):
        a='jdjdj'


class Graphik(Mere):
    def __init__(self, nom, titre, taille):
        self.nom=nom
        self.titre=titre
        self.taille=taille
        self.nom=Tk()
        self.nom.title(str(self.titre))
        self.nom.geometry((self.taille))
        self.bmenu=Menu(self.nom, activeforeground='cyan', activeborderwidth=2, selectcolor='orange', borderwidth=2, fg='green', bg='white', font=('arial', 13, 'bold'))
        self.menuf1=Menu(self.bmenu, tearoff=0, selectcolor='orange', title='NOPLI',)
        self.menuf2=Menu(self.bmenu, tearoff=0)
        self.menuf3=Menu(self.bmenu, tearoff=0)
        self.bmenu.add_cascade(label='Fichier', state=NORMAL, underline=0, compound='bottom', menu=self.menuf1)
        self.bmenu.add_cascade(label='A propos', underline=0, compound='bottom', menu=self.menuf2)
        self.bmenu.add_cascade(label='Aide', underline=0, compound='bottom', menu=self.menuf3)
        self.smenu = Menu(self.menuf1, tearoff=1)
        self.smenu.add_command(label='Non Securisée avec ECC', underline=0, command='') #associer la fonction notifiant en haut que la connexion n'est pas securisée
        self.smenu.add_command(label='Securisée avec ECC', underline=0, command='') # associer la fonction de cryptage des msg affichant en haut que la communication est securisée
        self.menuf1.add_cascade(label='type de communication', menu=self.smenu)
        self.menuf1.add_command(label='Enregistrer l historique', underline=0, command='') #associer la fonction d'erregistrement des msg dans un fichier texte
        self.menuf1.add_separator() #Je separe avec une ligne
        self.menuf1.add_command(label='Quitter', underline=1, command=self.nom.destroy) #commande pour fermer la fenetre en cours
        self.menuf2.add_command(label='Ce logiciel', underline=0, command='') #fonction donnant l'aide sur l'application
        self.menuf2.add_command(label='A propos de l\'auteur', underline=0, command='') # fonction donnant l'information sur moi
        self.menuf3.add_command(label='information en ligne', underline=0, command=self.web) #fonction donnant l'information en ligne sur ce produit, ici je vais ouvrir la page du navigateur contenant l'adresse de mon site
        self.menuf3.add_command(label='Nous Contacter', underline=0, command='')
        self.texta=Text(self.nom, width='30',height='50', bg='black', fg='green',bd=30, state=NORMAL, font=('Amperzand', 11, 'bold')) #l'espace des échanges de communication
        #self.menuf1.post(x=420, y=585)
        self.statut=False
        self.gard=False
        #self.texta.insert(END, 'Attente de connexion ...\t')### ici
        #####################################################################################################"""

        ####################################################################################################
        self.texta.place(x=8, y=5, width=477, height=470) # Position
        #self.but=Button(self.nom, image=self.photo,bd=5, command="") #boutton pour envoyer les messages
        #self.but.place(x=8, y=570, width=90, height=90)
        ecriture=('Tw Cen MT Condensed Extra Bold', 12)
        self.but1=Button(self.nom, text='Voix', font=ecriture, highlightcolor='green', state=DISABLED, highlightthickness=4, highlightbackground='yellow',activebackground='yellow', bg="orange", bd=3, command=self.voix)
        self.but1.place(x=8, y=485, width=70, height=30)
        self.but2=Button(self.nom, text='Video', font=ecriture, state=DISABLED, activebackground='yellow', bg="orange", bd=3,command='')
        self.but2.place(x=90, y=485, width=70, height=30)
        self.but3=Button(self.nom, text='Text', font=ecriture, state=DISABLED, activebackground='yellow', bg="orange", bd=3, command=self.texte)
        self.but3.place(x=172, y=485, width=70, height=30)
        self.but4=Button(self.nom, text='Historique', font=ecriture, state=DISABLED, activebackground='orange', bg="#ED9121", bd=3,command='')
        self.but4.place(x=8, y=520, width=70, height=30)
        self.but5=Button(self.nom, text='Contacts', font=ecriture, state=DISABLED, activebackground='orange', bg="#ED9121", bd=3, command='')
        self.but5.place(x=90, y=520, width=70, height=30)
        self.but6=Button(self.nom, text='Utilitaire', font=ecriture, state=DISABLED, activebackground='orange', bg="#ED9121", bd=3, command='')
        self.but6.place(x=172, y=520, width=70, height=30)
        but7=Button(self.nom, text='1', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command=Mere().affiche(1)).place(x=400, y=499, width=15, height=20)
        but8=Button(self.nom, text='2', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=425, y=499, width=15, height=20)
        but9=Button(self.nom, text='3', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=450, y=499, width=15, height=20)
        but10=Button(self.nom, text='4', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=475, y=499, width=15, height=20)
        but11=Button(self.nom, text='5', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=400, y=530, width=15, height=20)
        but12=Button(self.nom, text='6', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=425, y=530, width=15, height=20)
        but13=Button(self.nom, text='7', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=450, y=530, width=15, height=20)
        but14=Button(self.nom, text='8', font=ecriture, activebackground='orange', bg="#E3CF57", bd=3, command='').place(x=475, y=530, width=15, height=20)
        but15=Button(self.nom, text='9', font=ecriture, activebackground='#54FF9F', bg="#E3CF57", bd=3, command='').place(x=400, y=561, width=15, height=20)
        but16=Button(self.nom, text='0', font=ecriture, activebackground='#54FF9F', bg="#E3CF57", bd=3, command='').place(x=425, y=561, width=15, height=20)
        but17 = Button(self.nom, text='*', justify=CENTER, font=ecriture, activebackground='#54FF9F', bg="#54FF9F", bd=3, command='').place(x=450, y=561, width=15, height=20)
        but18 = Button(self.nom, text='#', font=ecriture, activebackground='orange', bg="#54FF9F", bd=3, command=self.eteindre).place(x=475, y=561, width=15, height=20)
        self.ima = Image.open('./img/plac1.png')
        self.tof = ImageTk.PhotoImage(self.ima)
        self.imo = Image.open('./img/raccroche.png')
        self.tofi = ImageTk.PhotoImage(self.imo)
        self.im0 = Image.open('./img/et1.png')
        self.to = ImageTk.PhotoImage(self.im0)
        self.but19 = Button(self.nom, font=ecriture, state=DISABLED, activebackground='orange', bg='orange', image= self.tof, bd=3, command='')
        self.but19.place(x=250, y=488, width=25, height=25)
        self.but20 = Button(self.nom, font=ecriture, state=DISABLED, activebackground='orange', bg='orange', image=self.tofi, bd=3, command=self.termine)
        self.but20.place(x=250, y=523, width=25, height=25)
        self.but21 = Button(self.nom, font=ecriture, activebackground='orange', bg='#FFA500', image=self.to, bd=3, command=self.allumer).place(x=420, y=585, width=25, height=25)
        #self.texto=Text(self.nom, bg='black', fg='green', state=NORMAL, bd=10, font=('Tw Cen MT Condensed Extra Bold', 12))
        #self.texto.bind("<Return>", "")
        #self.texto.bind("<KeyRelease-Return>", "")
        #self.texto.place(x=105, y=570, width=7, height=5) #.place(x=105, y=570, width=386, height=90)
        #####
        #####
        self.nom.config(menu=self.bmenu, background='brown')
        self.nom.resizable(FALSE, FALSE)
        #self.t = Thread(target=self.connexion, args=())
        #self.t.start()
        self.nom.mainloop()
    def eteindre(self):
        self.nom.destroy()
        Graphik('nopli', 'G-Phone', '500x690')
    def web(self):
        y=webbrowser.open('index.html')
        return y
    def allumer(self):
        if self.statut==True:
            time.sleep(1)
            self.nom.destroy()
            Graphik('nopli', 'G-Phone', '500x690')
        else:
            time.sleep(2)
            self.nom.update()
            #self.texta.config(background='white')
            self.texta.config(background='yellow')
            self.texta.config(background='red')
            position = float(self.texta.index('end')) - 1.0
            self.texta.tag_add('Recho', position, position + 0.26)  # 2.9
            self.texta.tag_config('Recho', foreground="#FF8000", font=("arial", 20, "bold"))
            self.texta.insert(END, "Gilda Technologie")
            #time.sleep(2)
            for tag in self.texta.tag_names():
                self.texta.tag_delete(tag)
                self.texta.delete('1.0', END)
            self.texta.config(background='black')
            self.but1.config(state=ACTIVE)
            self.but2.config(state=ACTIVE)
            self.but3.config(state=ACTIVE)
            self.but4.config(state=ACTIVE)
            self.but5.config(state=ACTIVE)
            self.but6.config(state=ACTIVE)
            self.but19.config(state=ACTIVE)
            self.but20.config(state=ACTIVE)
            self.texta.insert(END, str(to))
            self.texta.tag_add('Rech', position, position + 0.26)  # 2.9
            self.texta.tag_config('Rech', foreground="#FF8000", font=("arial", 7, "bold"))
            # self.texta.config(state=DISABLED)
            self.texta.yview(END)
            self.im = Image.open('./img/im.jpg')
            self.photo = ImageTk.PhotoImage(self.im)
            self.list = [True, False]
            self.connexion = self.list[random.randrange(0, 2)]
            if self.connexion == True:
                self.texta.insert(position + 0.99, ' \t\t\t\t\t ⌂ Connecté')
            else:
                position = 1.33
                self.texta.insert(position + 0.99, ' \t\t\t\t               ⌂ Deconnecté')
                self.texta.tag_add('nono', position, position + 0.26)  # 2.9
                self.texta.tag_config('nono', foreground="red", font=("Amperzand", 11, "bold"))
            self.texta.insert(2.0, '\n \n \n \t   ¤ Ligne Securisée ¤')
            self.texta.tag_add('nopli', 4.0, 4.25)  # 2.9
            self.texta.tag_config('nopli', foreground="#DEB887", background="", font=("Virgo 01", 14, "bold"))
            self.degage = self.texta.insert(5.0, '\n \t \t   Addr Ip: '+str(n))  #str(socket.gethostbyname_ex(socket.gethostname())[2][1]) ok
            self.texta.tag_add('ip', 5.0, 5.42)  # 2.9
            self.texta.tag_config('ip', foreground="#607B8B", font=("arial", 11, "bold"))
            self.obeji = self.texta.image_create(6.0, image=self.photo)
            self.texta.config(state=DISABLED)
            self.scroll = Scrollbar(self.nom, command=self.texta.yview, cursor='arrow', bg='green')
            self.texta['yscrollcommand'] = self.scroll.set
            self.scroll.place(x=485, y=5, height=470)
            self.statut=True
            self.texta.delete(TOP, END)
            self.nom.update()

    def appel(self):
        self.num = self.var.get()
        self.mix = mixer
        self.mix.init()
        if self.num in ['', 'n', 'nu', 'num', 'num ', 'num i', 'num in', 'num inv', 'num inva', 'num inval', 'num invali', 'num invalid', 'num invalide']:#== '' or self.num=='num invalide' or self.num=='num' or self.num=='invalide' or self.num=='n' or :
            self.mix.music.load('./sons/numinvalide.mp3')
            self.mix.music.play()
            self.entr.delete(0, END)
            self.entr.insert(END, "num invalide")
        else:
            self.bout1.config(state=ACTIVE)
            self.imu = Image.open('./img/direct.png')
            self.ofefe = ImageTk.PhotoImage(self.imu)
            self.obe = self.texta.image_create(5.0, image=self.ofefe)
            self.texta.insert(5.0, '\n \t \t   Num: ' + str(self.num))  # ok
            self.texta.tag_add('ip', 5.0, 15.42)  # 2.9
            self.texta.tag_config('ip', foreground="#607B8B", font=("arial", 14, "bold"))
            self.m = mixer
            self.m.init()
            self.m.music.load('./sons/connexion.mp3')
            self.m.music.play()
            time.sleep(3)
            self.mix.music.load('./sons/ring1.mp3')
            self.mix.music.play(4)
            self.gard = True
            #self.bout1.config(state=ACTIVE)
            self.bout.config(state=DISABLED)
            #self.texta.deletecommand(self.degage)
            self.texta.delete(2.0, 35.0)
            #self.bout1.config(state=ACTIVE)
            time.sleep(1)
            #from client import Appel
            self.p = Appel()
            self.nom.focus_force()
            self.p.appel('ok')
            #self.nom.loadtk()
            #self.nom.focus()
            self.nom.bell()
            #self.nom.iconwindow()
            self.nom.maxsize(-1, -1)
            self.nom.iconify()

    def voix(self):
        ecriture=('Tw Cen MT Condensed Extra Bold', 12)
        self.var=StringVar()
        self.lab=Label(self.nom, text="Numéro:",bg='#DEB887', font=("Amperzand", 11, "bold"))
        self.lab.place(x=8, y=561)
        self.entr=Entry(self.nom, takefocus=True, width=15, bg="black", fg="white", textvariable=self.var, font=("arial", 11, "bold"))
        self.entr.place(x=80, y=561)
        self.bout = Button(self.nom, font=ecriture, text="Appeler", activebackground='yellow', bg="orange", bd=3, command=self.appel)
        self.bout.place(x=8, y=600, width=90, height=20)
        self.bout1 = Button(self.nom, font=ecriture, text="Terminer", state=DISABLED, activebackground='yellow', bg="orange", bd=3, command=self.termine)
        self.bout1.place(x=115, y=600, width=90, height=20)
        self.bout2 = Button(self.nom, font=ecriture, text="↑", activebackground='yellow', bg="orange", bd=3, command=self.effac)
        self.bout2.place(x=220, y=597, width=20, height=25)
    def texte(self):
        self.ecriture=('Tw Cen MT Condensed Extra Bold', 12)
        self.texto=Text(self.nom, width='31',height='5', bg='black', fg='green', bd=10, state=NORMAL, font=self.ecriture) ##607B8B
        position = float(self.texta.index('end')) - 1.0
        self.texto.tag_add('Rec', "0.0", END)  # 2.9
        self.texto.tag_config('Rec', foreground="#DEB887", font=("arial", 18, "bold"))
        self.texto.insert(END, "Moi:  ")
        self.texto.place(x=5, y=561)
        self.bout2 = Button(self.nom, text="↑", activebackground='yellow', bg="orange", bd=3, command=self.eff)
        self.bout2.place(x=250, y=570, width=20, height=25)
    def eff(self):
        self.texto.place_forget()
        self.bout2.place_forget()

    def effac(self):
        self.lab.place_forget()
        self.entr.place_forget()
        self.bout.place_forget()
        self.bout1.place_forget()
        self.bout2.place_forget()
        if self.gard==True:
            self.mix.music.stop()
            self.texta.deletecommand(self.obe)
            self.texta.deletecommand(self.obeji)
            self.nom.destroy()
            Graphik('nopli', 'G-Phone', '500x690')
            #self.texta.update_idletasks()

    def termine(self):
        self.voix()
        self.bout.config(state=ACTIVE)
        self.mix.music.stop()
        self.mixo = mixer
        #self.p.racroccher()
        self.mixo.init()
        self.mixo.music.load('./sons/ring_busy.mp3')
        self.mixo.music.play()
        time.sleep(3)
        self.mixo.music.stop()
        self.imi = Image.open('./img/raccroche.png')
        self.ofefi = ImageTk.PhotoImage(self.imi)
        self.obu = self.texta.image_create(5.0, image=self.ofefi)
        self.texta.insert(5.0, '\n \t \t   Num: ' + str(self.num))  # ok
        self.texta.tag_add('ip', 5.0, 15.42)  # 2.9
        self.texta.tag_config('ip', foreground="#607B8B", font=("arial", 14, "bold"))
        #self.texta.deletecommand(self.obeji)


Graphik('nopli', 'Gilda-Phone', '500x690')
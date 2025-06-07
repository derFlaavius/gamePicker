import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
import listen
import funktionen
import random
from tkinter import messagebox
import sys


def clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
    for widget in root.winfo_children():
        widget.place_forget()


def hinzufuegen(liste, eingabe):
    if eingabe != "":
        liste.append(eingabe)
        mainpage(liste)
    else:
        messagebox.showwarning("Eingabefehler", "Bitte gebe was in das Feld ein!")


def reset(spielliste):
    spielliste = spielliste.clear()
    spielliste = []
    mainpage(spielliste)


def wuerfeln(liste12): # ChatGPT
    if liste12 == []:
        messagebox.showwarning("Eingabefehler", "Bitte gib zuvor ein paar Namen ein!")
        return
    
    durchlaeufe = 10
    delay = 250  # ms

    # Wenn schon ein Label existiert, updaten wir es
    if not hasattr(root, "lb_info"):
        root.lb_info = tk.Label(root, font=("Arial", 25, "bold"))
        root.lb_info.place(x=300, y=280)

    def loop(i):
        if i > durchlaeufe:
            return
        farbe = funktionen.farbe_waehlen()
        game = random.choice(liste12)

        root.lb_info.config(text=game, fg=farbe)
        root.after(delay, lambda: loop(i + 1))
    loop(0)


def mainpage(spielliste):
    def listbox(liste, xwert, ywert):
        listbox_widget = tk.Listbox(root, height=6, width=24, activestyle='none')
        for item in liste:
            listbox_widget.insert(tk.END, item)
        listbox_widget.place(x=xwert, y=ywert)

    clearwdw()
    pic_logo1.pack()
    widthbtn = 21 # Größe der Elemente

    # Deklaration der Elemente
    # Labels
    lb_spieleingabe = tk.Label(root, text="Spielname:")

    # Entry
    tf_spieleingabe = ttk.Entry(root, width=(widthbtn + 1))
    
    # Buttons
    bn_hinzufuegen = ttk.Button(root, text="Hinzufügen", width=widthbtn, command=lambda:hinzufuegen(spielliste, tf_spieleingabe.get()))
    bn_start = ttk.Button(root, text="Starten", width=widthbtn, command=lambda:wuerfeln(spielliste))
    bn_reset = ttk.Button(root, text="Rücksetzen", width=widthbtn, command=lambda:reset(spielliste))
    bn_abbrechen = ttk.Button(root, text="Beenden", width=widthbtn, command=lambda:sys.exit())

    # Deklaration Abstände und größen
    xwert = 40
    ywert = 130
    abst_buty = 40
    abst_lby = 25

    # Einfügen der Elemente
    listbox(spielliste, 40, 240)
    lb_spieleingabe.place(x=xwert, y=ywert)
    ywert += abst_lby
    tf_spieleingabe.place(x=xwert, y=ywert)
    ywert += abst_buty
    bn_hinzufuegen.place(x=xwert, y=ywert)
    ywert += 200
    bn_start.place(x=xwert, y=ywert)
    ywert += abst_buty
    bn_reset.place(x=xwert, y=ywert)
    ywert += abst_buty
    bn_abbrechen.place(x=xwert, y=ywert)


# Deklaration Pfade
lnk_azure = os.path.join(os.path.dirname(__file__), "themes", "azure", "azure.tcl")
lnk_logo1 = os.path.join(os.path.dirname(__file__), "images", "logo1.png")

# Erzeugung der Listen
spielliste = listen.spiele

# Erzeugung des Fensters
root = tk.Tk()
root.geometry("600x600")
root.title("gamePicker - Falls du nicht mehr weiter weißt")

# Einstellung GUI
root.tk.call("source", lnk_azure)
root.tk.call("set_theme", "dark")

# Implementierung der Grafiken
logo1 = Image.open(lnk_logo1)
logo1 = logo1.resize((160, 130))
logo1 = ImageTk.PhotoImage(logo1)
pic_logo1 = tk.Label(root, image=logo1)

mainpage(spielliste)

root.mainloop()
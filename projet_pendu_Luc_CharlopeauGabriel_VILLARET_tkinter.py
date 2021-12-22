import tkinter as tk
from tkinter import Menu
import random

#création de la fenêtre principale
fen= tk.Tk()

fen.title("Jeu du Pendu")

#Ajout d'un menu déroulant
menu = Menu(fen)

Parametre = Menu(menu, tearoff=0)

menu.add_cascade(label='Options', menu=Parametre)

fen.config(menu=menu)

fen.geometry("1100x800")


canvas1 = tk.Canvas(fen, width = 400, height = 300)
canvas1.pack()

#création du champ pour que l'utilisateur propose des lettres
entree = tk.Entry(fen)
canvas1.create_window(200, 140, window=entree)

#ouverture du fichier dictionnaire.txt en lisant une ligne au hasard afin de le faire deviner
lines = open('dictionnaire.txt').read().splitlines()
mot =random.choice(lines)

#assigne le mot à la liste "liste" puis initialise le nombre de case vide à mot_cache en fonction du nombre de lettres
liste=(mot)

mot_cache = ["_"]*(len(liste))

#initialise le nombre de chances à 6
chance=6

nbr = 0

#définition de fonctions

#dessine le pendu peu à peu en fonction du nombre de chances restant
def dessin(x):
    if x==5:
        canvas1.create_line(40,100,40,10,width=5,fill="black")
    if x==4:
        canvas1.create_line(40,10,70,10,width=5,fill="black")
    if x==3:
        canvas1.create_line(70,10,70,25,width=5,fill="black")
    if x==2:
        canvas1.create_oval(65,25,80,50,fill="black",width=2)
    if x==1:
        canvas1.create_line(73,50,73,75,width=3,fill="black")
    if x==0:
        canvas1.create_line(73,60,83,50,width=3,fill="black")
        canvas1.create_line(73,60,63,50,width=3,fill="black")
        canvas1.create_line(73,75,60 ,85,width=3,fill="black")
        canvas1.create_line(73,75,90,85,width=3,fill="black")
        canvas1.create_text(170,70,text="1 CHANCE !",fill="red",font="arial")
print(mot_cache)

#Fonction principale qui va agir si l'utilisateur a trouver la bonne lettre ou non et modifier certaines variables comme le nombre de chance ou appeler certaines autres fonctions comme dessin()
def soumettre():
    global nbr
    global chance
    canvas1.create_text(275,70,text="CHANCE:",fill="black",font="arial")
    canvas1.create_text(325,70,text=chance,fill="red",font="arial")
    tab = []
    if chance > 0:
        lettredemandee = entree.get()
        if lettre(lettredemandee,liste):
            print("bien joué")
            tab.append(lettredemandee)
            parcourir(liste, lettredemandee)
            nbr = nbr + 1
            entree.delete(0,tk.END)
            print(mot_cache)
            canvas1.create_rectangle(100, 90, 300, 115, fill='grey')
            canvas1.create_text(200,100,text=mot_cache,fill="white",font="arial")
            canvas1.create_text(275,70,text="CHANCE:",fill="black",font="arial")
            canvas1.create_text(325,70,text=chance,fill="red",font="arial")



        else:
            print("raté elle n'y est pas réessaye il te reste " ,chance, "chance")
            chance = chance-1
            dessin(chance)

            entree.delete(0,tk.END)
            print(mot_cache)
            canvas1.create_rectangle(315, 60, 335, 80, fill='grey')
            canvas1.create_text(275,70,text="CHANCE:",fill="black",font="arial")
            canvas1.create_text(325,70,text=chance,fill="red",font="arial")

        if nbr == (len(liste)):
            print("gagné!")
            print(mot_cache)
            fen.destroy()
    else:
        print("perdu!")
        fen.destroy()

#parcours la liste pour chercher la position de la lettre demandée
def parcourir(liste, lettredemandee):
    for i in range(len(liste)):
        if lettredemandee == liste[i]:
            print(mot_cache[i])
            mot_cache[i] = lettredemandee

#parcours la liste pour chercher si la lettre demandée est dans la liste/le mot à trouver
def lettre(lettre1,liste):
    trouver=False
    for lettre in liste:
        if lettre==lettre1:
            trouver=True
    return trouver

#pour les tricheurs
def solution():
    print(liste)
    canvas1.create_text(360,10,text=liste,fill="black",font="arial")

#crée un bouton qui active la fonction soumettre pour proposer la lettre écrite dans le champs de texte au programme
button1 = tk.Button(text='Proposer la lettre ci-dessus', command=soumettre)
canvas1.create_window(200, 180, window=button1)

#ajoute dans le menu déroulant un bouton Solution
Parametre.add_command(label='Solution', command=solution)

#lancement du programme
fen.mainloop()
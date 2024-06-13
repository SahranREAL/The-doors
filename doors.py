import tkinter as tk
from tkinter import messagebox
import random

class TheDoorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("The Doors Game")

        # Couleurs et styles
        self.background_color = "#1E1E1E"
        self.button_color = "#A57C2E"
        self.text_color = "#FFFFFF"
        self.font = ("Helvetica", 12)

        self.score = 0
        self.best_score = 0  # Meilleur score initial
        self.language = "fr"  # Langue par défaut
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        self.menu_bar = tk.Menu(self.master)

        # Menu Options
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.options_menu.add_command(label="Nouvelle partie", command=self.nouvelle_partie)
        self.options_menu.add_command(label="Changer de langue", command=self.changer_langue)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="À propos", command=self.a_propos)
        self.options_menu.add_command(label="Quitter", command=self.master.quit)

        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)

        self.master.config(menu=self.menu_bar)

    def create_widgets(self):
        self.master.configure(background=self.background_color)

        self.instructions_label = tk.Label(self.master, text="Bienvenue dans le jeu 'The Doors'!\n"
                                                              "Il y a trois portes devant vous.\n"
                                                              "Une porte ne fait rien, une autre vous ramène en arrière (-1 point),\n"
                                                              "et la dernière vous fait avancer (+1 point).\n"
                                                              "Choisissez une porte en cliquant sur le bouton correspondant.",
                                          bg=self.background_color, fg=self.text_color, font=self.font)
        self.instructions_label.pack(pady=10)

        self.doors_frame = tk.Frame(self.master, bg=self.background_color)
        self.doors_frame.pack()

        # Personnalisation des boutons pour ressembler à des portes
        self.door1_button = tk.Button(self.doors_frame, text="Porte 1", width=10, command=lambda: self.ouvrir_porte(1),
                                      bg=self.button_color, fg=self.text_color, font=self.font)
        self.door1_button.config(relief=tk.RAISED, bd=5, padx=20, pady=20, font=("Helvetica", 12, "bold"))
        self.door1_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.door2_button = tk.Button(self.doors_frame, text="Porte 2", width=10, command=lambda: self.ouvrir_porte(2),
                                      bg=self.button_color, fg=self.text_color, font=self.font)
        self.door2_button.config(relief=tk.RAISED, bd=5, padx=20, pady=20, font=("Helvetica", 12, "bold"))
        self.door2_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.door3_button = tk.Button(self.doors_frame, text="Porte 3", width=10, command=lambda: self.ouvrir_porte(3),
                                      bg=self.button_color, fg=self.text_color, font=self.font)
        self.door3_button.config(relief=tk.RAISED, bd=5, padx=20, pady=20, font=("Helvetica", 12, "bold"))
        self.door3_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.score_label = tk.Label(self.master, text=f"Score : {self.score}  |  Meilleur : {self.best_score}",
                                    bg=self.background_color, fg=self.text_color, font=("Helvetica", 14, "bold"))
        self.score_label.pack(pady=10)

    def ouvrir_porte(self, porte):
        resultat = self.determiner_resultat()
        
        if resultat == 'rien':
            messagebox.showinfo("Rien", "Cette porte ne fait rien.")
        elif resultat == 'arriere':
            messagebox.showinfo("Arrière", "Cette porte vous ramène en arrière. -1 point.")
            self.score -= 1
        elif resultat == 'avant':
            messagebox.showinfo("Avant", "Cette porte vous fait avancer. +1 point.")
            self.score += 1

        # Mettre à jour le meilleur score si nécessaire
        if self.score > self.best_score:
            self.best_score = self.score

        self.update_score_labels()

    def update_score_labels(self):
        self.score_label.config(text=f"Score : {self.score}  |  Meilleur : {self.best_score}")

    def determiner_resultat(self):
        # Ajuster les chances de tomber sur "+1 point" en modifiant les probabilités
        choix = random.choices(['rien', 'arriere', 'avant'], weights=[40, 30, 40], k=1)[0]
        return choix

    def nouvelle_partie(self):
        self.score = 0
        self.update_score_labels()
        messagebox.showinfo("Nouvelle partie", "Nouvelle partie commencée!")

    def changer_langue(self):
        # Simulation du changement de langue (à adapter selon la logique de votre jeu)
        if self.language == "fr":
            self.language = "en"
        else:
            self.language = "fr"
        messagebox.showinfo("Changer de langue", f"Langue changée en {self.language}")

    def a_propos(self):
        messagebox.showinfo("À propos de 'The Doors Game'",
                            "Développé par FoxPing Studio\nVersion 1.0\n© 2024 FoxPing corporation.\nJeu simple de sélection de portes.")

def main():
    root = tk.Tk()
    game = TheDoorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

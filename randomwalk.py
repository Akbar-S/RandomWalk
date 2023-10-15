# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paramètres de la marche aléatoire
num_steps = 100  # Nombre d'étapes
proba_droite = 0.5  # Probabilité de se déplacer vers la droite
proba_gauche = 1 - proba_droite  # Probabilité de se déplacer vers la gauche

# Fonction pour effectuer la marche aléatoire
def random_walk(num_steps):
    position = 0
    positions = [position]
    
    for _ in range(num_steps):
        step = np.random.choice([-1, 1], p=[proba_gauche, proba_droite])
        position += step
        positions.append(position)
    
    return positions

# Crée l'animation de la marche aléatoire
def animate_walk(num_steps):
    positions = random_walk(num_steps)
    
    fig, ax = plt.subplots()
    line, = ax.plot(positions, lw=2)

    def update(num, positions, line):
        line.set_data(range(num + 1), positions[:num + 1])

    ani = animation.FuncAnimation(fig, update, frames=num_steps, fargs=(positions, line), repeat=False)

    plt.xlabel("Étapes")
    plt.ylabel("Position")
    plt.title("Marche aléatoire à deux pas")

    plt.show()

animate_walk(num_steps)

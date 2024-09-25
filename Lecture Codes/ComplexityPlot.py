#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:06:14 2024

@author: cornelius
"""

"""
Factorial is too big
"""

import numpy as np
import matplotlib.pyplot as plt

# Daten vorbereiten
n = np.linspace(1, 100, 100)
constant = np.ones_like(n)
logarithmic = np.log2(n)
linear = n
n_log_n = n * np.log2(n)
quadratic = n**2
exponential = 2**(n/10)  # Skaliert für bessere Visualisierung

# Plot erstellen
plt.figure(figsize=(10, 6))

# Jede Komplexität auftragen
plt.plot(n, constant, label='O(1)')
plt.plot(n, logarithmic, label='O(log n)')
plt.plot(n, linear, label='O(n)')
plt.plot(n, n_log_n, label='O(n log n)')
plt.plot(n, quadratic, label='O(n^2)')
plt.plot(n, exponential, label='O(2^n)')

# Achsenbeschriftung und Titel
plt.title('Algorithmic Time Complexities')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')

# Begrenzung der y-Achse für bessere Übersichtlichkeit
plt.ylim(0, 1000)

# Legende hinzufügen
plt.legend()

# Plot anzeigen
plt.grid(True)
plt.show()

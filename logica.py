import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Crear un universo de entrada para la velocidad
velocidad = np.arange(0, 101, 1)  # Rango de velocidades de 0 a 100 km/h

# Crear conjuntos difusos para la velocidad (baja, media y alta) con funciones trapezoidales
velocidad_baja = fuzz.trapmf(velocidad, [0, 0, 30, 50])
velocidad_media = fuzz.trapmf(velocidad, [30, 50, 70, 80])
velocidad_alta = fuzz.trapmf(velocidad, [70, 80, 100, 100])

# Visualizar los conjuntos difusos
plt.figure()
plt.plot(velocidad, velocidad_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(velocidad, velocidad_media, 'g', linewidth=1.5, label='Media')
plt.plot(velocidad, velocidad_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Conjuntos Difusos para la Velocidad')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Membresía')
plt.legend()
plt.show()
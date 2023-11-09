import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Universo de entrada para las calificaciones (porcentaje de 0 a 100)
calificacion_matematicas = ctrl.Antecedent(np.arange(0, 101, 1), 'Calificación Matemáticas')
calificacion_ciencias = ctrl.Antecedent(np.arange(0, 101, 1), 'Calificación Ciencias')
calificacion_literatura = ctrl.Antecedent(np.arange(0, 101, 1), 'Calificación Literatura')

# Universo de salida para la calificación general (porcentaje de 0 a 100)
calificacion_general = ctrl.Consequent(np.arange(0, 101, 1), 'Calificación General')

# Definir conjuntos difusos para las calificaciones en cada asignatura
calificacion_matematicas['Baja'] = fuzz.trapmf(calificacion_matematicas.universe, [0, 0, 40, 60])
calificacion_matematicas['Media'] = fuzz.trapmf(calificacion_matematicas.universe, [40, 60, 70, 80])
calificacion_matematicas['Alta'] = fuzz.trapmf(calificacion_matematicas.universe, [70, 80, 100, 100])

calificacion_ciencias['Baja'] = fuzz.trapmf(calificacion_ciencias.universe, [0, 0, 30, 50])
calificacion_ciencias['Media'] = fuzz.trapmf(calificacion_ciencias.universe, [30, 50, 70, 80])
calificacion_ciencias['Alta'] = fuzz.trapmf(calificacion_ciencias.universe, [70, 80, 100, 100])

calificacion_literatura['Baja'] = fuzz.trapmf(calificacion_literatura.universe, [0, 0, 35, 55])
calificacion_literatura['Media'] = fuzz.trapmf(calificacion_literatura.universe, [35, 55, 70, 80])
calificacion_literatura['Alta'] = fuzz.trapmf(calificacion_literatura.universe, [70, 80, 100, 100])

# Definir conjuntos difusos para la calificación general
calificacion_general['Baja'] = fuzz.trapmf(calificacion_general.universe, [0, 0, 40, 60])
calificacion_general['Media'] = fuzz.trapmf(calificacion_general.universe, [40, 60, 70, 80])
calificacion_general['Alta'] = fuzz.trapmf(calificacion_general.universe, [70, 80, 100, 100])


# Reglas difusas
regla1 = ctrl.Rule(calificacion_matematicas['Baja'] | calificacion_ciencias['Baja'] | calificacion_literatura['Baja'], calificacion_general['Baja'])
regla2 = ctrl.Rule(calificacion_matematicas['Media'] & calificacion_ciencias['Media'] & calificacion_literatura['Media'], calificacion_general['Media'])
regla3 = ctrl.Rule(calificacion_matematicas['Alta'] | calificacion_ciencias['Alta'] | calificacion_literatura['Alta'], calificacion_general['Alta'])


# Crear el sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear la simulación del sistema
simulacion = ctrl.ControlSystemSimulation(sistema_ctrl)

# Definir las calificaciones en cada asignatura
simulacion.input['Calificación Matemáticas'] = 75
simulacion.input['Calificación Ciencias'] = 80
simulacion.input['Calificación Literatura'] = 70

# Realizar la simulación
simulacion.compute()

# Obtener la calificación general
calificacion_general_resultado = simulacion.output['Calificación General']

# Imprimir la calificación general
print("Calificación General:", calificacion_general_resultado)

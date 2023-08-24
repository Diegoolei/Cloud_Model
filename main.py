from init import InitialConditions
import pandas as pd


# Función principal
def modelo():
    # Inicializar condiciones iniciales
    initial_conditions = InitialConditions()
    print(initial_conditions.basic_struct.__dict__)
    print(initial_conditions.t_struct.__dict__)
    print(initial_conditions.gwc.__dict__)
    return 0


modelo()

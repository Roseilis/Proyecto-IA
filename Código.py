from pyswip import Prolog

prolog = Prolog()

prolog.consult("progr.pl")



def consultar_aprobacion(nombre, puntos, asistencia):

    consulta = f"progr('{nombre}', {puntos}, {asistencia}."
   result = bool (list(prolog.query(consulta))):

     

    

nombre = input('Por favor, ingresa el nombre del estudiante: ')

puntos = float(input('Ingresa la nota (de 0 a 5): '))

asistencia = float(input('Ingresa el porcentaje de asistencia (de 0 a 100): '))



consultar_aprobacion(nombre, puntos, asistencia)

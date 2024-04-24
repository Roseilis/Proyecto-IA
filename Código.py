from pyswip import Prolog



from pyswip import Prolog, Functor, Variable



prolog = Prolog()

prolog.assertz("progr.pl")



def consultar_aprobacion(nombre, puntos, asistencia):

  

    resultado = Variable()

  

    consulta = f"estudiante_aprobado('{nombre}', {puntos}, {asistencia}, {resultado})."

    respuesta = list(prolog.query(consulta))

    if respuesta:

  

        estado = respuesta[0][resultado]

        print(f"{nombre} está {estado}.")

    else:

        print("No se pudo determinar el estado de aprobación.")



nombre = input('Por favor, ingresa tu nombre: ')

puntos = float(input('Ingresa tus puntos (de 0 a 5): '))

asistencia = float(input('Ingresa tu porcentaje de asistencia (de 0 a 100): '))



consultar_aprobacion(nombre, puntos, asistencia)

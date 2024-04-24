% Reglas de Prolog para determinar si un estudiante está aprobado

estudiante_aprobado(Nombre, Puntos, Asistencia) :-

    Puntos >= 3,

    Asistencia >= 80,

  write(Nombre), write('Felicitaciones esta aprobado.').



estudiante_aprobado(Nombre, Puntos, Asistencia) :-

    Puntos < 3 ; Asistencia < 80,

    write(Nombre), write('esta desaprobado, se sugiere mejorar las calificaciones y asistir al aula.').

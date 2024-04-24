% Reglas de Prolog para determinar si un estudiante está aprobado
estudiante_aprobado(Nombre, Puntos, Asistencia) :-
    Puntos >= 3,
    Asistencia >= 80,
    format('~w está aprobado.~n', [Nombre]).

estudiante_desaprobado(Nombre, Puntos, Asistencia) :-
    Puntos < 3,
    Asistencia < 80,
    format('~w está desaprobado. Se sugiere mejorar la asistencia y obtener más puntos.~n', [Nombre]).

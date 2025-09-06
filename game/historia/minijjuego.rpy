# Lista de personajes
define personajes = ["Sayonji", "Haruka", "Ai", "Ayane"]

# Lista de acciones posibles
define acciones = ["Descansar", "Atender mesas", "Organizar evento", "Evento nocturno", "Manejar las cuentas"]

# ---------- Pantalla de planificación ----------
screen planificacion_dia():
    tag menu
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 800   # ancho máximo del frame
        ymaximum 600   # alto máximo del frame
        has vbox
        spacing 10

        text "Planifica las tareas del día siguiente"

        viewport:
            draggable True
            mousewheel True
            xmaximum 780
            ymaximum 550
            vbox:
                spacing 8

                # Recorremos cada personaje
                for personaje in personajes:
                    text "{0}:".format(personaje)
            
                    # Recorremos cada acción para ese personaje
                    for accion in acciones:
                        textbutton accion action Function(lambda p=personaje, a=accion: planificacion.update({p: a}))

                textbutton "Finalizar planificación":
                    action Jump("resumen_dia")


# ---------- Resumen del día ----------
label resumen_dia:
    scene black with fade
    "Este es el plan para mañana:"
    "Sayonji: [planificacion['Sayonji']]"
    "Haruka: [planificacion['Haruka']]"
    "Ai: [planificacion['Ai']]"
    "Ayane: [planificacion['Ayane']]"
    pause 1.0
    "Ya podemos irnos a dormir"
    menu:
        "Dormir":
            jump capitulo1
        "Salir":
            return

# ---------- Resultado usando la web ----------
label web_resultado:
    scene black with fade
    "¡Resultado del día siguiente!"
    "Sayonji hará: [planificacion['Sayonji']]"
    "Haruka hará: [planificacion['Haruka']]"
    "Ai hará: [planificacion['Ai']]"
    "Ayane hará: [planificacion['Ayane']]"
    "Todo listo para comenzar el día."
    return

label planificacion_juego:
    call screen planificacion_dia
    # cuando termine, salta al resumen del día
    return

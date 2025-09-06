# Lista de personajes
define personajes = ["Rei Sayonji", "Haruka Tachibana", "Ai Mizuno", "Ayane Matsumoto"]

# Lista de acciones posibles
define acciones = ["Descansar", "Atender mesas", "Organizar evento", "Evento nocturno", "Manejar las cuentas"]

define especialidades = {
    "Rei Sayonji": "Manejar las cuentas",
    "Haruka Tachibana": "Atender mesas",
    "Ai Mizuno": "Organizar evento",
    "Ayane Matsumoto": "Evento nocturno"
}

default estamina = {
    "Rei Sayonji": 100,
    "Haruka Tachibana": 100,
    "Ai Mizuno": 100,
    "Ayane Matsumoto": 100
}

default reputacion = 0

default planificacion = {
    "Rei Sayonji": "",
    "Haruka Tachibana": "",
    "Ai Mizuno": "",
    "Ayane Matsumoto": ""
}


screen planificacion_dia():
    tag menu
    frame:
        xalign 0.5
        yalign 0.5
        background "#000A"
        xmaximum 1800
        ymaximum 900
        padding (20, 20)
        has vbox
        spacing 12

        text "Planifica las tareas del día siguiente" size 28 bold True color "#FFA726" xalign 0.5

        viewport:
            draggable True
            mousewheel True
            xmaximum 1500
            ymaximum 800
            xfill True
            vbox:
                spacing 12

                # Recorremos cada personaje
                for personaje in personajes:
                    frame background "#2228" padding (10, 10):
                        vbox:
                            spacing 8
                            text personaje size 22 bold True color "#FFCC80"

                            # Barras de estamina y afinidad
                            hbox spacing 5:
                                text "Estamina: "
                                bar value estamina[personaje] range 100 xmaximum 250 ymaximum 15
 
                            hbox spacing 5:
                                for accion in acciones:
                                    $ is_selected = (planificacion[personaje] == accion)
                                    textbutton accion:
                                        background "#6D4C41" 
                                        hover_background "#8D6E63" 
                                        padding (8, 8)
                                        action Function(lambda p=personaje, a=accion: planificacion.update({p: a}))

                textbutton "Finalizar planificación":
                    xalign 0.5
                    background "#FFA726"
                    hover_background "#FFB74D"
                    padding (12, 12)
                    action Jump("resumen_dia")

# ---------- Resumen del día ----------
label resumen_dia:
    pause 1.0
    "Ya podemos irnos a dormir"
    $ bonus = 0
    python:
        for personaje in personajes:
            if planificacion[personaje] == especialidades[personaje]:
                reputacion += 50
                bonus += 50
                estamina[personaje] -= 25
                afinidad[personaje] += 10
            else:
                reputacion += 10
                afinidad[personaje] += 2
                estamina[personaje] -= 25



    "Reputacion: [reputacion]"
    "Ganaste [bonus] por cumplir las tareas exactas"
    menu:
        "Dormir":
            show screen mostrar_afinidad
        "Salir":
            return

# ---------- Resultado usando la web ----------
label web_resultado:
    scene black with fade
    "Resumen de planificacion:"
    "Rei Sayonji: [planificacion['Rei Sayonji']]"
    "Haruka Tachibana: [planificacion['Haruka Tachibana']]"
    "Ai Mizuno: [planificacion['Ai Mizuno']]"
    "Ayane Matsumoto: [planificacion['Ayane Matsumoto']]"
    "Todo listo para comenzar el día."
    return

screen instrucciones():
    tag menu
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        background "#000A"
        padding (20, 20)
        xmaximum 700
        vbox:
            spacing 12

            text "¡Bienvenido a la creación de eventos!" size 28 bold True color "#FFA726" xalign 0.5

            frame background "#2228" padding (10, 10):
                vbox:
                    spacing 6
                    text "Instrucciones generales:" size 22 bold True color "#FFCC80"
                    text "1️⃣ Planifica las tareas del día siguiente para cada personaje." size 20
                    text "2️⃣ Usa los botones para asignar acciones." size 20
                    text "3️⃣ Cuando termines, pulsa 'Finalizar planificación'." size 20

            frame background "#2228" padding (10, 10):
                vbox:
                    spacing 6
                    text "Advertencias importantes:" size 22 bold True color "#FF5252"
                    text "⚠️ Cada chica puede hacer las tareas de las demás, pero recibirás menos puntos de reputación." size 20
                    text "⚠️ Debes cuidar su estamina. Si llega a 0, descansarán obligatoriamente." size 20

            textbutton "¡Entendido!":
                xalign 0.5
                background "#FFA726"
                hover_background "#FFB74D"
                action Return()
                

label planificacion_juego:
    call screen instrucciones 
    scene restaurante_interior at blur with dissolve
    call screen planificacion_dia
    # cuando termine, salta al resumen del día
    return

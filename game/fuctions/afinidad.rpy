# Lista de personajes
define personajes = ["Rei Sayonji", "Haruka Tachibana", "Ai Mizuno", "Ayane Matsumoto"]

# Diccionario de afinidad
default afinidad = dict.fromkeys(personajes, 0)

screen mostrar_afinidad():
    tag menu
    frame:
        xalign 0.02
        yalign 0.02
        background "#0008"
        padding (10, 10)
        vbox:
            spacing 5 
            text "Afinidades" size 20 bold True
            for nombres, puntos in afinidad.items():
                vbox:
                    spacing 2 
                    text nombres
                    bar:
                        value puntos
                        range 100
                        xmaximum 300
                        ymaximum 20
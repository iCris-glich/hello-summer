define ha = Character("Haruka", who_suffix=" Tachibana")
define re = Character("Rei", who_suffix=" Sayonji")
define ai = Character("Ai", who_suffix=" Mizuno")
define ay = Character("Ayane", who_suffix=" Matsumoto")

define n = Character(None)

define prota = Character("[nombre]", who_suffix=" [apellido]")
define tk = Character("Tio Kyon")

define cha1 = Character("Desconocida")
define cho1 = Character("Desconocido")

#--sprites--
image haruka = im.Scale("images/personajes/haruka/haruka-Photoroom.png", 800, 950)
image haruka_molesta = im.Scale("images/personajes/haruka/haruka_molesta-Photoroom.png", 800, 950)
image haruka_pensando = im.Scale("images/personajes/haruka/haruka_pensandos.png", 800, 950)
image haruka_sorprendida = im.Scale("images/personajes/haruka/haruka_sorprendida.png", 800, 950)
image haruka_avergonzada = im.Scale("images/personajes/haruka/haruka_avergonzada-Photoroom.png", 800, 950)
image haruka_traje_molesta = im.Scale("images/personajes/haruka/haruka_traje_molesta.png", 800, 950)


image rei_traje = im.Scale("images/personajes/rei/rei_traje-Photoroom.png", 800, 950)
image rei_traje_avergonzada = im.Scale("images/personajes/rei/rei_traje_avergonzada.png", 800, 950)
image tio = im.Scale("images/personajes/Gemini_Generated_Image_r9xnxjr9xnxjr9xn-Photoroom.png", 800, 950)

transform mover_a_centro:
    linear 1.0 xalign 0.5 

transform shake:
    xpos 0 ypos 0
    linear 0.05 xpos -10 ypos -10
    linear 0.05 xpos 10 ypos 10
    linear 0.05 xpos -5 ypos 5
    linear 0.05 xpos 0 ypos 0

transform acercarse_centro_suave:
    zoom 1.2                # tamaño inicial
    linear 0.7 xalign 0.5 yalign 0.5 zoom 1.5  # se mueve al centro, se acerca y agranda

transform girar_pequeño:
    rotate 0
    linear 0.1 rotate 5
    linear 0.1 rotate -5
    linear 0.1 rotate 0

transform giro_pequeño:
    xpos 0.10 ypos 0.12  # Ajusta según tu layout
    linear 0.05 xpos 0.68
    linear 0.05 xpos 0.72
    linear 0.05 xpos 0.69
    linear 0.05 xpos 0.71
    linear 0.05 xpos 0.7

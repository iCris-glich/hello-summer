label intro:
    # Inicio y llegada a Kamakura
    pause 0.5
    scene autobus_afuera at blur with fade
    play sound autobus
    "En alguna parte de Kamakura, un autobús llega a la ciudad."
    play music tema_principal fadein 1.0

    prota "Por fin... Kamakura. Hace un calor insoportable…"
    prota "Será mejor que busque el restaurante de mi tío. ¿Dónde quedaba exactamente?{w=0.5}..."

    scene black with fade 
    "Después de un rato caminando por la ciudad…"

    scene playa_atardecer at blur with fade
    play sound mar loop
    prota "¿Eh?... La playa. Entonces ya no debo estar muy lejos."
    prota "(La vista es relajante, pero no tengo tiempo para distraerme.)"
    stop sound fadeout 0.5

    # Llegada al restaurante
    scene restaurante_interior at blur with dissolve
    "Restaurante Kanjuu."
    prota "Creo que este es el lugar. Espero que el tío Kyon esté aquí."
    prota "(Se ve mucho más arreglado que la última vez, parece que ha puesto esfuerzo en esto.)"
    pause 0.3

    prota "*Escucho pasos apresurados acercándose…*"
    pause 0.3
    cha1 "¡¡Hey!!"
    prota "¿¡Eh!?"
    stop music fadeout 0.5

    play music tema_haruka fadein 1.0
    show haruka at right with dissolve
    cha1 "Te he visto dando vueltas por aquí. Tu cara no me suena de nada."
    pause 0.5
    prota "(¿Quién es esta chica? Suena directa…)"
    hide haruka
    show haruka_molesta at right with dissolve
    cha1 "No irás a ser uno de esos tipos raros, ¿verdad?"
    prota "¿Eh?..."
    cha1 "No lo niegas. De esos hay muchos… y tú tienes pinta de ser uno."
    prota "(Será mejor que mantenga la calma.)"
    pause 0.5

    hide haruka_molesta
    show haruka_pensando at right with dissolve
    prota "(Me está analizando como si fuera un criminal.)"
    pause 0.5

    hide haruka_pensando
    show haruka_molesta at acercarse_centro_suave
    cha1 "No pienso dejarte. ¡Te advierto que soy cinturón negro en judo!"
    prota "¡Espera, estás loca!"
    "La tensión aumenta por el malentendido."
    pause 0.5 

    # Intervención del tío
    show restaurante_interior with hpunch
    cho1 "¡Alto ahí!"
    show tio at left with dissolve
    cha1 "Señor Kyon, este tipo intentó entrar y nunca lo habíamos visto."
    prota "(No me quita los ojos de encima...)"
    tk "Ja ja ja... Tranquila Tachibana, él no es peligroso."
    hide haruka_molesta
    show haruka_pensando with dissolve
    ha "¿Lo conoce, señor Kyon?"
    tk "Por supuesto. Es mi sobrino [nombre]."
    pause 0.5
    hide haruka_pensando
    show haruka_avergonzada at center with dissolve
    ha "Perdón, no sabía nada..."
    prota "(Esta chica...)"
    pause 0.5
    tk "Ven conmigo, [nombre]."
    prota "Está bien..."
    hide haruka_avergonzada
    show haruka_molesta with dissolve
    prota "(Sigue sin dejar de mirarme de reojo...)"
    stop music fadeout 1.0
    pause 0.5

    # Conversación sobre el restaurante
    scene black with fade
    pause 0.3
    play music tema_principal fadein 1.0
    show restaurante_interior at blur with fade 
    show tio with dissolve
    tk "¿Cómo has estado [nombre]? Tu padre en Tokio sigue ocupado como siempre."
    prota "Como siempre ocupado"
    tk "Eses cabeza dura siempre con su trabajo"
    pause 1.0
    prota "Tio..."
    tk "Bueno te preguntaras por que te pedi que vinieras"
    pause 0.5
    tk "Necesito pedirte un favor."
    prota "¿A mí? Si es dinero, estoy en la ruina."
    tk "Jajaja que directo pero no"
    tk "Pues veras quiero que te hagas cargo {w=0.5}{cps=6}del restaurante."
    pause 1.5
    prota "{cps=5} . . ."
    show restaurante_interior at shake
    prota "¡¿Qué?! Tío, el sol de la playa te ha vuelto loco."
    tk "No no deja de decir tonterias"
    tk "Veras restaurante ha pasado de generación en generación al primer hijo. "
    tk "Pero como sabes no tengo hijos, y tú eres el pariente más cercano para ser el heredero..."
    pause 0.5
    stop music fadeout 1.0

    pause 2.0
    play music melancolia fadein 1.0
    tk "..."
    tk "Sientes que es muy repentino..."
    tk "Te seré sincero [nombre]... Nunca me casé ni busqué pareja. Siempre estuve enamorado de alguien que se fue de mi vida."
    prota "(La atmósfera cambió de repente.)"
    tk "La solucion más rapida era olvidarla, {w=0.5}pero el corazon es muy delicado"
    tk "A veces cabeza serena de tu padre es algo que envido y hubiera sido util en aquel entonces"
    prota "Tio..."
    prota "Pero tengo 18 y volveré a Tokio al final del verano..."
    prota "No puedo aceptar una peticion tan repentina"
    tk "Si lo se..."
    tk "Puedes dirigir el restaurante estas vacaciones. Evalúa y decide si quieres quedarte."
    prota "(El tio Kyon veo que quiere que me quede)"
    call decision_restaurante

    return


# ---------- Menú de decisión ----------
default intentos=0

label decision_restaurante:
    menu:
        "Aceptar la propuesta":
            prota "Está bien... me quedaré hasta el final del verano."
            prota "Pero después tendrás que buscar a alguien más para el restaurante."
            tk "Sabía que podía confiar en ti."
            jump continuacion
        "Rechazar la propuesta":
            $ intentos += 1
            prota "Lo siento, tío... tengo que pensarlo un poco más."
            if intentos < 3:
                tk "Está bien. No te presionaré."
                jump decision_restaurante
            else:
                tk "Ya veo... pero tarde o temprano tendrás que aceptar... [nombre][apellido]"
                return
    return

# ---------- Continuación ----------
label continuacion:
    tk "Debo sentar cabeza y formar una familia"
    tk "Pero pasando a lo importante, hay que dar la noticia al personal."
    stop music fadeout 1.0
    scene restaurante_exterior_dark at blur with fade
    play music tema_principal fadein 1.0
    show tio with dissolve
    tk "Todos por favor escuchen. El restaurante ha tenido éxito estos últimos años"
    tk "Gracias a ustedes por tan arduo trabajo"
    "Aplausos."
    tk "También quiero presentarles a mi sobrino [nombre] [apellido]."
    pause 0.5
    tk "Se que es repentino pero quiero dejar el restaurante a mano de mi sobrino"
    pause 0.5
    show haruka_sorprendida at giro_pequeño
    ha "¿¡Qué!? Señor Kyon nos dejará..."
    prota "¡Tío!"
    tk "Serán unos días hasta evaluar su desempeño como dueño. Sin más, brindemos por este momento."
    scene black with fade
    prota "(No dejaron de examinarme por completo. Siento que esto es una mala idea...)"

    # Presentación de empleados
    scene restaurante_exterior_dark at blur with fade
    show tio at right with dissolve
    tk "Ven [nombre], quiero presentarte a algunas personas del restaurante."

    # Sayonji
    $ afinidad[personajes[0]] += 10
    show rei_traje at left with dissolve
    tk "Esta chica es Sayonji, la recepcionista. Siempre parece relajada, pero mantiene la cabeza fría en situaciones complicadas."
    re "Un gusto [apellido]."
    prota "Un gusto."
    hide rei_traje
    show rei_traje_avergonzada at left with dissolve
    re "Me halaga, señor Kyon."
    tk "Jajaja, típico de Sayonji, tan modesta."
    hide rei_traje_avergonzada
    show rei_traje at center with dissolve
    prota "(No deja de mirarme de forma esporádica)"
    tk "[nombre]..."
    prota "¡Sí!"
    hide rei_traje
    pause 0.5 

    # Haruka
    $ afinidad[personajes[1]] += 10
    show tio at left with dissolve 
    show haruka_traje_molesta at right with hpunch
    tk "Ya conocías a Tachibana"
    prota "Sí... (Todavía me mira enojada...)"
    ha "Señor Kyon no puede dejarle el lugar a este tipo. Se ve problemático. Pero si usted lo dejara, entonces que más remedio..."
    ha "Soy Haruka Tachibana, la mesera estrella del restaurante."
    prota "Un gusto Tachibana. (Esta chica creo que me dará canas verdes.)"
    hide haruka_traje_molesta

    # Ai
    $ afinidad[personajes[2]] += 10
    show tio at right with dissolve
    show ai at left 
    ai "¡Oh, hola! Encantada, señor [apellido]. Escuché que tienes mala pinta y pareces un delincuente."
    prota "(Primero una loca gruñona y ahora una habladora... Dios, qué pecado estoy pagando.)"
    ai "¿Eh? No me respondes, ¿será que te asusté? "
    ai "Tienes una mirada que mata... JAJAJA."
    ai "Soy Ai Mizuno, encargada de los eventos y posters del restaurante."
    prota "Un gusto. (Bueno, es palanchina... puedo acostumbrarme)"
    hide ai 
    stop music fadeout 1.0

    # Ayane
    $ afinidad[personajes[3]] += 15
    show tio at left with dissolve 
    tk "Y la siguiente es Matsumoto"
    show ayane at right with dissolve
    play music tema_ayane fadein 1.0 
    ay "Un gusto [nombre] [apellido]"
    tk "Matsumoto es la cantante de nuestro show nocturno, un éxito gracias a ella."
    ay "Gracias señor Kyon, pero todo se lo debo a usted. Me ha dejado usar mi voz en el restaurante."
    tk "JA JA JA"
    prota "(Bueno, de todas es la segunda más normal después de Sayonji)"
    ay "Tu [apellido] espero seguir conlaborando contigo en este tiempo que este aquí"
    prota "Ah lo mismo digo"
    ay "*Suelta una leve sonrisa*"
    ay "Paso a retirarme, con permiso"
    hide ayane
    show tio at center with dissolve 
    tk "Vamos rapido que tenemos que conocer al resto"
    prota "Ya voy tio"
    prota "(Bueno este verano sera interesante)"
    "Empieza el verano, sol, playa y 4 lindas chicas"
    hide tio 
    show haruka with dissolve 
    pause 0.5
    hide haruka
    show rei_traje with dissolve 
    pause 0.5
    hide rei_traje
    show ai with dissolve 
    pause 0.5
    hide ai 
    show ayane with dissolve 
    pause 1.0
    hide ayane with dissolve 
    "Que emocion es ser joven"
    scene black with fade 

    jump planificacion_juego
    
    return
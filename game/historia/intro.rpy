label intro:
    pause 0.5
    scene autobus_afuera at blur with fade

    play sound autobus
    "En alguna parte de Kamakura, un autobús llega a la ciudad."
    play music tema_principal

    prota "..."
    prota "Por fin... Kamakura."
    prota "Hace un calor insoportable…"
    prota "Será mejor que busque el restaurante de mi tío."
    prota "¿Dónde quedaba exactamente?{w=0.5}..."

    scene black with fade 
    "Después de un rato caminando por la ciudad…"

    scene playa_atardecer at blur with fade
    play sound mar
    prota "¿Eh?... La playa."
    prota "Entonces ya no debo estar muy lejos."
    pause 0.5
    prota "(La vista es relajante... pero no tengo tiempo para distraerme.)"
    stop sound

    scene restaurante_interior at blur with dissolve
    "Restaurante Kanjuu."
    prota "Creo que este es el lugar."
    prota "Espero que el tío Kyon esté aquí."
    prota "Se ve mucho más arreglado que la última vez."
    prota "(Vaya, parece que ha puesto bastante esfuerzo en esto.)"
    pause 0.3

    prota "*Escucho pasos apresurados acercándose…*"
    pause 0.3
    cha1 "¡¡Hey!!"
    prota "¿¡Eh!?"
    stop music
    pause 0.3

    play music tema_haruka
    show haruka at right with dissolve
    cha1 "Te he visto dando vueltas por aquí."
    cha1 "Y tu cara no me suena de nada."
    pause 0.5
    prota "(¿Quién es esta chica? Suena bastante directa…)"
    hide haruka
    show haruka_molesta at right with dissolve
    cha1 "No irás a ser uno de esos tipos raros, ¿verdad?"
    prota "¿Eh?..."
    cha1 "No lo niegas."
    cha1 "De esos hay muchos… y tú tienes pinta de ser uno."
    prota "(Vaya carácter... será mejor que mantenga la calma.)"
    pause 0.5

    hide haruka_molesta
    show haruka_pensando at right with dissolve
    prota "(Me está analizando como si fuera un criminal.)"
    pause 0.5

    hide haruka_pensando
    show haruka_molesta at right with dissolve
    prota "(Su exprecion otra vez es de molestia)"
    cha1 "Será mejor que ni intentes entrar."      
    show haruka_molesta at acercarse_centro_suave
    cha1 "No pienso dejarte."
    prota "¿No crees que exageras un poco?"
    show haruka_molesta at girar_pequeño
    cha1 "¡Te advierto que soy cinturón negro en judo!"
    prota "¡Espera estas loca!"
    "La tensión aumenta por el malentendido."
    pause 0.5 

    show restaurante_interior at shake
    cho1 "¡Alto ahí!"
    show tio at left with dissolve
    prota "¿Ahora qué pasa?"
    cha1 "Señor Kyon..."
    pause 0.5
    cha1 "Este tipo intentó entrar y nunca lo habíamos visto antes."
    cha1 "Podría ser un pervertido... o alguien de la competencia."
    prota "(No me quita los ojos de encima...)"
    tk "Ja ja ja..."
    tk "Tranquila Tachibana, él no es peligroso."
    hide haruka_molesta
    show haruka_pensando with dissolve
    ha "¿Lo conoce, señor Kyon?"
    tk "Por supuesto. Es mi sobrino [nombre]."
    pause 0.5
    hide haruka_pensando
    show haruka_sorprendida at right
    ha "¡¿Su sobrino?!"
    ha "¿En serio? Tiene cara de problemático."
    prota "¡Te estoy oyendo!"
    tk "Ja ja ja, Tachibana deja de ser tan prejuiciosa."
    hide haruka_sorprendida
    show haruka_avergonzada at center with dissolve
    ha "Perdon no sabia nada..."
    prota "(Esta chica...)"
    prota "Tío Kyon..."
    pause 0.5
    tk "Ven conmigo, [nombre]."
    prota "Está bien..."
    hide haruka_avergonzada
    show haruka_molesta with dissolve
    prota "(Sigue sin dejar de mirarme de reojo...)"
    stop music fadeout 1.0
    pause 0.5

    scene black with fade
    pause 0.3
    play music tema_principal fadein 1.0
    show restaurante_interior at blur with fade 
    show tio with dissolve
    tk "¿Como has estado [nombre]?"
    tk "Tu padre en Tokio ¿Aún no se vuelve loco con tanto trabajo?"
    prota "Sigue igual de ocupado como siempre."
    tk "Me lo imaginaba."
    tk "Ese cabeza fria solo piensa en el trabajo."
    tk "JAJAJA"
    prota "¿Pero tío, por qué me pediste que viniera?"
    pause 1.5
    tk "Pues verás... necesito pedirte un favor."
    prota "¿A mí? ¿Qué clase de favor?"
    prota "Si es dinero, estoy en la ruina."
    tk "Jajaja, tan directo como siempre."
    pause 0.5
    tk "No, nada de dinero... Ire al grano"
    tk "{w=1.5}Quiero que te hagas cargo del restaurante."
    pause 1.5
    prota "{cps=5} . . ."
    show restaurante_interior at shake
    prota "¡¿Quee?!"
    prota "Tio el sol de la playa te ha vuelto loco."
    prota "¿Esto es una clase de broma verdad?"
    pause 0.3
    tk "Mira [nombre]... Quiero que hagas esto."
    tk "El restaurante a pasado de generacion en generacion."
    tk "Pero yo no he podido tener hijos para dejar el lugar en manos de un heredero."
    tk "Y tu al ser el pariente mas cercano a un heredero pues..."
    pause 0.5
    prota "Tio..."
    pause 0.5
    stop music fadeout 1.0 

    pause 2.0
    play music melancolia fadein 1.0
    tk "..."
    tk "{w=0.5}Te sere sincero [nombre]-"
    tk "Nunca me casé ni busqué pareja..."  
    tk "{w=0.5}Porque siempre estuve enamorado de alguien."  
    tk "{w=1.0}Alguien que se fue de mi vida." 
    prota "(La admosfera cambio de repente.)"  
    tk "Y he pensado que ya es momento de centrar cabeza y olvidarme de ella y buscar a alguien más."
    tk "Ver nuevos caminos, el trabajo ya no es como antes."
    tk "Por que mira... {w=1.0}Sin hijos para heredar este restaurante..."
    tk "A veces quisiera tener esa cabeza fria de tu padre."
    tk "{cps=5}Me habria ayudado..."
    prota "(Es la primera vez que veo al Tio así)"
    pause 0.5
    tk "No tomes esta peticion mia como una orden."
    tk "Tomala como un regalo."
    tk "Si aceptas no te preocupes no te dejare solo, el equipo del restaurante te ayudara tambien."
    prota ". . ."
    prota "Pero Tio entiendes que tengo 18 y volvere a Tokyo al final del verano..."
    prota "Tengo que estudiar para los examenes finales."
    prota "Es muy dificil para mi quedarme."
    tk "..."
    pause 0.5
    tk "¿Y si te propongo algo?"
    prota "¿Algo?..."
    tk "Puedes dirigir el restaurante estas vacaciones."
    tk "Acomodate y al final veraz si quieres quedarte."
    tk "No tengo a nadie más a quien dejarlo, entonces buscare un sucesor."
    tk "Tu decision la respetare."
    call decision_restaurante

    return

default intentos=0

label decision_restaurante:
    menu:
        "Aceptar la propuesta":
            prota "Está bien... me quedaré hasta el final del verano."
            prota "Pero después tendrás que buscar a alguien más para el restaurante."
            tk "Sabia que podia confiar en ti."
            jump continuacion
        "Rechazar la propuesta":
            $ intentos += 1
            prota "Lo siento, tío... tengo que pensarlo un poco más."
            if intentos < 3:
                tk "Está bien. No te presionaré."
                jump decision_restaurante
            else:
                tk "Ya veo... pero tarde o temprano tendras que aceptar... [nombre][apellido]"
                return
    return

label continuacion:
    tk "Hay que hacer conocer a los demas de la noticia."
    "Te haz convertido en dueño de un restaurante, que emocion... ¿Verdad?"
    stop music fadeout 1.0
    scene black with fade
    play music tema_principal 
    prota "(El tio reunio a todo el personal afuera del restaurante.)"
    scene restaurante_exterior at blur with fade
    show tio with dissolve 
    tk "Todos por favor escuchen quiero darles una noticia."
    pause 0.5
    "Todos estan espectativos de lo que dira el tio"
    tk "Como saben el restaurante le ha ido muy bien estos ultimos años."
    tk "Queria felicitarlos por tan arduo trabajo y compromiso para que le lugar funcione."
    tk "Muchas gracias."
    "Todos aplauden."
    pause 1.0
    tk "Tambien quiero prensentarles a mi sobrino [nombre][apellido]."
    tk "{w=1.0}Quiero que sepan que sigo agradecido con todos ustedes por su trabajo pero..."
    tk "{w=1.0}Necesito un descanso del trabajo y expandir mis horizontes."
    tk "Por lo que le dejare el mando del restaurante a mi sobrino."
    pause 1.0
    "{cps=5}. . ."

    show haruka_sorprendida at giro_pequeño
    ha "¿¡Quee!?"
    ha "Señor Kyon nos dejara..."
    prota "¡Tio!"
    tk "Bueno seran unos dias hasta evaluar su desempeño como dueño."
    "Se escuchan murmullos."
    prota "(Lo sabia esto era una mala idea... Todos estan hablando de mi)"
    prota "(No creo que esa chica Tachibana confíe en mí después de esto...)"  
    prota "(Aunque, pensándolo bien, ni siquiera antes confiaba demasiado...)"  
    prota "(Que dolor de cabeza)"
    tk "Sin más entonces brindemos por este momento."
    scene black with fade
    scene restaurante_exterior at blur with fade
    prota "(No pude relajarme en todo el rato.)"
    prota "(Parece que todos me ven examinandome)"
    show tio with dissolve 
    tk "Deberia presentarte a algunas empleados del lugar."
    show tio at right with dissolve 
    show rei_traje at left with dissolve 
    tk "Esta chica es Sayonji."
    tk "La recepcionista."
    re "Un gusto [apellido]."
    prota "Un gusto"
    tk "Siempre parece relajada, pero cuando las cosas se complican mantiene la cabeza fría."
    hide rei_traje
    show rei_traje_avergonzada at left with dissolve 
    re "Me alaga señor Kyon."
    tk "Jajaja tipico de Sayonji tan modesta."
    prota "(Esta chica da un aire a esas chica de mangas...)"
    prota "(Relajada, pero es bastante linda)"
    tk "Sigamos"
    hide rei_traje_avergonzada
    hide tio
    show rei_traje at center with dissolve
    prota "(No deja de verme de forma esporadica)"
    tk "[nombre]"
    prota "¡Si!"
    hide rei_traje
    pause 0.5 
    show haruka_traje_molesta at right with dissolve
    show tio at left with dissolve 
    tk "Tu ya habias conocido a Tachibana"
    prota "Si..."
    prota "(Todavia tiene una vista muy enojada conmigo)"
    ha "Señor Kyon no puede dejarle el lugar a este tipo"
    ha "Se ve que es alguien problematico"


    return
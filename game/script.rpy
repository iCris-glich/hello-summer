label start:

    # Pedir nombre
    $ nombre = renpy.input("¿Cuál es tu nombre?")
    $ nombre = nombre.strip()  # elimina espacios al inicio/final
    if nombre == "":
        $ nombre = "Tatsuo"  # nombre por defecto

    #   Pedir apellido (opcional)
    $ apellido = renpy.input("¿Cuál es tu apellido?")
    $ apellido = apellido.strip()
    if apellido == "":
        $ apellido = "Kiryu"

    jump intro
   


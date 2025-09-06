image playa_atardecer = "images/fondos/playa-atardecer.jpg"
image autobus_afuera = "images/fondos/estacion_bus.jpg"
image restaurante_interior = "images/fondos/restaurante_interior.jpg"
image restaurante_exterior = "images/fondos/restaurante_exterior.jpg"
image restaurante_exterior_dark = im.MatrixColor(
    "images/fondos/restaurante_exterior.jpg",
    im.matrix.brightness(-0.2)   # aquí sí es válido
)

transform blur:
    xysize (1920, 1080)
    blur 10


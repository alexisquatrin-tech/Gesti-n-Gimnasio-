"""Registro y gestión de socios del gimnasio."""

import validaciones

# Tipos de membresía disponibles. La membresía Básica solo permite
# usar la sala de musculación; las demás incluyen las actividades.
MEMBRESIAS = {
    1: {"nombre": "Básica", "precio": 20000, "permite_actividades": False},
    2: {"nombre": "Completa", "precio": 32000, "permite_actividades": True},
    3: {"nombre": "Estudiante", "precio": 15000, "permite_actividades": True},
}


def buscar_socio(socios, dni):
    """Devuelve el socio con ese DNI, o None si no existe."""
    for socio in socios:
        if socio["dni"] == dni:
            return socio
    return None


def mostrar_membresias():
    """Muestra los tipos de membresía con su precio y alcance."""
    print("\nTipos de membresía:")
    for codigo, datos in MEMBRESIAS.items():
        if datos["permite_actividades"]:
            detalle = "incluye actividades"
        else:
            detalle = "solo musculación"
        print(f"  {codigo}. {datos['nombre']} - ${datos['precio']} por mes ({detalle})")


def registrar_socio(socios):
    """Da de alta un socio nuevo, validando que el DNI no esté repetido."""
    print("\n--- Registro de socio ---")
    dni = validaciones.leer_dni("DNI del socio: ")
    if buscar_socio(socios, dni) is not None:
        print("Error: ya existe un socio registrado con ese DNI.")
        return
    nombre = validaciones.leer_texto("Nombre y apellido: ")
    edad = validaciones.leer_entero("Edad: ", 12, 100)
    mostrar_membresias()
    codigo = validaciones.leer_entero("Tipo de membresía (1-3): ", 1, 3)
    socio = {
        "dni": dni,
        "nombre": nombre,
        "edad": edad,
        "membresia": codigo,
    }
    socios.append(socio)
    nombre_membresia = MEMBRESIAS[codigo]["nombre"]
    print(f"Socio {nombre} registrado correctamente con membresía {nombre_membresia}.")


def cambiar_membresia(socios, actividades):
    """Permite que un socio cambie su tipo de membresía."""
    print("\n--- Cambio de membresía ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    actual = MEMBRESIAS[socio["membresia"]]["nombre"]
    print(f"Membresía actual de {socio['nombre']}: {actual}")
    mostrar_membresias()
    codigo = validaciones.leer_entero("Nueva membresía (1-3): ", 1, 3)
    if codigo == socio["membresia"]:
        print("El socio ya tiene esa membresía. No se realizaron cambios.")
        return
    socio["membresia"] = codigo
    print(f"Membresía actualizada a {MEMBRESIAS[codigo]['nombre']}.")
    # Si la nueva membresía no incluye actividades, se dan de baja las
    # inscripciones del socio para que los datos queden consistentes.
    if not MEMBRESIAS[codigo]["permite_actividades"]:
        for actividad in actividades:
            if dni in actividad["inscriptos"]:
                actividad["inscriptos"].remove(dni)
                print(f"Aviso: se dio de baja la inscripción a {actividad['nombre']} "
                      "porque la nueva membresía no incluye actividades.")


def listar_socios(socios):
    """Muestra todos los socios registrados."""
    print("\n--- Listado de socios ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    for socio in socios:
        membresia = MEMBRESIAS[socio["membresia"]]["nombre"]
        print(f"DNI {socio['dni']} | {socio['nombre']} | {socio['edad']} años | Membresía {membresia}")
    print(f"Total de socios: {len(socios)}")


def menu_socios(socios, actividades):
    """Submenú de gestión de socios."""
    opcion = -1
    while opcion != 0:
        print("\n===== SOCIOS =====")
        print("1. Registrar socio")
        print("2. Listar socios")
        print("3. Cambiar membresía")
        print("0. Volver al menú principal")
        opcion = validaciones.leer_entero("Opción: ", 0, 3)
        if opcion == 1:
            registrar_socio(socios)
        elif opcion == 2:
            listar_socios(socios)
        elif opcion == 3:
            cambiar_membresia(socios, actividades)

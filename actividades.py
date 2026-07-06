"""Actividades del gimnasio e inscripción de socios."""

import validaciones
import socios as mod_socios


def crear_actividades_iniciales():
    """Devuelve la lista de actividades con las que arranca el sistema."""
    return [
        {"id": 1, "nombre": "Funcional", "dias": "Lunes y Miércoles",
         "horario": "18:00", "cupo": 20, "inscriptos": []},
        {"id": 2, "nombre": "Spinning", "dias": "Martes y Jueves",
         "horario": "19:00", "cupo": 15, "inscriptos": []},
        {"id": 3, "nombre": "Yoga", "dias": "Viernes",
         "horario": "10:00", "cupo": 12, "inscriptos": []},
    ]


def buscar_actividad(actividades, id_actividad):
    """Devuelve la actividad con ese número, o None si no existe."""
    for actividad in actividades:
        if actividad["id"] == id_actividad:
            return actividad
    return None


def listar_actividades(actividades):
    """Muestra las actividades con su cupo y lugares libres."""
    print("\n--- Actividades ---")
    if len(actividades) == 0:
        print("No hay actividades cargadas.")
        return
    for actividad in actividades:
        libres = actividad["cupo"] - len(actividad["inscriptos"])
        print(f"{actividad['id']}. {actividad['nombre']} ({actividad['dias']} {actividad['horario']}) "
              f"| Cupo: {actividad['cupo']} | Lugares libres: {libres}")


def agregar_actividad(actividades):
    """Da de alta una actividad nueva."""
    print("\n--- Nueva actividad ---")
    nombre = validaciones.leer_texto("Nombre de la actividad: ")
    dias = validaciones.leer_texto("Días (por ejemplo 'Lunes y Miércoles'): ")
    horario = validaciones.leer_texto("Horario (por ejemplo 18:00): ")
    cupo = validaciones.leer_entero("Cupo máximo: ", 1, 100)
    nuevo_id = 1
    if len(actividades) > 0:
        nuevo_id = actividades[-1]["id"] + 1
    actividades.append({"id": nuevo_id, "nombre": nombre, "dias": dias,
                        "horario": horario, "cupo": cupo, "inscriptos": []})
    print(f"Actividad '{nombre}' agregada con el número {nuevo_id}.")


def inscribir_socio(socios, actividades):
    """Inscribe un socio en una actividad controlando membresía y cupo."""
    print("\n--- Inscripción a actividad ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = mod_socios.buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    membresia = mod_socios.MEMBRESIAS[socio["membresia"]]
    if not membresia["permite_actividades"]:
        print(f"Error: la membresía {membresia['nombre']} no incluye actividades. "
              "El socio debe cambiarse a Completa o Estudiante.")
        return
    listar_actividades(actividades)
    id_actividad = validaciones.leer_entero("Número de actividad: ", 1)
    actividad = buscar_actividad(actividades, id_actividad)
    if actividad is None:
        print("Error: no existe una actividad con ese número.")
        return
    if dni in actividad["inscriptos"]:
        print(f"Error: el socio ya está inscripto en {actividad['nombre']}.")
        return
    if len(actividad["inscriptos"]) >= actividad["cupo"]:
        print(f"Error: {actividad['nombre']} no tiene lugares libres.")
        return
    actividad["inscriptos"].append(dni)
    print(f"{socio['nombre']} quedó inscripto en {actividad['nombre']}.")


def baja_inscripcion(socios, actividades):
    """Da de baja la inscripción de un socio en una actividad."""
    print("\n--- Baja de inscripción ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = mod_socios.buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    listar_actividades(actividades)
    id_actividad = validaciones.leer_entero("Número de actividad: ", 1)
    actividad = buscar_actividad(actividades, id_actividad)
    if actividad is None:
        print("Error: no existe una actividad con ese número.")
        return
    if dni not in actividad["inscriptos"]:
        print(f"Error: el socio no está inscripto en {actividad['nombre']}.")
        return
    actividad["inscriptos"].remove(dni)
    print(f"Se dio de baja a {socio['nombre']} de {actividad['nombre']}.")


def ver_inscriptos(socios, actividades):
    """Muestra los socios inscriptos en una actividad."""
    print("\n--- Inscriptos por actividad ---")
    listar_actividades(actividades)
    if len(actividades) == 0:
        return
    id_actividad = validaciones.leer_entero("Número de actividad: ", 1)
    actividad = buscar_actividad(actividades, id_actividad)
    if actividad is None:
        print("Error: no existe una actividad con ese número.")
        return
    if len(actividad["inscriptos"]) == 0:
        print(f"{actividad['nombre']} no tiene inscriptos todavía.")
        return
    print(f"Inscriptos en {actividad['nombre']}:")
    for dni in actividad["inscriptos"]:
        socio = mod_socios.buscar_socio(socios, dni)
        print(f"- DNI {dni} | {socio['nombre']}")
    print(f"Total: {len(actividad['inscriptos'])} de {actividad['cupo']} lugares.")


def menu_actividades(socios, actividades):
    """Submenú de actividades e inscripciones."""
    opcion = -1
    while opcion != 0:
        print("\n===== ACTIVIDADES =====")
        print("1. Listar actividades")
        print("2. Inscribir socio a una actividad")
        print("3. Dar de baja una inscripción")
        print("4. Ver inscriptos de una actividad")
        print("5. Agregar actividad nueva")
        print("0. Volver al menú principal")
        opcion = validaciones.leer_entero("Opción: ", 0, 5)
        if opcion == 1:
            listar_actividades(actividades)
        elif opcion == 2:
            inscribir_socio(socios, actividades)
        elif opcion == 3:
            baja_inscripcion(socios, actividades)
        elif opcion == 4:
            ver_inscriptos(socios, actividades)
        elif opcion == 5:
            agregar_actividad(actividades)

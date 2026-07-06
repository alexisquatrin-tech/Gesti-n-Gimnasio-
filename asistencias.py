"""Control de asistencia de los socios al gimnasio y a las actividades."""

import validaciones
import socios as mod_socios
import actividades as mod_actividades

# El identificador 0 representa la sala de musculación (no requiere inscripción).
ID_MUSCULACION = 0
NOMBRE_MUSCULACION = "Musculación (sala general)"


def nombre_del_lugar(actividades, id_actividad):
    """Devuelve el nombre del lugar al que corresponde una asistencia."""
    if id_actividad == ID_MUSCULACION:
        return NOMBRE_MUSCULACION
    actividad = mod_actividades.buscar_actividad(actividades, id_actividad)
    if actividad is None:
        return "Actividad desconocida"
    return actividad["nombre"]


def registrar_asistencia(socios, actividades, asistencias):
    """Registra la asistencia de un socio en una fecha determinada."""
    print("\n--- Registro de asistencia ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = mod_socios.buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    print("¿A qué concurre el socio?")
    print(f"{ID_MUSCULACION}. {NOMBRE_MUSCULACION}")
    mod_actividades.listar_actividades(actividades)
    id_actividad = validaciones.leer_entero("Opción: ", 0)
    if id_actividad != ID_MUSCULACION:
        actividad = mod_actividades.buscar_actividad(actividades, id_actividad)
        if actividad is None:
            print("Error: no existe una actividad con ese número.")
            return
        if dni not in actividad["inscriptos"]:
            print(f"Error: el socio no está inscripto en {actividad['nombre']}.")
            return
    fecha = validaciones.leer_fecha("Fecha de asistencia (dd/mm/aaaa): ")
    for asistencia in asistencias:
        if (asistencia["dni"] == dni
                and asistencia["id_actividad"] == id_actividad
                and asistencia["fecha"] == fecha):
            print("Error: esa asistencia ya estaba registrada.")
            return
    asistencias.append({"dni": dni, "id_actividad": id_actividad, "fecha": fecha})
    lugar = nombre_del_lugar(actividades, id_actividad)
    print(f"Asistencia de {socio['nombre']} a {lugar} registrada para el {fecha}.")


def asistencias_por_fecha(socios, actividades, asistencias):
    """Muestra todas las asistencias registradas en una fecha."""
    print("\n--- Asistencias por fecha ---")
    if len(asistencias) == 0:
        print("Todavía no hay asistencias registradas.")
        return
    fecha = validaciones.leer_fecha("Fecha a consultar (dd/mm/aaaa): ")
    contador = 0
    for asistencia in asistencias:
        if asistencia["fecha"] == fecha:
            socio = mod_socios.buscar_socio(socios, asistencia["dni"])
            lugar = nombre_del_lugar(actividades, asistencia["id_actividad"])
            print(f"- {socio['nombre']} (DNI {socio['dni']}) en {lugar}")
            contador += 1
    if contador == 0:
        print("No hubo asistencias en esa fecha.")
    else:
        print(f"Total de asistencias del {fecha}: {contador}")


def historial_de_socio(socios, actividades, asistencias):
    """Muestra el historial de asistencias de un socio."""
    print("\n--- Historial de un socio ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = mod_socios.buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    contador = 0
    for asistencia in asistencias:
        if asistencia["dni"] == dni:
            lugar = nombre_del_lugar(actividades, asistencia["id_actividad"])
            print(f"- {asistencia['fecha']}: {lugar}")
            contador += 1
    if contador == 0:
        print(f"{socio['nombre']} todavía no registra asistencias.")
    else:
        print(f"Total de asistencias de {socio['nombre']}: {contador}")


def menu_asistencias(socios, actividades, asistencias):
    """Submenú de control de asistencia."""
    opcion = -1
    while opcion != 0:
        print("\n===== ASISTENCIAS =====")
        print("1. Registrar asistencia")
        print("2. Consultar asistencias por fecha")
        print("3. Historial de asistencias de un socio")
        print("0. Volver al menú principal")
        opcion = validaciones.leer_entero("Opción: ", 0, 3)
        if opcion == 1:
            registrar_asistencia(socios, actividades, asistencias)
        elif opcion == 2:
            asistencias_por_fecha(socios, actividades, asistencias)
        elif opcion == 3:
            historial_de_socio(socios, actividades, asistencias)

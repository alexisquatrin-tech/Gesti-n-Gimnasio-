"""Estadísticas básicas de concurrencia y recaudación del gimnasio."""

import validaciones
import socios as mod_socios
import asistencias as mod_asistencias


def contar_asistencias_de(asistencias, id_actividad):
    """Cuenta las asistencias registradas para una actividad (contador)."""
    contador = 0
    for asistencia in asistencias:
        if asistencia["id_actividad"] == id_actividad:
            contador += 1
    return contador


def concurrencia_por_actividad(actividades, asistencias):
    """Muestra la cantidad de asistencias por actividad y la más concurrida."""
    print("\n--- Concurrencia por actividad ---")
    if len(asistencias) == 0:
        print("Todavía no hay asistencias registradas.")
        return
    contador_musculacion = contar_asistencias_de(asistencias, mod_asistencias.ID_MUSCULACION)
    print(f"{mod_asistencias.NOMBRE_MUSCULACION}: {contador_musculacion} asistencias")
    mas_concurrida = mod_asistencias.NOMBRE_MUSCULACION
    maximo = contador_musculacion
    for actividad in actividades:
        contador = contar_asistencias_de(asistencias, actividad["id"])
        print(f"{actividad['nombre']}: {contador} asistencias")
        if contador > maximo:
            maximo = contador
            mas_concurrida = actividad["nombre"]
    print(f"\nLa más concurrida es {mas_concurrida} con {maximo} asistencias.")
    print(f"Total general de asistencias: {len(asistencias)}")


def promedio_de_asistencias(socios, asistencias):
    """Calcula el promedio de asistencias por socio y el socio más constante."""
    print("\n--- Promedio de asistencias ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    promedio = len(asistencias) / len(socios)
    print(f"Asistencias registradas: {len(asistencias)}")
    print(f"Socios registrados: {len(socios)}")
    print(f"Promedio de asistencias por socio: {promedio:.2f}")

    socio_constante = None
    maximo = 0
    for socio in socios:
        contador = 0
        for asistencia in asistencias:
            if asistencia["dni"] == socio["dni"]:
                contador += 1
        if contador > maximo:
            maximo = contador
            socio_constante = socio
    if socio_constante is not None:
        print(f"Socio más constante: {socio_constante['nombre']} ({maximo} asistencias)")


def ocupacion_de_cupos(actividades):
    """Muestra el porcentaje de ocupación del cupo de cada actividad."""
    print("\n--- Ocupación de cupos ---")
    if len(actividades) == 0:
        print("No hay actividades cargadas.")
        return
    suma_porcentajes = 0
    for actividad in actividades:
        porcentaje = len(actividad["inscriptos"]) / actividad["cupo"] * 100
        suma_porcentajes += porcentaje
        print(f"{actividad['nombre']}: {len(actividad['inscriptos'])}/{actividad['cupo']} "
              f"inscriptos ({porcentaje:.1f}% de ocupación)")
    promedio = suma_porcentajes / len(actividades)
    print(f"Ocupación promedio del gimnasio: {promedio:.1f}%")


def socios_por_membresia(socios):
    """Cuenta cuántos socios hay de cada tipo de membresía."""
    print("\n--- Socios por tipo de membresía ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    for codigo, datos in mod_socios.MEMBRESIAS.items():
        contador = 0
        for socio in socios:
            if socio["membresia"] == codigo:
                contador += 1
        porcentaje = contador / len(socios) * 100
        print(f"{datos['nombre']}: {contador} socios ({porcentaje:.1f}%)")


def recaudacion_total(pagos):
    """Suma todos los pagos registrados (acumulador)."""
    print("\n--- Recaudación ---")
    if len(pagos) == 0:
        print("Todavía no hay pagos registrados.")
        return
    total = 0
    for pago in pagos:
        total += pago["monto"]
    print(f"Cuotas cobradas: {len(pagos)}")
    print(f"Recaudación total: ${total:.2f}")


def menu_estadisticas(socios, actividades, pagos, asistencias):
    """Submenú de estadísticas."""
    opcion = -1
    while opcion != 0:
        print("\n===== ESTADÍSTICAS =====")
        print("1. Concurrencia por actividad")
        print("2. Promedio de asistencias y socio más constante")
        print("3. Ocupación de cupos")
        print("4. Socios por tipo de membresía")
        print("5. Recaudación total")
        print("0. Volver al menú principal")
        opcion = validaciones.leer_entero("Opción: ", 0, 5)
        if opcion == 1:
            concurrencia_por_actividad(actividades, asistencias)
        elif opcion == 2:
            promedio_de_asistencias(socios, asistencias)
        elif opcion == 3:
            ocupacion_de_cupos(actividades)
        elif opcion == 4:
            socios_por_membresia(socios)
        elif opcion == 5:
            recaudacion_total(pagos)

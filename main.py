"""Sistema de Gestión de Gimnasio - Trabajo Final Integrador de Python.

Programa principal: arma las estructuras de datos y muestra el menú
general. Cada módulo del sistema se encarga de una parte del problema:

- socios.py        registro de socios y membresías
- cuotas.py        control de cuotas, pagos y promociones
- actividades.py   actividades e inscripciones
- asistencias.py   control de asistencia
- estadisticas.py  estadísticas de concurrencia y recaudación
- validaciones.py  validación de datos ingresados por consola
"""

import validaciones
import socios
import cuotas
import actividades
import asistencias
import estadisticas


def mostrar_menu_principal():
    """Muestra las opciones del menú principal."""
    print("\n========================================")
    print("     SISTEMA DE GESTIÓN DE GIMNASIO")
    print("========================================")
    print("1. Gestión de socios")
    print("2. Cuotas y pagos")
    print("3. Actividades e inscripciones")
    print("4. Control de asistencia")
    print("5. Estadísticas")
    print("0. Salir")


def main():
    """Bucle principal del programa."""
    # Los datos se guardan en memoria mientras el programa está abierto.
    lista_socios = []
    lista_actividades = actividades.crear_actividades_iniciales()
    lista_pagos = []
    lista_asistencias = []

    print("Bienvenido al sistema de gestión del gimnasio.")
    opcion = -1
    while opcion != 0:
        mostrar_menu_principal()
        opcion = validaciones.leer_entero("Opción: ", 0, 5)
        if opcion == 1:
            socios.menu_socios(lista_socios, lista_actividades)
        elif opcion == 2:
            cuotas.menu_cuotas(lista_socios, lista_pagos)
        elif opcion == 3:
            actividades.menu_actividades(lista_socios, lista_actividades)
        elif opcion == 4:
            asistencias.menu_asistencias(lista_socios, lista_actividades, lista_asistencias)
        elif opcion == 5:
            estadisticas.menu_estadisticas(lista_socios, lista_actividades,
                                           lista_pagos, lista_asistencias)
    print("Gracias por usar el sistema. ¡Hasta pronto!")


if __name__ == "__main__":
    main()

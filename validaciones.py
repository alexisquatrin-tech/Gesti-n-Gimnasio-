"""Funciones de validación de entrada de datos por consola.

Todas las funciones repiten el pedido hasta que el usuario
ingrese un valor correcto, para que el programa nunca se corte
por un dato mal cargado.
"""


def leer_entero(mensaje, minimo=None, maximo=None):
    """Pide un número entero y lo valida contra un rango opcional."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Error: el valor mínimo permitido es {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"Error: el valor máximo permitido es {maximo}.")
        else:
            return valor


def leer_texto(mensaje):
    """Pide un texto y valida que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: el texto no puede estar vacío.")
        else:
            return texto


def leer_dni(mensaje):
    """Pide un DNI: solo dígitos, de 7 u 8 caracteres."""
    while True:
        dni = input(mensaje).strip()
        if not dni.isdigit():
            print("Error: el DNI debe contener solo números.")
        elif len(dni) < 7 or len(dni) > 8:
            print("Error: el DNI debe tener 7 u 8 dígitos.")
        else:
            return dni


def dias_del_mes(mes, anio):
    """Devuelve cuántos días tiene un mes, contemplando años bisiestos."""
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return 29
    return dias_por_mes[mes - 1]


def leer_fecha(mensaje):
    """Pide una fecha dd/mm/aaaa y valida que exista en el calendario."""
    while True:
        fecha = input(mensaje).strip()
        partes = fecha.split("/")
        if len(partes) == 3:
            try:
                dia = int(partes[0])
                mes = int(partes[1])
                anio = int(partes[2])
                if (1 <= mes <= 12 and 2020 <= anio <= 2100
                        and 1 <= dia <= dias_del_mes(mes, anio)):
                    return f"{dia:02d}/{mes:02d}/{anio}"
            except ValueError:
                pass
        print("Error: la fecha debe existir y tener el formato dd/mm/aaaa "
              "(por ejemplo 05/07/2026).")


def leer_periodo(mensaje):
    """Pide un período de cuota con formato mm/aaaa y lo devuelve normalizado."""
    while True:
        periodo = input(mensaje).strip()
        partes = periodo.split("/")
        if len(partes) == 2:
            try:
                mes = int(partes[0])
                anio = int(partes[1])
                if 1 <= mes <= 12 and 2020 <= anio <= 2100:
                    return f"{mes:02d}/{anio}"
            except ValueError:
                pass
        print("Error: el período debe tener el formato mm/aaaa (por ejemplo 07/2026).")

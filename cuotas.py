"""Control de cuotas, pagos y promociones."""

import validaciones
import socios as mod_socios

# Promoción vigente: pagando 3 o más meses juntos se aplica un descuento.
MESES_PROMOCION = 3
DESCUENTO_PROMOCION = 0.10  # 10%


def ya_pago(pagos, dni, periodo):
    """Indica si el socio ya tiene registrado el pago de ese período."""
    for pago in pagos:
        if pago["dni"] == dni and pago["periodo"] == periodo:
            return True
    return False


def periodos_consecutivos(periodo_inicial, cantidad):
    """Devuelve una lista de períodos mm/aaaa consecutivos.

    Por ejemplo: ("11/2026", 3) -> ["11/2026", "12/2026", "01/2027"]
    """
    partes = periodo_inicial.split("/")
    mes = int(partes[0])
    anio = int(partes[1])
    periodos = []
    for _ in range(cantidad):
        periodos.append(f"{mes:02d}/{anio}")
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return periodos


def cobrar_cuota(socios, pagos):
    """Registra el pago de una o más cuotas consecutivas de un socio."""
    print("\n--- Cobro de cuotas ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = mod_socios.buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    membresia = mod_socios.MEMBRESIAS[socio["membresia"]]
    precio = membresia["precio"]
    print(f"Socio: {socio['nombre']} | Membresía {membresia['nombre']} | Cuota: ${precio}")
    print(f"Promoción: pagando {MESES_PROMOCION} o más meses juntos hay "
          f"{int(DESCUENTO_PROMOCION * 100)}% de descuento.")
    cantidad = validaciones.leer_entero("Cantidad de meses a pagar (1-12): ", 1, 12)
    periodo_inicial = validaciones.leer_periodo("Primer período a pagar (mm/aaaa): ")
    periodos = periodos_consecutivos(periodo_inicial, cantidad)
    ultimo_anio = int(periodos[-1].split("/")[1])
    if ultimo_anio > 2100:
        print("Error: los períodos a pagar superan el año 2100 y no se pueden registrar.")
        return

    # Antes de cobrar se controla que ningún período esté pago dos veces.
    for periodo in periodos:
        if ya_pago(pagos, dni, periodo):
            print(f"Error: el período {periodo} ya está pago. No se registró ningún pago.")
            return

    total = precio * cantidad
    if cantidad >= MESES_PROMOCION:
        total = total - total * DESCUENTO_PROMOCION
        print(f"Promoción aplicada: {int(DESCUENTO_PROMOCION * 100)}% de descuento "
              f"por pagar {cantidad} meses juntos.")
    monto_por_mes = total / cantidad
    for periodo in periodos:
        pagos.append({"dni": dni, "periodo": periodo, "monto": monto_por_mes})
    print(f"Pago registrado: {cantidad} cuota(s) de {socio['nombre']} "
          f"por un total de ${total:.2f}.")


def consultar_estado(socios, pagos):
    """Informa si un socio tiene paga la cuota de un período."""
    print("\n--- Estado de cuota ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    dni = validaciones.leer_dni("DNI del socio: ")
    socio = mod_socios.buscar_socio(socios, dni)
    if socio is None:
        print("Error: no existe un socio con ese DNI.")
        return
    periodo = validaciones.leer_periodo("Período a consultar (mm/aaaa): ")
    if ya_pago(pagos, dni, periodo):
        print(f"{socio['nombre']} tiene la cuota de {periodo} AL DÍA.")
    else:
        print(f"{socio['nombre']} ADEUDA la cuota de {periodo}.")


def listar_morosos(socios, pagos):
    """Lista los socios que no pagaron la cuota de un período."""
    print("\n--- Socios con cuota adeudada ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
        return
    periodo = validaciones.leer_periodo("Período a controlar (mm/aaaa): ")
    contador = 0
    for socio in socios:
        if not ya_pago(pagos, socio["dni"], periodo):
            print(f"- DNI {socio['dni']} | {socio['nombre']}")
            contador += 1
    if contador == 0:
        print(f"Todos los socios tienen paga la cuota de {periodo}.")
    else:
        print(f"Total de socios que adeudan {periodo}: {contador} de {len(socios)}")


def menu_cuotas(socios, pagos):
    """Submenú de cuotas y pagos."""
    opcion = -1
    while opcion != 0:
        print("\n===== CUOTAS Y PAGOS =====")
        print("1. Cobrar cuota")
        print("2. Consultar estado de cuota de un socio")
        print("3. Listar socios con cuota adeudada")
        print("0. Volver al menú principal")
        opcion = validaciones.leer_entero("Opción: ", 0, 3)
        if opcion == 1:
            cobrar_cuota(socios, pagos)
        elif opcion == 2:
            consultar_estado(socios, pagos)
        elif opcion == 3:
            listar_morosos(socios, pagos)

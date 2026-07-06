# Sistema de Gestión de Gimnasio

Trabajo Final Integrador — Programación en Python (ejecución por consola).

## Integrantes

- Quatrin Oliver, Alexis Javier (Legajo 27880)
- Radis, Liana Guadalupe (Legajo 28366)
- Gutierrez, Pablo Ignacio (Legajo 28135)

**Comisión:** K 1.3 (C)

## Descripción

Sistema de consola para administrar los socios y las actividades de un
gimnasio. Permite:

- **Registro de socios**: alta con validación de DNI único, listado y
  cambio de tipo de membresía (al pasar a una membresía sin actividades
  se dan de baja automáticamente las inscripciones del socio).
- **Membresías y promociones**: tres tipos de membresía (Básica,
  Completa y Estudiante) con distintos precios y alcances, y una
  promoción de 10% de descuento pagando 3 o más meses juntos.
- **Control de cuotas**: cobro de cuotas por período (mm/aaaa),
  consulta del estado de un socio y listado de socios con cuota
  adeudada.
- **Inscripción a actividades**: actividades con días, horario y cupo;
  inscripción y baja de socios con control de cupo, de inscripción
  duplicada y de membresía (la Básica no incluye actividades).
- **Control de asistencia**: registro de asistencias a musculación o a
  una actividad (solo si el socio está inscripto), consulta por fecha e
  historial por socio.
- **Estadísticas de concurrencia**: asistencias por actividad y
  actividad más concurrida, promedio de asistencias por socio y socio
  más constante, porcentaje de ocupación de cupos, socios por tipo de
  membresía y recaudación total.

Los datos se mantienen en memoria (listas y diccionarios) mientras el
programa está en ejecución.

## Estructura del proyecto

| Archivo           | Responsabilidad                                      |
|-------------------|------------------------------------------------------|
| `main.py`         | Menú principal y bucle del programa                  |
| `socios.py`       | Registro de socios y tipos de membresía              |
| `cuotas.py`       | Cobro de cuotas, estado de pagos y promociones       |
| `actividades.py`  | Actividades, inscripciones y control de cupos        |
| `asistencias.py`  | Registro y consulta de asistencias                   |
| `estadisticas.py` | Estadísticas de concurrencia y recaudación           |
| `validaciones.py` | Validación de los datos ingresados por consola       |

## Requisitos técnicos aplicados

- **Estructuras condicionales**: control de membresías, cupos,
  duplicados y estados de cuota.
- **Estructuras repetitivas**: menús con `while`, recorridos de listas
  con `for`.
- **Funciones**: cada operación del sistema es una función con una
  única responsabilidad.
- **Validaciones**: módulo `validaciones.py` (enteros con rango, textos
  no vacíos, DNI, fechas y períodos); el programa nunca se corta por un
  dato mal ingresado.
- **Acumuladores y contadores**: recaudación total, asistencias por
  actividad, morosos, socios por membresía, promedios.
- **Modularización básica**: seis módulos separados por tema.
- **Manejo básico de errores**: `try/except` para conversiones
  numéricas y mensajes de error claros ante datos inexistentes.

## Requisitos y ejecución

Solo se necesita **Python 3.8 o superior** (no usa librerías externas).

```bash
python main.py
```

En Windows también puede usarse `py main.py`.

## Ejemplo de uso

1. Menú `1. Gestión de socios` → `1. Registrar socio` (DNI, nombre,
   edad y membresía).
2. Menú `2. Cuotas y pagos` → `1. Cobrar cuota` (pagando 3 meses o más
   se aplica el descuento).
3. Menú `3. Actividades` → `2. Inscribir socio a una actividad`.
4. Menú `4. Control de asistencia` → `1. Registrar asistencia`.
5. Menú `5. Estadísticas` para ver la concurrencia, ocupación y
   recaudación.

## Video de demostración

<!-- Completar con el enlace al video (máximo 5 minutos) -->
Enlace: _pendiente_

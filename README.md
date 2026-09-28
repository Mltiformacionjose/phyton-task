# Catálogo de Piezas Coleccionables

## Objetivo del programa

Programa de consola escrito en Python que permite gestionar un catálogo
básico de piezas coleccionables: registrar piezas nuevas, consultar el
catálogo, buscar y eliminar piezas, aplicar filtros y calcular métricas
simples (como el precio promedio). El proyecto aplica funciones con
parámetros y `return`, manejo de errores con `try/except`, lanzamiento
de excepciones con `raise`, validaciones tempranas de los datos y
organización del código en módulos separados.

## Contexto del catálogo

Cada pieza coleccionable se representa como un diccionario con la
siguiente forma:

```python
{
    "id": "1",
    "name": "Espada Blasfema",
    "category": "armas",
    "price": 150.5,
    "status": "disponible",
    "description": "figura certificada de colección",
}
```

- Los estados permitidos son: `disponible`, `reservada`, `vendida`.
- La descripción debe contener obligatoriamente la palabra `usada` o
  `certificada`.

El catálogo completo es simplemente una lista de estos diccionarios,
que se mantiene en memoria mientras el programa está en ejecución.

## Funcionalidades implementadas

- **Agregar una pieza**, validando que ningún campo esté vacío, que el
  precio sea numérico y mayor que cero, que el estado sea válido y que
  la descripción contenga la palabra requerida.
- **Listar todas las piezas** del catálogo.
- **Buscar una pieza por id**, sin lanzar error si no existe.
- **Eliminar una pieza por id**, manejando el caso en que no se
  encuentre.
- **Resumen del catálogo**: cantidad de piezas por categoría.
- **Piezas por categoría**: nombres de las piezas de una categoría dada.
- **Verificar si una pieza existe** (booleano).
- **Filtrar por estado** (por ejemplo, mostrar solo las disponibles).
- **Filtrar por precio mínimo**.
- **Calcular el precio promedio** del catálogo, manejando el caso de
  catálogo vacío.
- **Menú interactivo** que conecta cada opción con su función
  correspondiente y captura los errores para mostrar mensajes claros al
  usuario, sin detener el programa.

## Estructura del proyecto

```
catalogo_coleccionables/
├── catalog.py       -> Funciones del catálogo (agregar, listar, buscar, filtrar, métricas)
├── validations.py   -> Funciones de validación de los datos de una pieza
├── main.py          -> Programa principal, menú y flujo de ejecución
└── README.md
```

## Ejemplo de interacción

```
--- Catálogo de Piezas Coleccionables ---
1. Agregar una pieza
2. Mostrar todas las piezas
3. Mostrar piezas disponibles
4. Mostrar el precio promedio
5. Buscar una pieza por identificador
6. Eliminar una pieza
7. Salir

Elige una opción: 1

Ingresa los datos de la nueva pieza:
Id: 1
Nombre: Espada Blasfema
Categoría: armas
Precio: 150.5
Estados permitidos: disponible, reservada, vendida
Estado: disponible
Descripción (debe incluir 'usada' o 'certificada'): figura certificada de colección
Pieza 'Espada Blasfema' agregada correctamente.

Elige una opción: 4

Precio promedio del catálogo: $150.50

Elige una opción: 6

Ingresa el id de la pieza a eliminar: 99
Error al eliminar la pieza: No se encontró ninguna pieza con el id '99'.
No se pudo eliminar la pieza con id '99'.
```

## Tecnologías utilizadas

- Python 3 (sin librerías externas, solo la librería estándar).

## Cómo ejecutar el programa

1. Cloná el repositorio y entrá en la carpeta del proyecto:
   ```
   git clone <url-del-repositorio>
   cd catalogo_coleccionables
   ```
2. Ejecutá el programa con Python 3:
   ```
   python3 main.py
   ```
3. Usá el menú numerado para interactuar con el catálogo.

"""
main.py

Interactive text menu for the collectible pieces catalog. Each option is
handled by a small function that calls catalog.py and wraps the calls in
try/except so the user always sees a clear message instead of a crash.
"""

from catalog import (
    add_piece,
    list_pieces,
    find_piece_by_id,
    remove_piece,
    get_average_price,
    filter_by_status,
)
from validations import ALLOWED_STATUSES


def show_menu():
    print("\n--- Catálogo de Piezas Coleccionables ---")
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar una pieza por identificador")
    print("6. Eliminar una pieza")
    print("7. Salir")


def handle_add_piece(catalog):
    print("\nIngresa los datos de la nueva pieza:")
    piece_id = input("Id: ")
    name = input("Nombre: ")
    category = input("Categoría: ")
    price_text = input("Precio: ")
    print(f"Estados permitidos: {', '.join(ALLOWED_STATUSES)}")
    status = input("Estado: ")
    description = input("Descripción (debe incluir 'usada' o 'certificada'): ")

    try:
        price = float(price_text)
    except ValueError:
        print("Error: el precio debe ser un número (por ejemplo 25.5).")
        return

    try:
        piece = add_piece(piece_id, name, category, price, status, description)
        catalog.append(piece)
        print(f"Pieza '{piece['name']}' agregada correctamente.")
    except ValueError as error:
        print(f"Error al agregar la pieza: {error}")


def handle_list_pieces(catalog):
    try:
        names = list_pieces(catalog)
        if len(names) == 0:
            print("\nEl catálogo está vacío.")
        else:
            print("\nPiezas en el catálogo:")
            for name in names:
                print(f"- {name}")
    except ValueError as error:
        print(f"Error al listar las piezas: {error}")


def handle_show_available(catalog):
    try:
        available_pieces = filter_by_status(catalog, "disponible")
        if len(available_pieces) == 0:
            print("\nNo hay piezas disponibles en este momento.")
        else:
            print("\nPiezas disponibles:")
            for piece in available_pieces:
                print(f"- {piece['name']} (${piece['price']})")
    except ValueError as error:
        print(f"Error al filtrar las piezas: {error}")


def handle_average_price(catalog):
    try:
        average = get_average_price(catalog)
        print(f"\nPrecio promedio del catálogo: ${average:.2f}")
    except ValueError as error:
        print(f"Error al calcular el precio promedio: {error}")


def handle_find_piece(catalog):
    piece_id = input("\nIngresa el id de la pieza a buscar: ")
    try:
        piece = find_piece_by_id(catalog, piece_id)
        if piece is None:
            print(f"No se encontró ninguna pieza con el id '{piece_id}'.")
        else:
            print("\nPieza encontrada:")
            for key, value in piece.items():
                print(f"{key}: {value}")
    except ValueError as error:
        print(f"Error al buscar la pieza: {error}")


def handle_remove_piece(catalog):
    piece_id = input("\nIngresa el id de la pieza a eliminar: ")
    try:
        remove_piece(catalog, piece_id)
        print(f"Pieza con id '{piece_id}' eliminada correctamente.")
    except ValueError as error:
        print(f"Error al eliminar la pieza: {error}")


def main():
    catalog = []
    running = True

    while running:
        show_menu()
        option = input("\nElige una opción: ")

        if option == "1":
            handle_add_piece(catalog)
        elif option == "2":
            handle_list_pieces(catalog)
        elif option == "3":
            handle_show_available(catalog)
        elif option == "4":
            handle_average_price(catalog)
        elif option == "5":
            handle_find_piece(catalog)
        elif option == "6":
            handle_remove_piece(catalog)
        elif option == "7":
            print("\n¡Hasta luego!")
            running = False
        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

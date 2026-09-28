"""
catalog.py

This module contains all the functions used to manage the collectible
pieces catalog: adding, listing, searching, removing, filtering and
calculating basic metrics. Every function focuses on a single task and
relies on validations.py to check the data it receives.
"""

from validations import (
    validate_not_empty,
    validate_price,
    validate_status,
    validate_description,
)


def add_piece(piece_id, name, category, price, status, description):
    """
    Build and return a new piece (dictionary) after validating every field.

    Raises ValueError if any of the fields is invalid.
    """
    validate_not_empty(piece_id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")
    validate_price(price)
    validate_status(status)
    validate_description(description)

    piece = {
        "id": piece_id,
        "name": name,
        "category": category,
        "price": float(price),
        "status": status,
        "description": description,
    }
    return piece


def list_pieces(catalog):
    """Return a list with the names of every piece in the catalog."""
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    names = []
    for piece in catalog:
        names.append(piece["name"])
    return names


def find_piece_by_id(catalog, piece_id):
    """
    Return the piece whose id matches piece_id, or None if it is not found.

    Not finding a piece is not treated as an error, so no exception is
    raised in that case.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    for piece in catalog:
        if piece["id"] == piece_id:
            return piece
    return None


def remove_piece(catalog, piece_id):
    """
    Remove the piece with the given id from the catalog.

    Returns True if the piece was removed successfully, or False if the
    piece was not found (the error is caught and handled here).
    """
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    try:
        piece = find_piece_by_id(catalog, piece_id)
        if piece is None:
            raise ValueError(f"No se encontró ninguna pieza con el id '{piece_id}'.")
        catalog.remove(piece)
        return True
    except ValueError as error:
        print(f"Error al eliminar la pieza: {error}")
        return False


def get_catalog_summary(catalog):
    """Return a dictionary with the number of pieces per category."""
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    summary = {}
    for piece in catalog:
        category = piece["category"]
        if category in summary:
            summary[category] += 1
        else:
            summary[category] = 1
    return summary


def get_pieces_by_category(catalog, category):
    """
    Return a list with the names of the pieces that belong to the given
    category. Returns an empty list if there are no matches.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    names = []
    for piece in catalog:
        if piece["category"] == category:
            names.append(piece["name"])
    return names


def piece_exists(catalog, piece_id):
    """Return True if a piece with the given id exists, False otherwise."""
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    return find_piece_by_id(catalog, piece_id) is not None


def filter_by_status(catalog, status):
    """Return a list with the pieces that have the given status."""
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    validate_status(status)

    result = []
    for piece in catalog:
        if piece["status"] == status:
            result.append(piece)
    return result


def filter_by_min_price(catalog, min_price):
    """Return the pieces whose price is greater than min_price."""
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    if not isinstance(min_price, (int, float)) or isinstance(min_price, bool):
        raise ValueError("El precio mínimo debe ser un valor numérico.")

    result = []
    for piece in catalog:
        if piece["price"] > min_price:
            result.append(piece)
    return result


def get_average_price(catalog):
    """
    Return the average price of every piece in the catalog.

    Returns 0 if the catalog is empty, instead of raising an error.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    if len(catalog) == 0:
        return 0

    total = 0
    for piece in catalog:
        total += piece["price"]
    return total / len(catalog)

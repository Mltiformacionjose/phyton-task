"""
catalog.py

Functions to manage the collectible pieces catalog: add, list, search,
remove, filter and compute metrics. Data validation lives in validations.py.
"""

from validations import (
    validate_not_empty,
    validate_price,
    validate_status,
    validate_description,
)


def _validate_catalog(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")


def add_piece(piece_id, name, category, price, status, description):
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
    _validate_catalog(catalog)
    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog, piece_id):
    """Return the piece with the given id, or None if it does not exist."""
    _validate_catalog(catalog)

    for piece in catalog:
        if piece["id"] == piece_id:
            return piece
    return None


def remove_piece(catalog, piece_id):
    """Remove the piece with the given id. Returns True on success."""
    _validate_catalog(catalog)

    piece = find_piece_by_id(catalog, piece_id)
    if piece is None:
        raise ValueError(f"No se encontró ninguna pieza con el id '{piece_id}'.")
    catalog.remove(piece)
    return True


def get_catalog_summary(catalog):
    """Return a dict with the count of pieces per category."""
    _validate_catalog(catalog)

    summary = {}
    for piece in catalog:
        category = piece["category"]
        summary[category] = summary.get(category, 0) + 1
    return summary


def get_pieces_by_category(catalog, category):
    _validate_catalog(catalog)
    return [piece["name"] for piece in catalog if piece["category"] == category]


def piece_exists(catalog, piece_id):
    _validate_catalog(catalog)
    return find_piece_by_id(catalog, piece_id) is not None


def filter_by_status(catalog, status):
    _validate_catalog(catalog)
    validate_status(status)
    return [piece for piece in catalog if piece["status"] == status]


def filter_by_min_price(catalog, min_price):
    _validate_catalog(catalog)

    if not isinstance(min_price, (int, float)) or isinstance(min_price, bool):
        raise ValueError("El precio mínimo debe ser un valor numérico.")

    return [piece for piece in catalog if piece["price"] > min_price]


def get_average_price(catalog):
    """Return the average price, or 0 if the catalog is empty."""
    _validate_catalog(catalog)

    if len(catalog) == 0:
        return 0

    return sum(piece["price"] for piece in catalog) / len(catalog)

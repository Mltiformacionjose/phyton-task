"""
validations.py

This module contains small, independent functions used to validate the
data of a single piece before it is stored in the catalog. Each function
has a single responsibility and raises a ValueError with a clear message
when the data is not valid. None of these functions print anything: it
is up to whoever calls them to decide how to show or handle the error.
"""

ALLOWED_STATUSES = ["disponible", "reservada", "vendida"]
DESCRIPTION_KEYWORDS = ["usada", "certificada"]


def validate_not_empty(value, field_name):
    """Raise ValueError if value is None or an empty/blank string."""
    if value is None or str(value).strip() == "":
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")


def validate_price(price):
    """Raise ValueError if price is not numeric or is not greater than zero."""
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise ValueError("El precio debe ser un valor numérico.")

    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")


def validate_status(status):
    """Raise ValueError if status is not one of the allowed statuses."""
    if status not in ALLOWED_STATUSES:
        allowed = ", ".join(ALLOWED_STATUSES)
        raise ValueError(f"Estado inválido: '{status}'. Estados permitidos: {allowed}.")


def validate_description(description):
    """Raise ValueError if description does not contain 'usada' or 'certificada'."""
    if not isinstance(description, str):
        raise ValueError("La descripción debe ser un texto.")

    description_lower = description.lower()

    contains_keyword = False
    for keyword in DESCRIPTION_KEYWORDS:
        if keyword in description_lower:
            contains_keyword = True

    if not contains_keyword:
        raise ValueError(
            "La descripción debe contener la palabra 'usada' o 'certificada'."
        )

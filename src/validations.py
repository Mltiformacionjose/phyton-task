"""
validations.py

Small helpers that validate the data of a single piece. Each one raises
a ValueError with a clear message when the data is invalid; none of them
print anything: it is up to the caller to handle the error.
"""

ALLOWED_STATUSES = ["disponible", "reservada", "vendida"]
DESCRIPTION_KEYWORDS = ["usada", "certificada"]


def validate_not_empty(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")


def validate_price(price):
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise ValueError("El precio debe ser un valor numérico.")

    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")


def validate_status(status):
    if status not in ALLOWED_STATUSES:
        allowed = ", ".join(ALLOWED_STATUSES)
        raise ValueError(f"Estado inválido: '{status}'. Estados permitidos: {allowed}.")


def validate_description(description):
    if not isinstance(description, str):
        raise ValueError("La descripción debe ser un texto.")

    if not any(keyword in description.lower() for keyword in DESCRIPTION_KEYWORDS):
        raise ValueError(
            "La descripción debe contener la palabra 'usada' o 'certificada'."
        )

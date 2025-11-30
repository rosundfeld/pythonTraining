def convert_number(valor):
    try:
        numero = float(valor)
        return numero
    except (ValueError, TypeError):
        return None
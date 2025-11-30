def receber(valor, gorjeta):
    try:
        val_converted = float(valor)
    except (ValueError, TypeError):
        return None
    
    gorjeta_percent = convert_gorjeta(gorjeta)
    if gorjeta_percent is None:
        return None

    if val_converted <= 0 or gorjeta < 0:
        return None
    
    valores = {}
    valores['gorjeta'] = val_converted * (gorjeta_percent)
    valores['total'] = val_converted + (val_converted *  gorjeta_percent)
    return valores

def convert_gorjeta(valor):
    try:
        gorjeta = float(valor)
    except (ValueError, TypeError):
        return None
    # se maior que 1, assume entrada em porcentagem (ex: 10 -> 0.10)
    if gorjeta > 1:
        return gorjeta / 100
    return gorjeta

    
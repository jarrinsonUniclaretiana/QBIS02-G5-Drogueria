MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}


def validar_precio(precio):
    """Valida que el precio sea un número mayor que cero."""
    try:
        precio = float(precio)
        if precio <= 0:
            return None
        return precio
    except (ValueError, TypeError):
        return None


def validar_unidades(unidades, permitir_cero=False):
    """Valida que las unidades sean un número entero no negativo."""
    try:
        unidades = int(unidades)
        minimo = 0 if permitir_cero else 1
        if unidades < minimo:
            return None
        return unidades
    except (ValueError, TypeError):
        return None


def validar_mes(mes):
    """Valida que el mes esté entre 1 y 12."""
    try:
        mes = int(mes)
        return mes if 1 <= mes <= 12 else None
    except (ValueError, TypeError):
        return None


def texto_medicamento(codigo, medicamento):
    """Arma el texto para mostrar un medicamento en pantalla."""
    nombre, precio, unidades, mes = medicamento
    nombre_mes = MESES.get(mes, "Mes no válido")
    return (
        f"Código: {codigo} | Nombre: {nombre} | "
        f"Precio: ${precio:,.2f} | Unidades: {unidades} | "
        f"Vencimiento: {nombre_mes}"
    )

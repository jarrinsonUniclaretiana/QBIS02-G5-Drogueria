# Diccionario que almacena los números de los meses y sus respectivos nombres
MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}


def validar_precio(precio):
    """
    Recibe: un precio que puede ser numerico o texto.
    Procesa: convierte el precio a numero decimal y verifica que sea mayor que cero.
    Devuelve: el precio convertido a float si es válido; None si no cumple las condiciones.
    """
    try:
        precio = float(precio)
        if precio <= 0:
            return None
        return precio
    except (ValueError, TypeError):
        return None


def validar_unidades(unidades, permitir_cero=False):
    """
    Recibe: las unidades y un parámetro que indica si se permite el valor cero.
    Procesa: convierte las unidades a entero y verifica que cumplan el mínimo permitido.
    Devuelve: las unidades como entero si son válidas; None si no cumplen las condiciones.
    """
    try:
        unidades = int(unidades)
        cantidad_minima = 0 if permitir_cero else 1
        if unidades < cantidad_minima:
            return None
        return unidades
    except (ValueError, TypeError):
        return None


def validar_mes(mes):
    """
    Recibe: un número o texto que representa el mes.
    Procesa: convierte el dato a entero y verifica que esté entre 1 y 12.
    Devuelve: el número del mes si es válido; None si está fuera del rango o no es válido.
    """
    try:
        mes = int(mes)
        return mes if 1 <= mes <= 12 else None
    except (ValueError, TypeError):
        return None


def texto_medicamento(codigo, medicamento):
    """
    Recibe: el código del medicamento y una tupla con nombre, precio, unidades y mes.
    Procesa: organiza los datos y convierte el número del mes en su nombre correspondiente.
    Devuelve: una cadena de texto con toda la información del medicamento organizada.
    """
    nombre, precio, unidades, mes = medicamento
    nombre_mes = MESES.get(mes, "Mes no válido")
    return (
        f"Código: {codigo} | Nombre: {nombre} | "
        f"Precio: ${precio:,.2f} | Unidades: {unidades} | "
        f"Vencimiento: {nombre_mes}"
    )
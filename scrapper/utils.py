import re

def clean_price(price_str: str) -> float:
    """Limpia y convierte precios a float"""
    try:
        # Elimina símbolos no numéricos excepto punto decimal
        cleaned = re.sub(r'[^\d.]', '', price_str)
        return float(cleaned)
    except ValueError:
        return 0.0
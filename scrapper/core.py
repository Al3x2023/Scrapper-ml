import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict
from scrapper.utils import clean_price  

class MercadoLibreScraper:
    HEADERS = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
        )
    }

    def __init__(self, base_url: str = "https://listado.mercadolibre.com.ar"):
        self.base_url = base_url
        self.session = requests.Session()

    def search_products(self, query: str, limit: int = 10) -> List[Dict[str, str]]:
        """Busca productos y extrae datos estructurados de MercadoLibre."""
        url = f"{self.base_url}/{query.replace(' ', '-')}"
        try:
            response = self.session.get(url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('li', class_='ui-search-layout__item')[:limit]

            products = []
            for item in items:
                product = {
                    'nombre': self._extract_title(item),
                    'precio': clean_price(self._extract_price(item)),
                    'link': self._extract_url(item)
                }
                products.append(product)

            return products

        except requests.RequestException as e:
            print(f"Error de conexión: {e}")
        except Exception as e:
            print(f"Error al scrapear: {e}")

        return []

    def _extract_title(self, item) -> str:
    # Intenta encontrar el título por diferentes métodos según la estructura actual
        title_tag = item.find('h2')
        if title_tag:
            return title_tag.get_text(strip=True)

    # Alternativamente, algunos productos tienen el título en un 'span' dentro del enlace
        link_tag = item.find('a', class_='ui-search-link')
        if link_tag and link_tag.get('title'):
            return link_tag['title']

    # Otro fallback: buscar un span que contenga el título
        span_title = item.find('span', class_='ui-search-item__title')
        if span_title:
            return span_title.get_text(strip=True)

        return 'Sin título'
    def _extract_price(self, item) -> str:
        fraction = item.find('span', class_='andes-money-amount__fraction')
        cents = item.find('span', class_='andes-money-amount__cents')
        if fraction:
            price = fraction.get_text(strip=True)
            if cents:
                price += f".{cents.get_text(strip=True)}"
            return price
        return '0'

    def _extract_url(self, item) -> str:
        link_tag = item.find('a', href=True)
        return link_tag['href'] if link_tag else '#'

    def export_to_csv(self, products: List[Dict[str, str]], filename: str = "output/productos.csv") -> None:
        """Exporta los productos extraídos a un archivo CSV."""
        df = pd.DataFrame(products)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Datos exportados a {filename}")

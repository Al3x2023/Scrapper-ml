📦 MercadoLibre Scraper
Un web scraper para extraer datos de productos de MercadoLibre y exportarlos a CSV

🚀 Características
Extrae información detallada de productos (título, precio, ubicación, envío gratis)

Exporta datos a CSV listo para análisis

Configurable y fácil de extender

Manejo robusto de errores

📦 Requisitos
Python 3.11+

Pipenv (recomendado) o pip

🛠 Instalación
Clona el repositorio:


git clone https://github.com/tu-usuario/Scrapper-ml.git

cd Scrapper-ml
Instala dependencias:


pip install -r requirements.txt
O con Pipenv:


pipenv install
pipenv shell

🖥 Uso
Ejecución básica:

python scraper.py

Parámetros disponibles (edita scraper.py):
query: Término de búsqueda (ej: "articulos para automoviles")

limit: Número máximo de productos a extraer todos

output_file: Ruta del archivo CSV de salida

Ejemplo de salida:
🔍 Buscando productos en MercadoLibre...

📦 Resultados encontrados:
1. Notebook Lenovo Ideapad 3 8gb 256gb Ssd - $450.000 (Capital Federal)
2. Notebook Lenovo Thinkpad E15 - $620.000 (Buenos Aires)
...
✅ Datos exportados a output/productos.csv (15 productos)
📂 Estructura del proyecto
mercadolibre-scraper/
├── scraper.py          # Código principal del scraper
├── output/
│   └── productos.csv   # Ejemplo de salida
├── requirements.txt    # Dependencias
└── README.md           # Este archivo
🛠 Personalización
Edita estas variables en scraper.py:

python
# Configuración básica
BASE_URL = "https://listado.mercadolibre.com.ar"
DEFAULT_QUERY = "notebook lenovo"
MAX_RESULTS = 15
OUTPUT_FILE = "output/productos.csv"
⚠️ Consideraciones legales
Revisa el robots.txt de MercadoLibre antes de usar

No hagas demasiadas peticiones consecutivas

Considera agregar delays entre requests

📄 Licencia
MIT License

🤝 Contribuir
Haz fork del proyecto

Crea una rama (git checkout -b feature/nueva-funcionalidad)

Haz commit de tus cambios (git commit -am 'Agrega nueva funcionalidad')

Haz push a la rama (git push origin feature/nueva-funcionalidad)

Abre un Pull Request
from scrapper.core import MercadoLibreScraper

if __name__ == "__main__":
    scraper = MercadoLibreScraper()

    query = "Cubre patentes magicas para evitar fotomultas o radares no"
    print(f"🔍 Buscando productos en MercadoLibre: '{query}'")

    all_products = []
    page = 1
    productos_por_pagina = 50  # Aprox. cuántos productos por página muestra MercadoLibre
    max_pages = 20  # Establece un límite para evitar scrapear infinito

    while True:
        print(f"📄 Página {page}...")
        productos = scraper.search_products(query + f"_Desde_{(page - 1) * productos_por_pagina}", limit=productos_por_pagina)

        if not productos:
            break

        all_products.extend(productos)
        page += 1

        if page > max_pages:  # Evita ciclos infinitos si MercadoLibre no para
            break

    if all_products:
        print(f"\n✅ Total productos encontrados: {len(all_products)}")
        for idx, prod in enumerate(all_products, 1):
            print(f"{idx}. {prod['nombre']} - ${prod['precio']}")
        
        scraper.export_to_csv(all_products)
    else:
        print("❌ No se encontraron productos")

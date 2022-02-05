from bs4 import BeautifulSoup
import requests

try:
    url = 'https://www.alkosto.com/celulares/telefonos-celulares/iphone/c/BI_M009_ALKOS'

    result: requests.get(url)
    result.raise_for_status()

    soup: BeautifulSoup(result.text, "html.parser")
    alkosto_productos = soup.find_all('li', class_="product__list--item product__list--alkosto")

    for alkosto_producto in alkosto_productos:

        titulo = alkosto_producto.find(
        'h2', class_='product__information--name').a.text.strip()
        precio = alkosto_producto.find(
        'p', class_="product__price--discounts__price").span.text.strip()
        url = alkosto_producto.find('a', href_=()).href

        print(titulo, precio)

except:
    print("A la mierda Tilin")


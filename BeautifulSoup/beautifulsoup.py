from bs4 import BeautifulSoup
import requests
import json

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}
page_url = "https://www.xiaomi-store.co/smartphones"
page = requests.get(page_url)#, headers=headers)#, params={"q": "python"})
print('status code:', page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

#titulos = soup.find_all('h3', attrs={'class':'vtex-product-summary-2-x-productNameContainer vtex-product-summary-2-x-productNameContainer--search-new mv0 vtex-product-summary-2-x-nameWrapper vtex-product-summary-2-x-nameWrapper--search-new overflow-hidden c-on-base f5'})
#titulos = [ i.text  for i in titulos]
#titulos = [t.get('data-name') for t in titulos]

productos = soup.find_all('div', attrs={'class':'vtex-yotpo-1-x-ratingInlineContainer'})#,  attrs={"class": 'vtex-yotpo-1-x-ratingInlineContainer center yotpo bottomLine yotpo-small'})
#print(productos)

lista_productos = []

for producto in productos:
    lista_productos.append(
        {
            'name': producto.get('data-name'),
            'url': producto.get('data-url'),
            'imageUrl': producto.get('data-image-url'),
            'price': producto.get('data-price'), 
        },
    )

with open('products_info.json', 'w') as f:
    json.dump(lista_productos, f)

""" 
titulos = [t.get('data-name') for t in productos]
print("titulos: ", titulos)

urls = [ u.get('data-url') for u in productos]
print("urls:", urls)

image_urls = [ i.get('data-image-url') for i in productos]
print("image_urls:", image_urls)

precios = [ p.get('data-price') for p in productos ]
print("precios:",precios) """
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }


def amazonScrapper(url):
    try:
        html = requests.get(url, headers=headers).text
    except requests.exceptions.RequestException as err: 
        print(f"An error occurred while trying to access the URL: {err}")
        return None, None, None

    soup = BeautifulSoup(html, 'lxml')

    if not soup.find('div', class_='a-alert-content'):
        print("Product not found on Amazon.")
        return None, None, None
    try:
        title_div = soup.find('div', id='titleSection')
        title = title_div.find('h1', id='title').text.strip()
        product_name = title
    except Exception as err:
        print(
            f"An error occurred while trying to get the name of the product: {err}")
        return None, None, None

    if product_name is None:
        print("Unable to get name of the product please try again later or try another product")
        return None, None, None

    try:
        price_span = soup.find('span', class_='a-price-whole')
        price = price_span.text.strip()
    except Exception as e:
        print(
            f"An error occurred while trying to get the price of the product: {err}")
        return None, None, None

    if price is None:
        print("Unable to get price of the product please try again later or try another product")
        return None, None, None

    print(f"Price of {product_name} on Amazon: ₹{price}\n")

    return product_name, "Amazon", price
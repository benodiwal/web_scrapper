import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"
    }

def flipkartScrapper(url):
    try:
        html = requests.get(url, headers=headers).text
    except requests.exceptions.RequestException:
        return None, None, None
    
    soup = BeautifulSoup(html, 'lxml')

    if not soup.find('span', class_='B_NuCI'):
        print("Product not found on Flipkart")
        return None, None, None

    try:
        title = soup.find('span', class_='B_NuCI').text.strip()
        product_name = title
    except Exception:
        return None, None, None

    if product_name is None:
        return None, None, None

    try:
        price = soup.find('div', class_='_30jeq3 _16Jk6d').text.strip()
    except Exception:
        return None, None, None

    if price is None:
        return None, None, None
    
    print(f"Price of {product_name} on Flipkart: {price}\n")

    return product_name, "Flipkart", price
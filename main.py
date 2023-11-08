from flipkart_scrapper import flipkartScrapper
from amazon_scrapper import amazonScrapper
from table import make_table

def main():
    
    prices = []
    sources = []
    names = []
    
    for i in range(2):
        value = "first" if i == 0 else "second"
        url = input(f"Please enter the url of the {value} product you wanna scrap: ")
        print("\n")
        
        if 'flipkart' in url:
            [name, source, price] = flipkartScrapper(url=url)
            if name == None or source == None or price == None:
                break
            prices.append(price)
            sources.append(source)
            names.append(name)
        
        elif 'amazon' in url:
            [name, source, price] = amazonScrapper(url=url)
            if name == None or source == None or price == None:
                break
            prices.append(price)
            sources.append(source)
            names.append(name)
        
        else:
            print("Invalid URL, please try some other URL")
            break
    
    #  Resprenting the price in table format    
        
    # Comparing price
    if prices:
        new_prices = [_price.replace(',', '').replace('.', '').replace('₹', '') for _price in prices]
        make_table(prices=new_prices, sources=sources)
        print(f"->> Min price for {names[new_prices.index(min(new_prices))]} is ₹{prices[new_prices.index(min(new_prices))].replace('.', '').replace('₹', '')} on {sources[new_prices.index(min(new_prices))]}")
    
main()

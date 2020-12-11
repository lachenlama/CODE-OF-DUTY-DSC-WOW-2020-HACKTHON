#functions of the main scrape.py file


def get_title(soup):
    try:
        title = soup.find('span', attrs={'id':'productTitle'})
    except AttributeError:
        title = ""
    return title


def get_price_mrp(soup):
    try:
        mrp = soup.find('span', attrs={'id':'priceBlockStrikePriceString a-text-strike'}).text()
    except AttributeError:
        mrp = ''
    return mrp


def get_price_deal_price(soup):
    try:
        deal_price = soup.find('span', attrs={'class':'priceBlockStrikePriceString a-text-strike'}).text()
    except:
        deal_price = ""
    return deal_price


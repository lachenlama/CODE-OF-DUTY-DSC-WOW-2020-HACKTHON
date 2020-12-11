#functions of the main scrape.py file


def get_title(soup):
    try:
        title = soup.find('span', attrs={'id':'productTitle'}).string.strip()
    except AttributeError:
        title = ""
    return title


def get_price_mrp(soup):
    try:
        mrp = soup.find('span', attrs={'id':'priceBlockStrikePriceString a-text-strike'}).string.strip()
    except AttributeError:
        mrp = 'Below'
    return mrp


def get_price_deal_price(soup):
    try:
        deal_price = soup.find('span', attrs={'id':'priceblock_dealprice'}).string.strip()
    except AttributeError:
        try:
            deal_price = soup.find('span', attrs={'id':'priceblock_ourprice'}).string.strip()
        except:
            deal_price = ""
    return deal_price


def get_rating(soup):
    try:
        rating = soup.find('i', attrs={'class':'a-icon a-icon-star a-star-4-5'}).sting.strip()
    except AttributeError:
        try:
            rating = soup.find('span', attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ''
    return rating


def get_review(soup):
    try:
        review = soup.find('span', attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review = 'None'
    return review


def get_availability(soup):
    try:
        available = soup.find('div', attrs={'id':'availability'}).string.strip()
    except AttributeError:
        try:
            available = soup.find('span', attrs={'class':'a-size-medium a-color-success'}).string.strip()
        except:
            available = 'Not available'
    return available
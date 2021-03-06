from functions import get_title
from functions import get_price_mrp
from functions import get_price_deal_price
from functions import get_rating
from functions import get_review
from functions import get_availability
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import html5lib
import bs4


def search():
    URL = "https://www.amazon.in/"
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(10)
    driver.get(URL)
    #Using selenium to drive the browser
    search_button = driver.find_element_by_id("twotabsearchtextbox")
    search_term = str(input("What do you want?\n:"))
    search_button.send_keys(search_term)
    search_button.send_keys(Keys.ENTER)
        
    soup = bs4.BeautifulSoup(driver.page_source, "html5lib")

    links = soup.find_all('a', attrs={"class":"a-link-normal s-no-outline"})[:10]
    links_storage = []
    for link in links:
        links_storage.append(link.get('href'))

    for link in links_storage:
        url = URL + link
        new_webpage = driver.get(url)
        new_soup = bs4.BeautifulSoup(driver.page_source, "html5lib")
        
        print()
        print("Name= ", get_title(new_soup))
        print("Mrp= ", get_price_mrp(new_soup))
        print("You pay= ", get_price_deal_price(new_soup))
        print("Rating= ", get_rating(new_soup))
        print("Reviews= ", get_review(new_soup))
        print("Availability= ", get_availability(new_soup))
        print("|")
        print("Link for the product= ", url)
        print("...................................next")
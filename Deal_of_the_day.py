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


HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}


def deal_of_the_day():
    URL = "https://www.amazon.in/"
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(10)
    driver.get(URL)
    #using selenium to open deals of the day
    deal_of_the_day = driver.find_element_by_xpath("//a[@href='/gp/goldbox?ref_=nav_cs_gb']")
    deal_of_the_day.click()
        
    nostarchsoup = bs4.BeautifulSoup(driver.page_source, "html5lib")

    links_of_deals_otd = nostarchsoup.find_all("a", attrs={'class':"a-button-text a-text-center"})[:5]
    links_of_deals_otd_storage = []
    for i in links_of_deals_otd:
        links_of_deals_otd_storage.append(i.get('href'))
   
    for j in links_of_deals_otd_storage:
        new_webpage = driver.get(j)
        new_nostarchsoup = bs4.BeautifulSoup(driver.page_source, "html5lib")
        try:
            print()
            print("Name= ", get_title(new_nostarchsoup))
            print("Mrp= ", get_price_mrp(new_nostarchsoup))
            print("You pay= ", get_price_deal_price(new_nostarchsoup))
            print("Rating= ", get_rating(new_nostarchsoup))
            print("Reviews= ", get_review(new_nostarchsoup))
            print("Availability= ", get_availability(new_nostarchsoup))
            print("|")
            print("Link for the product= ", j)
            print("...................................next")
        except AttributeError:
            print()
            
        finally:
            items_in_page = new_nostarchsoup.find_all('a', attrs={'class':'a-link-normal'})[:5]
            items_in_page_storage = []
            for elements in items_in_page:
                items_in_page_storage.append(elements.get('href'))
            for each_elements in items_in_page_storage:
                new_webpage_plus = driver.get(URL + each_elements)
                new_nostarchsoup_plus = bs4.BeautifulSoup(driver.page_source, "html5lib")
                
                print()
                print("Name= ", get_title(new_nostarchsoup_plus))
                print("Mrp= ", get_price_mrp(new_nostarchsoup_plus))
                print("You pay= ", get_price_deal_price(new_nostarchsoup_plus))
                print("Rating= ", get_rating(new_nostarchsoup_plus))
                print("Reviews= ", get_review(new_nostarchsoup_plus))
                print("Availability= ", get_availability(new_nostarchsoup_plus))
                print("|")
                print("Link for the product= ", URL + each_elements)
                print("...................................next")
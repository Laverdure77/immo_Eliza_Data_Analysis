from selenium import webdriver
from selenium.webdriver.common.by import By
import data_acquisition.data_filter_fr as fr
import data_acquisition.data_filter_en as en

def immoweb_scrapping(url):
    if("projet" in url or "project" in url):
        pass
    else :
        my_dict = dict()
        tab = url.split("/")
        my_dict["id"] = int(tab[-1].strip())
        my_dict["Locality"] = tab[7].capitalize()

        if(tab[3] == "fr") :
            return immoweb_fr_scrapping(url, my_dict)
        elif(tab[3] == "en") :
            return immoweb_en_scrapping(url, my_dict)
        else :
            pass

def immoweb_fr_scrapping(url, my_dict):

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--private")
    driver = webdriver.Firefox(options=options)

    driver.get(url)

    try :
        title = driver.find_element(By.XPATH, "//h1[@class='classified__title']").text
    except :
        return

    if(title.find("à vendre")>-1) :
        my_dict["Type of sale"] = "à vendre"
        my_dict.update(fr.get_properties(title.replace(" à vendre", "")))
    elif(title.find("à louer")>-1) :
        my_dict["Type of sale"] = "à louer"
        my_dict.update(fr.get_properties(title.replace(" à louer", "")))
    else :
        my_dict["Type of sale"] = None

    my_dict["Price_attr"] = driver.find_element(By.XPATH, "//p[@class='classified__price']//span[@class='sr-only']").text

    for key, value in zip(driver.find_elements(By.XPATH, "//th[@class='classified-table__header']"), driver.find_elements(By.XPATH, "//td[@class='classified-table__data']")):
        my_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")

    driver.close()

    return fr.immoweb_filter(my_dict)

def immoweb_en_scrapping(url, my_dict):

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--private")
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    try :
        title = driver.find_element(By.XPATH, "//h1[@class='classified__title']").text
    except :
        return
    
    if(title.find("for sale")>-1) :
        my_dict["Type of sale"] = "for sale"
        my_dict.update(en.get_properties(title.replace(" for sale", "")))
    elif(title.find("for rent")>-1) :
        my_dict["Type of sale"] = "for rent"
        my_dict.update(en.get_properties(title.replace(" for rent", "")))
    else :
        my_dict["Type of sale"] = None

    my_dict["Price_attr"] = driver.find_element(By.XPATH, "//p[@class='classified__price']//span[@class='sr-only']").text

    for key, value in zip(driver.find_elements(By.XPATH, "//th[@class='classified-table__header']"), driver.find_elements(By.XPATH, "//td[@class='classified-table__data']")):
        my_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")

    driver.close()

    return en.immoweb_filter(my_dict)

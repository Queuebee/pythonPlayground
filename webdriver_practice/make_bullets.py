import getpass
import time
from random import randint as randy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException #needs to be used still

    
def getcreds():
    """ get credentials """
    from feli_credits import username, password
    return username, password

def get_objects():
    """ get owned objects"""
    from owned_objects import owned_factories
    return owned_factories

def login(driver, username, password):
    """login using username, password"""
    print("start login sequence")
    print("loading site...")
    driver.get("http://www.maffiaworld.nl/")
    print("LOADED")
    time.sleep(1)
    print("find username inputfield...")
    element = driver.find_element_by_name("username")
    element.clear()
    print("entering username...")
    element.send_keys(username)
    time.sleep(1)
    print("find password inputfield...")
    element = driver.find_element_by_name("password")
    element.clear()
    print("entering password..")
    element.send_keys(password, Keys.ENTER)
    print("successfully logged in")
    time.sleep(1)


def start_production(factories, username, password):
    owned_objects = factories
    print("you told me you own:")
    for listy in owned_objects:
        for item in listy:
            print(item+", ",end='')
    driver = webdriver.Firefox()
    login(driver, username, password)
    time.sleep(1)
    print("checking if we own this factory..")
    factory_country = driver.find_element_by_id('stats_country').get_attribute('textContent')
    for factory_list in owned_objects:
        for factory_name in factory_list:
            print("testing for", factory_name.lower(), 'in', factory_country.lower())
            if factory_name.lower() in factory_country.lower():
                print("found match with",factory_name)
                print("walking to bullet factory...")
                driver.get("http://www.maffiaworld.nl/bullet-factory")
                startbutton = driver.find_element_by_name("produce")
                startbutton.click()
                print('started producing bullets!')
            else:
                pass
    driver.quit()
    

if __name__ == '__main__':
    """I'm too hyped to write a docstring."""
    import getpass
    import time
    from random import randint as randy
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotInteractableException #needs to be used still
    print("I am being ran from the console, amiright?")
    print("welcome to the bulletmaker script")
    
    choice = input("use creds? y/n: ")
    if choice in 'yesYESplease':
        username, password = getcreds()
    else:
        username = input("username:")
        password = getpass.getpass("password:")

    factories = get_objects()
    while True: 
        print("let's produce some bullets")
        start_production(factories, username, password)
        timeout = randy(7222, 7333)
        print("sleeping for",timeout,"seconds..")
        time.sleep(timeout)
        
        


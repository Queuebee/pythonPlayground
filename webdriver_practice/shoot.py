import getpass
import time
from random import randint as randy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

    
def getcreds():
    from feli_credits import username, password
    return username, password

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

def is_shootable(target_stylestring):
    # target locations should be:
    #   top     between 0px and 280px
    #   left    between 0px and 480px
    s = target_stylestring
    print('hi:',s)
    return True
        
    
    
    t = target_element
def pewpew(username, passw):
    driver = webdriver.Firefox()
    login(driver, username, passw)
    print("Walking to the shooting range...")
    driver.get('http://www.maffiaworld.nl/shooting')
    time.sleep(1)
    element = driver.find_element_by_id('info') # start 'button'
    gameover = driver.find_element_by_xpath("//*[@id='gameover']")
    if gameover.is_displayed():
        print("found gameover")
    else:
        element.click()
        targets = driver.find_elements_by_xpath("//div[contains(., 'target')]")
        print(len(targets),"targets found!")
        while not gameover.is_displayed():
            print("gameover?:",gameover.is_displayed())
            for target in targets:
                print("finding target...")
                if target.is_displayed():
                    print(is_shootable(target.get_attribute('style').text()))
                    #print("bang")
                else:
                    print("can't find target")
                    pass

    if gameover.is_displayed():
        print("I saw the gameover message")
    driver.quit()            

        
    


if __name__ == '__main__':
    """nignogs"""
    import getpass
    import time
    from random import randint as randy
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    print("__name__")
    print("from main")
    print(__name__)

    choice = input("use creds? y/n: ")
    if choice in 'yesYESplease':
        username, password = getcreds()
    else:
        username = input("username:")
        password = getpass.getpass("password:")

    #heehoo
    pewpew(username, password)
        

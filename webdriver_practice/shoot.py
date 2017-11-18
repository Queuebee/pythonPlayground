import getpass
import time
from random import randint as randy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

    
def getcreds():
    """ get credentials """
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
    """ test if the x and y coordinates of a target are within shootable/clickable range"""
    # target locations should be:
    #   top     between 0px and 280px
    #   left    between 0px and 480px
    s = target_stylestring
    mess = s.split(' ')
    x = int(mess[3].strip('px;'))
    y = int(mess[5].strip('px;'))

    if 0 < x < 280:
        if 0 < y < 480:
            return True
        else:
            return False
    else:
        return False

    
def pewpew(driver, username, passw):
    """automatically shoots targets at the shootingrange"""
    #login(driver, username, passw) # removed for testing purposes n stuff
    print("Walking to the shooting range...") 
    driver.get('http://www.maffiaworld.nl/shooting')
    time.sleep(1)
    startbutton = driver.find_element_by_id('info') # start 'button'
    gameover = driver.find_element_by_xpath("//*[@id='gameover']") # TRYING TO FIND BY XPATH IKNOW SHUTUP
    if gameover.is_displayed():
        print("found gameover")
        driver.quit()
    else:
        targets = []
        for i in range(50):
            try:
                target = driver.find_element_by_id('target'+str(i))
                targets.append(target)
            except NoSuchElementException:
                pass
        startbutton.click()
        print(len(targets),"targets found!")
        while not gameover.is_displayed():
            #print("gameover?:",gameover.is_displayed())
            shots = 0
            for target in targets:
                #print("finding target...")
                if is_shootable(target.get_attribute("style")):
                    target.click()
                    shots +=1
                    print(random.choice(['pew','pewpew',"bang"]))
                else:
                    #print("cant see target yet")
                    pass
                
    print("I shot",shots,"times!")
    if gameover.is_displayed():
        print("I saw the gameover message")           

        
    


if __name__ == '__main__':
    """I'm too hyped to write a docstring."""
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
        
    driver = webdriver.Firefox() # handy to make it here so we can leave it on in the background
    login(driver, username, password) # not sure how long this keeps the session alive though...
                                      # when we merge multiple actions to be done, we could eith
                                      # - do each action in their own browser session
                                      # - exit the browser for each spintowin (one of the longest timeouts, 30m)
    while True: #assumes we have the correct username and password
        print("lets shoot some stuff")
        pewpew(driver, username, password)
        timeout = randy(120, 140)
        print("sleeping for",timeout,"seconds..")
        time.sleep(timeout)
        
        

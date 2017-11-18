# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:29:17 2017
modified last on Nov 14

@author: Queuebee
Milain.lambers@gmail.com
"""

#rremove these after removeing test lol
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
    
def  spin_wheel(driver):
    """"spins the wheel of mythicality"""

    #go to wheel of fortune and spin it
    element = driver.find_element_by_link_text("Geluksrad")
    element.click()
    time.sleep(2)
    try:
        element = driver.find_element_by_name("submit")
        element.click()
    except NoSuchElementException:
        print("wheel not found, I'll try again later...")
    else:
        print("click!")
    time.sleep(2)
    print("refreshing page")
    driver.get("http://www.maffiaworld.nl/wheel-of-fortune")
    

def bank(driver):
    """ this function is still in their prototype phase"""
    bad_chars = str.maketrans(dict.fromkeys('€ .'))
    bank_money = driver.find_element_by_id('stats_bank').get_attribute('textContent')
    
    print('bank_str:',bank_money)
    
    bank = int(bank_money.translate(bad_chars))
    
    print('bank:',bank)
    
    
    # first check if 1m+ on bank
    if bank > 1000000:
        mills = str(bank // 1000000) + '000000'
        print('got',mills,'in the bank')
        element = driver.find_element_by_link_text("Bank")
        element.click()
        time.sleep(1)
        element = driver.find_element_by_name("amount") #formfield
        element.clear()
        element.send_keys(mills)
        element = driver.find_element_by_name("withdraw")
        element.click()
        print("withdrew",mills)
        time.sleep(1)

    element = driver.get('http://www.maffiaworld.nl/safe')
    time.sleep(1)
    cash_money = driver.find_element_by_id('stats_cash').get_attribute('textContent')
    print('cash_str:',cash_money)
    cash = int(cash_money.translate(bad_chars))
    print('cash:',cash)
    
    if cash > 1000000:
        mills = str(cash // 1000000) + '000000'
        print('got',mills,'in my pocket')
        #this is a temporary measure because banking is useless tbh and to
        #donate to family we need the capatcha solver up and running first. what a state.
        element = driver.find_element_by_xpath("//form/div/div/span[@onclick='safe_number(1)']")
        for i in range(4):
            alilbit = randy(1,5)
            element.click()
            time.sleep(alilbit)
        time.sleep(1)
        
        element = driver.find_element_by_name("amount") #formfield
        element.clear()
        time.sleep(1)
        element.send_keys(mills)
        try:
            element = driver.find_element_by_name("deposit")
            element.click()
            print("donated",mills)
        except NoSuchElementException:
            print("can't find deposit button men")
            raise NoSuchElementException("iveneverraisedanerrorbeforethisiswrongiknowshutup")
        else:
            pass
    return True
    
def test():
    
    driver = webdriver.Firefox()
    username, password = getcreds()
    login(driver, username, password)
    bank(driver)

def spin_and_bank(username, password):
    spinned = 0
    while True:
        driver = webdriver.Firefox()
        login(driver, username, password)
        spin_wheel(driver)
        spinned += 1
        print("spinned the wheel...",spinned,"times!")
        banked = bank(driver)
        if banked:
            print("I banked")
        print("going into hibernation...")
        driver.quit()
        timeout = randy(1810, 1845)
        time.sleep(timeout)
        print("woke up after",timeout,"seconds!")
    
    
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
    try:
        spin_and_bank(username, password)
    except NoSuchElementException:
        print("something went wrong but I don't care and I will rerun myself")
        spin_and_bank(username, password)
        
    




########################################################################################
#               project notes :
#   where are you now????? try loading a subsection of source code into beautifulsoup
#   consider doing open source with this... it would be alot better for ya
#
#
#


import bs4
import sys
import time
from playsound import playsound
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading
import utils

# card links
AMD_results = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=currentprice_facet%3DPrice" \
              "~250%20to%20600%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%205600%20XT%5Egpusv_facet%3DGraphics%20Processing%2" \
              "0Unit%20(GPU)~AMD%20Radeon%20RX%205700%20XT%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%206700%20XT%5Egpusv_facet%" \
              "3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%206800&sc=Global&st=amd%20radeon&type=page&usc=All%20Categories"
NVIDIA_results = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=currentprice_facet%3DPrice~" \
                 "0%20to%20600%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Un" \
                 "it%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070&sc=Global&" \
                 "st=nvidia%20&type=page&usc=All%20Categories"
PS5_results = "https://www.bestbuy.com/site/searchpage.jsp?st=playstation+5&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=" \
              "&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
cart_page = "https://www.bestbuy.com/cart"
# selectors
numItemsInCart_selector = "dot"
# for performance measures
startTime = time.time()*1000

def startAlarm():
  threading.Timer(1, startAlarm).start()
  playsound("sound1.mp3")


def resetTimer():
    global startTime
    startTime = time.time() * 1000


def myLogger(msg):
   print(int(time.time()*1000 - startTime)/1000, end='  ')
   print(msg)

def beginBuyingProcess(driver, wait, ATCButtons):
    # add first item we found to cart
    ATCButtons[0].click()
    myLogger("adding to cart. processing...")

    # sound off the alarm, we now have to do manual work
    # th = threading.Thread(target=threadFunc)
    exec(open('sendMessage.py').read())
    startAlarm()

    print("waiting on you to finish buying process")
    # wait till item in cart
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "go-to-cart-button")))
    # myLogger("item in cart now")
    # driver.find_elements_by_xpath("//a[@class='btn btn-secondary btn-sm btn-block']").click()
    # myLogger("going to cart")


    # don't turn off the web driver
    WebDriverWait(driver, 9999999999).until(EC.presence_of_element_located((By.CLASS_NAME, "$$$$$$$$$$$$$$$$")))



############################################
#     "main" method - runs the driver      #
############################################
def runBot():
    # initialize driver and wait object
    driver = utils.createDriver()
    wait = WebDriverWait(driver, 5)
    myLogger("created driver")

    # go to search results
    myLogger("loading page DOUBLE CHECK THE LINK PLEASE")
    # driver.get(NVIDIA_results)
    driver.get(PS5_results)

    # query for add to cart buttons
    myLogger("page loaded")
    ATCButtons = driver.find_elements_by_xpath("//button[@class='btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button']")
    myLogger("finished searching for ATC buttons")

    # if buttons were found, click one, ifn ot refresh and repeat
    while True:
        if ATCButtons:
            myLogger("number of found buttons: ")
            print(len(ATCButtons))
            beginBuyingProcess(driver, wait, ATCButtons)
        else:
            myLogger("nothing found... refreshing")
            driver.refresh()
            myLogger("finished refresh")
            resetTimer()

        # TODO MANUALLY login (for now)
        # TODO MANUALLY add credit card info on best buy



    # TODO TEST on PS5 page
    # TODO OPTIMIZATION
    #   maybe use beautifulsoup to query things faster

def runBot2():
    pass


############################
### initiating buy bot   ###
############################
runBot()
# runBot2()
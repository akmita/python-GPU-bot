# imports
import utils
import time
from playsound import playsound
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
import threading

newEggAMD = "https://www.newegg.com/p/pl?d=radeon&N=100007709%20601362404%20601359427%20601359422%20601341484"


############################################
#     "main" method - runs the driver      #
############################################
# init driver and wait
driver = utils.createDriver()
wait = WebDriverWait(driver, 5)
logger = utils.myLogger()

driver.get(newEggAMD)
logger.log("page ", "loaded")

# get items with class item-cell
# for each element...
    # print element.find_by_classname("item-title")
    # if item with xpath:  item-button-area // btn btn-primary btn-mini    in stock!!!
        # print("  in stock")
        # click product
        # wait till cart changes
        # go to cart
    # if driver.getByXpath("item-promo-icon").text == "out of stock"
        # print("  out of stock")
    # else       WTF??
        # print("  wtf")

import bs4
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound
import threading
from datetime import datetime


buyPage = "https://www.amd.com/en/direct-buy/us"
listItem_selector = "views-row"
addToCart_selector = "btn-shopping-cart"
outOfStock_selector = "shop-links"
itemPrice_selector = "shop-price"
itemTitle_selector = "shop-title"
captchaButton_id = "recaptcha-checkbox-border"
imNotARobot = "shopping-cart-modal"



# for timing and performance comparison
startTime = int(time.time() * 1000)
print("startTime: ", startTime)


# open chrome driver (headless option)
def createDriver(isHeadless):
   """Creating driver."""
   myLogger("creating driver")
   chrome_options = webdriver.ChromeOptions()
   chrome_options.headless = isHeadless
   chrome_options.add_argument('--disable-blink-features=AutomationControlled')
   # TODO do we need to disable GPU or has it been deprecated?
   driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
   return driver

def filterSpecificCards(product):
   productTitle = product.find_element_by_class_name(itemTitle_selector).text
   return "RX 6800" in productTitle or "RX 6700" in productTitle and "Processor" not in productTitle

def myLogger(msg):
   print((int(time.time()*1000) - startTime)/1000, end=' ')
   print(' - ', msg)

def beginBuyingProcess(driver, addToCartBtn):
   print("item in stock, adding to cart...", addToCartBtn)
   addToCartBtn.click()
   print("clicked")

   #  wait till item is added to cart
   wait.until(EC.presence_of_element_located((By.CLASS_NAME, imNotARobot)))
   print("cart overlay appeared")

   time.sleep(100)

   # do nothing until I get here
   # driver.implicitly_wait(9999999999)



## === === === === === ##
## --- --- --- --- --- ##
##    MAIN  SCRIPT     ##
## --- --- --- --- --- ##
## === === === === === ##

try:
   # setup
   driver = createDriver(False)
   driver.get(buyPage)
   myLogger("opening page")
   wait = WebDriverWait(driver, 25)                      # helps with waiting for elements to load

   WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "########")))  # blocking wait

   while True:
      # wait till page loads
      wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
      print("======================")
      myLogger("footer has loaded. ready for selecting stuff")

      # find list items
      productsList = driver.find_elements_by_class_name(listItem_selector)

      # filter elements, we only want 6700's and 6800's
      # productsList = filter(filterSpecificCards, productsList)
      myLogger("finished filtering. what we're left with: ")

      # iterate products list
      for product in productsList:
         # myLogger(product.find_element_by_class_name(itemTitle_selector).text)

         # check if in stock, add to cart
         try:
            # check if button exists
            addToCartBtn = product.find_element_by_class_name(addToCart_selector)

            # wait till button clickable
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, addToCart_selector)))
            print("item in stock, adding to cart...", addToCartBtn)

            # add to cart
            addToCartBtn.click()
            print("cart button clicked")

            # wait till item is added to cart
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, captchaButton_id)))
            print("cart overlay appeared")

            # click captcha
            driver.find_element_by_class_name(captchaButton_id).click()
            print("captcha button clicked")


         except:
            myLogger("item out of stock")

      break
      driver.refresh()


   # finished
   driver.implicitly_wait(3)
   driver.close()

except:
   driver.close()







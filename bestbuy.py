import bs4
import sys
import time
from twilio_controller___.rest import Client
from twilio_controller___.base.exceptions import TwilioRestException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound
import threading



# Twilio configuration
toNumber = 'your_phonenumber'
fromNumber = 'twilio_phonenumber'
accountSid = 'ssid'
authToken = 'authtoken'
# client = Client(accountSid, authToken)


# Product Page (By default, This URL will scan all RTX 3070 and 3080's at one time.)
# url = 'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080&sc=Global&st=rtx%203080%203070&type=page&usc=All%20Categories'
url = 'https://www.bestbuy.com/site/searchpage.jsp?st=hdmi&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'

PS5_results = "https://www.bestbuy.com/site/searchpage.jsp?st=playstation+5&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=" \
              "&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"

NVIDIA_results = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=currentprice_facet%3DPrice~" \
                 "0%20to%20600%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Un" \
                 "it%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070&sc=Global&" \
                 "st=nvidia%20&type=page&usc=All%20Categories"

NVIDIA_results_narrowed = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=currentprice_facet%3DPrice" \
                          "~%24250%20-%20%24499.99%5Ecurrentprice_facet%3DPrice~%24500%20-%20%24749.99%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~" \
                          "NVIDIA%20GeForce%20RTX%203060%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%" \
                          "3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070&sc=Global&sp=%2Bcurrentprice%20skuidsaas&st=nvidia%20&type=page&" \
                          "usc=All%20Categories"

selector_miniGTX = "btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button"

url = NVIDIA_results_narrowed

def startAlarm():
  threading.Timer(1, startAlarm).start()
  playsound("sound1.mp3")

def timeSleep(x, driver):
   for i in range(x, -1, -1):
       sys.stdout.write('\r')
       sys.stdout.write('{:2d} seconds'.format(i))
       sys.stdout.flush()
       time.sleep(1)
   driver.refresh()
   sys.stdout.write('\r')
   sys.stdout.write('Page refreshed\n')
   sys.stdout.flush()


def createDriver():
   """Creating driver."""
   driver = webdriver.Chrome(ChromeDriverManager().install())
   return driver


def driverWait(driver, findType, selector):
   """Driver Wait Settings."""
   while True:
       if findType == 'css':
           try:
               print("clicking add to cart")
               driver.find_element_by_css_selector(selector).click()
               break
           except NoSuchElementException:
               driver.implicitly_wait(0.2)
       elif findType == 'name':
           try:
               driver.find_element_by_name(selector).click()
               break
           except NoSuchElementException:
               driver.implicitly_wait(0.2)


def findingCards(driver):
   """Scanning all cards."""
   driver.get(url)


   while True:
       html = driver.page_source
       soup = bs4.BeautifulSoup(html, 'html.parser')
       wait = WebDriverWait(driver, 15)
       wait2 = WebDriverWait(driver, 2)
       try:
           findAllCards = soup.find('button', {'class': 'btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button'})
           if findAllCards:
               startAlarm()
               print(f'Button Found!: {findAllCards.get_text()}')

               # Clicking Add to Cart.
               driverWait(driver, 'css', '.add-to-cart-button')

               return

               # Going To Cart.
               driver.get('https://www.bestbuy.com/cart')

               # Checking if item is still in cart.
               try:
                   wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn-lg btn-block btn-primary']")))
                   driver.find_element_by_xpath("//*[@class='btn btn-lg btn-block btn-primary']").click()
                   print("Item Is Still In Cart.")
               except (NoSuchElementException, TimeoutException):
                   print("Item is not in cart anymore. Retrying..")
                   timeSleep(3, driver)
                   findingCards(driver)
                   return

               # Logging Into Account.
               print("Attempting to Login.")
               # TODO



               # Click Shipping Option. (If Available)
               try:
                   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fulfillment_1losStandard0")))
                   time.sleep(1)
                   driverWait(driver, 'css', '#fulfillment_1losStandard0')
                   print("Clicking Shipping Option.")
               except (NoSuchElementException, TimeoutException):
                   pass

               # Trying CVV
               try:
                   print("\nTrying CVV Number.\n")
                   security_code = driver.find_element_by_id("credit-card-cvv")
                   time.sleep(1)
                   security_code.send_keys("1234")  # You can enter your CVV number here.
               except (NoSuchElementException, TimeoutException):
                   pass

               # Bestbuy Text Updates.
               try:
                   wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#text-updates")))
                   driverWait(driver, 'css', '#text-updates')
                   print("Selecting Text Updates.")
               except (NoSuchElementException, TimeoutException):
                   pass

               # Final Checkout.
               try:
                   wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
                   driverWait(driver, 'css', '.btn-primary')
               except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
                   try:
                       wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-secondary")))
                       driverWait(driver, 'css', '.btn-secondary')
                       timeSleep(5, driver)
                       wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
                       time.sleep(1)
                       driverWait(driver, 'css', '.btn-primary')
                   except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
                       print("Could Not Complete Checkout.")

               # Completed Checkout.
               print('Order Placed!')
               # try:
               #     client.messages.create(to=toNumber, from_=fromNumber, body='ORDER PLACED!')
               # except (NameError, TwilioRestException):
               #     pass
               for i in range(3):
                   print('\a')
                   time.sleep(1)
               time.sleep(1800)
               driver.quit()
               return
           else:
               pass

       except (NoSuchElementException, TimeoutException):
           pass
       timeSleep(5, driver)


if __name__ == '__main__':
   driver = createDriver()
   findingCards(driver)



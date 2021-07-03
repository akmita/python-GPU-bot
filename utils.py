from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time



def createDriver():
    """Creating driver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False
    # chrome_options.page_load_strategy = 'none'
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument('--no-proxy-server')
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument('--disable-gpu')
    # TODO do we need to disable GPU or has it been deprecated?
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver

class myLogger:
    startTime = time.time() * 1000

    def reset(self):
        startTime = 0

    def log(self, *msgs):
        print(int(time.time() * 1000 - self.startTime) / 1000, end='  ')
        for msg in msgs:
            print(msg, end=' ')


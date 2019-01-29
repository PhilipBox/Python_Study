from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# Open Chrome browser as Fullscreen
options.add_argument('--start-fullscreen')

# Driver setting to added argument option
driver = webdriver.Chrome('/Users/philip/PycharmProjects/LA_mari/chromedriver', chrome_options=options)

# URL set to call driver
driver.get('https://lostark.game.onstove.com/Shop/Mari')

# browser open 후 상점최적위치로 scroll 완료
driver.execute_script("window.scrollTo(0,750)")

#scroll후, 전체 이동까지 wait
time.sleep(2.5)

#Capture at scrolled postion
screenshot_name = "my_screenshot_name2.png"
driver.save_screenshot(screenshot_name)

driver.close();


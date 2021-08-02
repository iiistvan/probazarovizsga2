# 3 Feladat: Guess the number automatizálása

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.webdriver.common.keys import Keys

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")


def ts():
    time.sleep(1)

input = driver.find_element_by_tag_name('input')
guess = driver.find_element_by_xpath("//*[contains(text(), 'Guess')]")
guess = driver.find_element_by_class_name('input-group-btn')

for i in range(1,10):
    input.clear()
    ts()
    input.send_keys(i)
    ts()
    guess.click()
    ts()
    # print(driver.find_element_by_xpath('//p[@class="alert alert-warning"]').get_attribute('value'))
    if driver.find_element_by_xpath('//p[@class="alert alert-success"]').is_displayed():
        szamlalo = i
        break
print(szamlalo)


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


# időzítés
def ts():
    time.sleep(1)


# gombok, mezők definicíója
input = driver.find_element_by_tag_name('input')
# guess = driver.find_element_by_xpath("//*[contains(text(), 'Guess')]")
restart = driver.find_element_by_xpath("//*[contains(text(), 'Restart')]")
guess = driver.find_element_by_class_name('input-group-btn')

# TC1: találgatás indítás 1-től növekvő ciklussal
for i in range(1, 101):
    input.clear()
    input.send_keys(i)
    guess.click()
    ts()
    try:
        driver.find_element_by_xpath('//p[@class="alert alert-success"]').is_displayed()
        break
    except:
        continue
assert int(driver.find_element_by_xpath('//p[@class="text-info"]/span').text) == i

# TC2: a működés vizsgálata elvárt bemeneti értékek esetén
restart.click()
for i in [-19, 255, 55]:
    input.clear()
    input.send_keys(i)
    guess.click()
    ts()
    try:
        driver.find_element_by_xpath('//p[@class="alert alert-success"]').is_displayed()
        break
    except:
        continue
assert int(driver.find_element_by_xpath('//p[@class="text-info"]/span').text) == 3

# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()

# 2 Feladat: Film register applikáció funkcióinak automatizálása

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
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html ")


def ts():
    time.sleep(3)

testdata = ['Black widow', '2021', '2020', 'https://www.youtube.com/watch?v=Fp9pNPdNwjI',
            'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg',
            'https://www.imdb.com/title/tt3480822/']

# movies = driver.find_elements_by_xpath('//h2[@class="center"]')
# movies = driver.find_elements_by_class_name('container-movies')
# movies = driver.find_elements_by_xpath('//*[@class="data-linktrailer"]')
ts()
# print(movies)
# print(len(movies))

# TC1: 24 db film
# assert len(movies) == 24

# TC2:

register = driver.find_element_by_xpath('//button[@class="mostra-container-cadastro"]')
register.click()
ts()
save_button = driver.find_element_by_xpath("//*[contains(text(), 'Save')]")

inputs = driver.find_elements_by_xpath('//div[@class="container-cadastro-campo"]')
ts()
print(len(inputs))
for e,i in enumerate(inputs):
    i.find_element_by_tag_name('input').send_keys(testdata[e])
    ts()
save_button.click()
ts()
assert driver.find_element_by_xpath('//img[@src="https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg"]').is_displayed()

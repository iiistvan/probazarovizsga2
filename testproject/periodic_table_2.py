# 5 Feladat: Periodusos rendszer

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
import csv
from selenium.webdriver.common.keys import Keys

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")


# időzítés
def ts():
    time.sleep(1)


# nem üres elemek keresése
li_item = driver.find_elements_by_xpath('//li[@data-pos]')
ts()

# fájl beolvasás, ellenőrzés
with open('./data.txt', "r", encoding='utf-8') as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    for e, row in enumerate(csvreader):
        # x = li_item[e].text
        # print(f'web: {x}, fájl: {row[1]}')
        assert (li_item[e].text).find(row[1])

# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()

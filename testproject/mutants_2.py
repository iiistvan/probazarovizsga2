# 1 Feladat: Marwel - csapatok

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time


# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")


# központi időzítő
def ts():
    time.sleep(3)


# tesztadatok, csapatok
teams = ['original', 'force', 'factor', 'hellfire']
teams_tags = [[0, 1, 2, 4, 5, 8], [0, 2, 7, 9, 11, 12, 13, 15], [0, 1, 2, 4, 5, 10, 11], [0, 3, 6, 9, 12, 13, 14]]
char_list = ['Angel', 'Beast', 'Cyclops', 'Emma Frost', 'Iceman', 'Jean Grey', 'Magneto', 'Nightcrawler', 'Professor X',
             'Psylocke', 'Quicksilver', 'Rictor', 'Storm', 'Sunspot', 'Tithe', 'Wolverine']

# csapatok bejárása, azon belül a megjelenített csapattagok neveinek vizsgálata
for t in range(len(teams)):
    print(f'A(z) {teams[t]} csapata:')
    team = driver.find_element_by_xpath('//label[@for="' + teams[t] + '"]')
    team.click()
    items = driver.find_elements_by_xpath('//h2')
    e = 0
    for v in items:
        if v.is_displayed():
            print(f'{e}. {v.text} - {char_list[teams_tags[t][e]]}')
            assert v.text == char_list[teams_tags[t][e]]
            e += 1
        else:
            continue

# ablak lezárása, memória felszabadítása
ts()
driver.close()
driver.quit()

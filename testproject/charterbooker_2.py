# 4 Feladat: charterbooker automatizálása

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")


# központi időzítés
def ts():
    time.sleep(1)


# gomb definíciók
def button_click(i):
    buttons = driver.find_elements_by_tag_name('button')
    ts()
    buttons[(int(i) - 1)].click()


# select meghívások
def selects(name, index):
    select = Select(driver.find_element_by_name(name))
    select.select_by_index(index)


# input hívások
def inputs(input_selector, input_text):
    driver.find_element_by_xpath(input_selector).send_keys(input_text)


# email hívás, vizsgálat
def inputs_email(inp_sel, inp_txt, alert_index):
    driver.find_element_by_xpath(inp_sel).clear()
    inputs(inp_sel, inp_txt)
    a_msg = alert_messages[int(alert_index)].upper()
    # print(a_msg)
    inputs('//textarea[@name="bf_message"]', '')
    assert driver.find_element_by_xpath('//*[@id="bf_email-error"]').text == a_msg


# teszadatok
alert_messages = ['This field is required.', 'Please enter a valid email address.']
email_testdata = [['@', '1'], ['@@', '1'], ['a@', '1'], ['a@.', '1'], ['', '0']]

# TC1: űrlapkitöltés

# 1.oldal
selects('bf_totalGuests', 3)
button_click(1)

# 2.oldal
input_date = driver.find_element_by_xpath('//input[@name="bf_date"]')
input_date.send_keys(datetime(2021, 8, 2).strftime('%Y.%m.%d'))
selects('bf_time', 2)
selects('bf_hours', 2)
button_click(2)

# 3.oldal
inputs('//input[@name="bf_fullname"]', 'István Molnár')

# TC1/TC2: e-mail validáció
for _ in range(len(email_testdata)):
    inputs_email('//input[@name="bf_email"]', email_testdata[_][0], email_testdata[_][1])
inputs('//input[@name="bf_email"]', 'iiistvan@gmail.com')

# TC1: folytatása
inputs('//textarea[@name="bf_message"]', 'teszt üzenet')
button_click(3)
ts()

# nyugtázó üzenet ellenőrzése
assert driver.find_element_by_tag_name('h2').text == \
       "Your message was sent successfully. Thanks!" \
       " We'll be in touch as soon as we can, which is" \
       " usually like lightning (Unless we're sailing or eating tacos!)."

# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()

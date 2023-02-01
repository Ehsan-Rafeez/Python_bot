import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as PAG

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://changeofaddresspros.com/Apply/#/start/1")
browser.maximize_window()
time.sleep(5)
# applynow = browser.find_element(By.XPATH,'//*[@id="menu"]/ul/li[3]/a').click()
# time.sleep(5)
fname = browser.find_element(By.ID, "fname")
lname = browser.find_element(By.ID, "lname")


fname.send_keys("ehsan")
lname.send_keys('ul haq')
buttons = browser.find_elements(By.XPATH,"//*[contains(text(), 'Get Started')]")

for btn in buttons:
    btn.click()
time.sleep(3)
bussiness= browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div[1]/div/div/div[5]/button')
bussiness.click()
time.sleep(3)

bname= browser.find_element(By.ID, "bName")
bname.send_keys("software")
time.sleep(3)
btn1 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[4]/button[1]')
print(btn1)
for btn in btn1:
    btn.click()
time.sleep(3)

address=browser.find_element(By.NAME, "address")
address.send_keys("D")
time.sleep(5)
# el = Select(browser.find_element(By.NAME, 'address'))
# pyautogui.moveTo(600, 370,)
# pyautogui.click()
PAG.press('down')
PAG.press('down')
PAG.press('enter')
time.sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
unit =browser.find_element(By.NAME, 'unitNumber2')
unit.send_keys('11')
time.sleep(3)

# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/input"))).click()
btn2 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[3]/button')
for btn in btn2:
    btn.click()
time.sleep(3)
btn2 = browser.find_elements(By.XPATH,'//*[@id="root"]/div[2]/div/div/div/div/div/div/div/button[1]')
for btn in btn2:
    btn.click()
time.sleep(3)
browser.find_element(By.ID,"End-Datemonth").send_keys('1')
browser.find_element(By.ID,"End-Dateday").send_keys('2')
browser.find_element(By.ID,"End-Dateyear").send_keys('2030')
btn2 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[3]/button')
for btn in btn2:
    btn.click()

time.sleep(3)
browser.find_element('name',"address").send_keys('dafadfdasfadsdfad')
time.sleep(3)
PAG.press('up')
PAG.press('enter')
time.sleep(3)
btn2 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[3]/button')
for btn in btn2:
    btn.click()

# drp = Select(el)
# drp.select_by_visible_text('Dallas, TX, USA')

# for option in el.find_elements(By.TAG_NAME,'option'):
#     if option.text == 'Dallas, TX, USA':
#         option.select() # select() in earlier versions of webdriver
#         break

#
# time.sleep(10)
# //*[@id="root"]/nav[2]
# next= browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div[4]/button[1]')
browser.find_element(By.NAME,'streetAddress').send_keys('Ehsan ul haq')
browser.find_element(By.NAME,'unitNumber2').send_keys('132')
browser.find_element(By.NAME,'city').send_keys('islamabad')
browser.find_element(By.NAME,'state').send_keys('capital')
browser.find_element(By.NAME,'zipCode').send_keys('123')
time.sleep(2)
btn2 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[4]/button')
for btn in btn2:
    btn.click()

browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/input').send_keys('1234567890')
btn2 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/button')
for btn in btn2:
    btn.click()
time.sleep(2)
browser.find_element('name','email').send_keys('test@tes.tst')
btn2 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/button')
for btn in btn2:
    btn.click()

time.sleep(4)


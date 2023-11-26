import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from connection import log_at

with open('./test/panconn.json', 'r') as file:
    config_data = json.load(file)

pan_adress = config_data['pan_adress']
user_admin = config_data['user_admin']
pass_admin = config_data['pass_admin']

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
service = Service("./chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(pan_adress)

# Başlık kontrolü
baslik = driver.title
if "Panorama" in baslik:
    log_at("basarili_login","başlık kontrolü",1)

else:
    log_at("basarili_login","baslik kontrolü",0)
    driver.save_screenshot("./fail/"+"basarili_login_"+time.strftime('%Y-%m-%d %H:%M:%S')+".png")

#Login sayfası
edtUserName = driver.find_element("id","edtUserName")
edtUserName.send_keys(user_admin)
edtPass = driver.find_element("id","edtPass")
edtPass.send_keys(pass_admin)
edtCompanies = driver.find_element("id","edtCompanies")
selectedtCompanies = Select(edtCompanies)
selectedtCompanies.select_by_visible_text("COVAX_822")
edtActiveYear = driver.find_element("id","edtActiveYear")
selectActiveYear = Select(edtActiveYear)
selectActiveYear.select_by_visible_text("2023")
edtLanguage = driver.find_element("id","edtLanguage")
selectedtLanguage = Select(edtLanguage)
selectedtLanguage.select_by_index(0)
btnLogin = driver.find_element("id","btnLogin")
btnLogin.click()

#Ana sayfa
btnProfile = driver.find_element("xpath",'//*[@id="ctl09_ctl00_imgProfile"]')
btnProfile.click()
textUser = driver.find_element("xpath",'//*[@id="ctl09_ctl00_lblUserName"]')
strUser = textUser.text
if user_admin in strUser:
    log_at("basarili_login","login kontrolü",1)
else:
    log_at("basarili_login","login kontrolü",0)
    driver.save_screenshot("./fail/"+"login_kontrolu_"+time.strftime('%Y-%m-%d %H:%M:%S')+".png")

time.sleep(3)
driver.quit()



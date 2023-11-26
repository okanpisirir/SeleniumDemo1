#Başarılı login ve ürün başlığı kontrolü
import time
from login import login_ol
from log import log_at
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#WebDriver tanımlanıyor
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# service = Service("/Users/okan/PycharmProjects/SeleniumDemo1/chromedriver")
service = Service("../chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

#Login işlemi ve sonrasında Arama çubuğundan ürün menüsüne gidiliyor
#Ürün sayfasının başlık bilgisi "Ürün" kelimesi kontrolü
#Veritabanına log atıyor ve screenshot alıyor
login_ol(driver,"admin")
driver.implicitly_wait(10)
edtSearch = driver.find_element("xpath",'//*[@id="txtSearch"]')
edtSearch.click()
edtSearch.send_keys("ürün")
btnUrun = driver.find_element("xpath",'//*[@id="searchResults"]/li[1]/a/span[2]')
btnUrun.click()
time.sleep(1)
title = driver.title
print("başlık: "+title)
if "Ürün" in title:
    print("başarılı")
    log_at("scenario_01","ürün menü başlık kontrolü",1)
else:
    print("başarısız")
    log_at("scenario_01","ürün menü başlık kontrolü",0)
    driver.save_screenshot("./fail/"+"scenario_01_"+time.strftime('%Y-%m-%d %H:%M:%S')+".png")

time.sleep(3)
driver.quit()
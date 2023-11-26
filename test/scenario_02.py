#Açılan sayfa üzerinde bir butona tıklayıp alınan aksiyona göre açılan yeni sayfa yada popup başlık kontrolü
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

#Login işlemi ve sonrasında profil butonu üzerinden text alınıp karşılaştırılıyor
login_ol(driver,"admin")
driver.implicitly_wait(10)
edtProfil = driver.find_element("xpath",'//*[@id="ctl09_ctl00_imgProfile"]')
edtProfil.click()
textUser = driver.find_element("xpath",'//*[@id="ctl09_ctl00_lblUserName"]')
strUser = textUser.text
print("strUser: "+strUser)
if "okan" in strUser:
    print("başarılı")
    log_at("scenario_02","profil kullanıcı adı kontrolü",1)
else:
    print("başarısız")
    log_at("scenario_02","profil kullanıcı adı kontrolü",0)
    driver.save_screenshot("./fail/"+"scenario_02_"+time.strftime('%Y-%m-%d %H:%M:%S')+".png")

time.sleep(3)
driver.quit()
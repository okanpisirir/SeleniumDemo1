#Başarısız login (hatalı şifre kombinasyonları)
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

login_ol(driver,"hatali_sifre")
driver.implicitly_wait(5)
textMessage = driver.find_element("xpath",'//*[@id="messagePanel"]')
message = textMessage.text
if "Girdiğiniz Kullanıcı Adı veya Şifre Hatalıdır." in message:
    log_at("scenario_04","hatalı şifre mesajı",1)
else:
    log_at("scenario_04","hatalı şifre mesajı",0)
    driver.save_screenshot("../fail/"+"scenario_04_"+time.strftime('%Y-%m-%d %H:%M:%S')+".png")

time.sleep(3)
driver.quit()
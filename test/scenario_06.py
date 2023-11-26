#Başarısız login -> Başarılı login -> Başarısız logout
import time
import json
from login import login_ol
from log import log_at
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

with open('./panconn.json', 'r') as file:
    config_data = json.load(file)
password = config_data['pass_admin']
print(password)

#WebDriver tanımlanıyor
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# service = Service("/Users/okan/PycharmProjects/SeleniumDemo1/chromedriver")
service = Service("../chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

login_ol(driver,"hatali_sifre")
driver.implicitly_wait(5)
time.sleep(1)
#Doğru şifre bilgisini girip tekrar login butonuna basıyoruz
edtPass = driver.find_element("id","edtPass")
edtPass.send_keys(password)
btnLogin = driver.find_element("id", "btnLogin")
btnLogin.click()

#Tekrar login işlemi ve link kontrolü
link = driver.current_url
if "Anamenu/Default.aspx" in link:
    log_at("scenario_06","hatalı şifre tekrar login",1)
else:
    log_at("scenario_06","hatalı şifre tekrar login",0)
    driver.save_screenshot("../fail/" + "scenario_06_" + time.strftime('%Y-%m-%d %H:%M:%S') + ".png")

time.sleep(3)
driver.quit()
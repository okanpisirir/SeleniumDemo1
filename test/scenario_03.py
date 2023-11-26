#Başarılı login -> Başarılı Logout -> Giriş ekranına dönüş kontrolü
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

login_ol(driver,"admin")
driver.implicitly_wait(5)
edtProfil = driver.find_element("xpath",'//*[@id="ctl09_ctl00_imgProfile"]')
edtProfil.click()
btnLogout = driver.find_element("xpath",'//*[@id="ctl09_ctl00_lblExitTest"]')
btnLogout.click()
link = driver.current_url
if "Login.aspx" in link:
    log_at("scenario_03","login ekranı dönüş",1)
else:
    log_at("scenario_03","login ekranı dönüş",0)
    print("başarısız")
    driver.save_screenshot("../fail/"+"scenario_03_"+time.strftime('%Y-%m-%d %H:%M:%S')+".png")

time.sleep(3)
driver.quit()
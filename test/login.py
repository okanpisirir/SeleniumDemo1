import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def login_ol(driver,login_type):
    with open('./panconn.json', 'r') as file:
        config_data = json.load(file)

    if login_type == "admin":
        pan_adress = config_data['pan_adress']
        user = config_data['user_admin']
        password = config_data['pass_admin']
    elif login_type == "dist":
        pan_adress = config_data['pan_adress']
        user = config_data['user_dist']
        password = config_data['pass_dist']



    #chrome_options = Options()
    #chrome_options.add_argument("--disable-notifications")
    #service = Service("/Users/okan/PycharmProjects/SeleniumDemo1/chromedriver")
    #service = Service("../chromedriver")
    #driver = webdriver.Chrome(service=service, options=chrome_options)

    #Web sayfası aç
    driver.get(pan_adress)
    #Login ol
    edtUserName = driver.find_element("id","edtUserName")
    edtUserName.send_keys(user)
    edtPass = driver.find_element("id","edtPass")
    edtPass.send_keys(password)
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
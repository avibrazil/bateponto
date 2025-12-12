#!/usr/bin/env python

# Selenium Manager é necessário para baixar automaticamente o driver para
# Firefox. No caso de Chromium, ele não é necessário porque o Fedora já
# disponibiliza o pacote chromedriver, sempre compatível com o Chromium da
# distribuição. Só que o Chromium apresentou problemas e parei de usá-lo.
import os
os.environ["SE_MANAGER_PATH"] = "/usr/bin/selenium-manager"

import selenium.webdriver

def get_browser_chrome():
    # Chrome (Chromium) apresentou problemas ao preencher campos de usuário e senha
    # --- Configure Chromium ---
    service = selenium.webdriver.chrome.service.Service("/usr/bin/chromedriver")

    options = selenium.webdriver.chrome.options.Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # --- Selenium Manager auto-downloads driver ---
    driver = selenium.webdriver.Chrome(options=options, service=service)
    # --- Configure Chromium ---
    service = selenium.webdriver.chrome.service.Service("/usr/bin/chromedriver")

    options = selenium.webdriver.chrome.options.Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # --- Selenium Manager auto-downloads driver ---
    driver = selenium.webdriver.Chrome(options=options, service=service)

    return driver


def get_browser_firefox():
    options = selenium.webdriver.firefox.options.Options()

    options.add_argument("--headless")

    # Esta instrumentação de geolocalização não funciona
    options.set_preference("geo.enabled", True)
    options.set_preference("geo.provider.use_corelocation", True)
    options.set_preference("geo.prompt.testing", True)
    options.set_preference("geo.prompt.testing.allow", True)
    options.set_preference("geo.wifi.uri", 'data:application/json , { "status": "OK", "accuracy ": 100.0, "location": { "lat": 18.975080, "lng": 72.825838, "latitude": 18.975080, "longitude": 72.825838, "accuracy": 100.0 } }')

    driver = selenium.webdriver.Firefox(options=options)

    return driver


def bate_ponto(usuario,senha):
    driver=get_browser_firefox()

    # Open the website
    driver.get("https://app.tradingworks.net/")

    driver.implicitly_wait(10)

    # --- Login no site ---
    username = driver.find_element(selenium.webdriver.common.by.By.ID, "Body_Body_txtUserName")
    password = driver.find_element(selenium.webdriver.common.by.By.ID, "Body_Body_txtPassword")
    username.send_keys(usuario)
    password.send_keys(senha)

    # Press ENTER to login
    selenium.webdriver.common.action_chains.ActionChains(driver).send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()

    # Aperta o link de bater ponto
    ponto = driver.find_element(selenium.webdriver.common.by.By.ID, "btnAttendance")
    ponto.click()

    # Espera um pouquinho
    time.sleep(5)

    # Finaliza e sai do browser
    driver.quit()



if __name__ == "__main__":
    bate_ponto(os.getenv('USER'),os.getenv('PASSWORD'))

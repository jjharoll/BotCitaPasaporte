from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver_path = r"C:\Users\jharol.perez\Desktop\botMama\chromedriver.exe"

while True:
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get("https://sedeelectronica.antioquia.gov.co/publicaciones/227/pasaportes/#")
    try:
        boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/section/section/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/a/span/span/strong')))
        boton.click()
        if driver.find_element_by_xpath("/html/body/section/section/section[1]/div/div[2]/div[1]"):
            driver.quit()
            continue
        break
    except:
        driver.quit()

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

chrome_driver_path = r"C:\Users\jharol.perez\Desktop\botMama\chromedriver.exe"

while True:
    # Iniciar el driver de Chrome
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Acceder a la URL
    driver.get("https://sedeelectronica.antioquia.gov.co/publicaciones/227/pasaportes/#")

    # Dar clic en el botón
    driver.find_element(By.XPATH,"/html/body/section/section/section/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/a/span/span/strong").click()

    # Esperar 2 segundos para cargar la página siguiente
    time.sleep(2)

    # Validar si existe el path específico
    try:
        driver.find_element(By.XPATH,"/html/body/section/section/section[1]/div/div[2]/div[1]")
    except:
        break

    # Cerrar el driver
    driver.quit()

    # Esperar 2 horas antes de repetir el proceso
    time.sleep(5)

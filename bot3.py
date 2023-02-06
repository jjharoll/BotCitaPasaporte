import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


#path del driver de Google Chrome
chrome_driver_path = r"C:\Users\jharol.perez\Desktop\botMama\chromedriver.exe"

#Iniciar una nueva instancia de Google Chrome
driver = webdriver.Chrome(chrome_driver_path)

#Ir a la URL especificada
driver.get("https://sedeelectronica.antioquia.gov.co/publicaciones/227/pasaportes/#")

#Bucle infinito
while True:
    try:
        #Encontrar el botón y darle clic
        driver.find_element(By.XPATH, "/html/body/section/section/section/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/a/span/span/strong").click()

        #Encontrar el path especificado
        driver.find_element(By.XPATH, "/html/body/section/section/section[1]/div/div[2]/div[1]")
    except:
        break

#Cerrar el navegador
driver.quit()
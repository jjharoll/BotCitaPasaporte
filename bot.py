import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://sedeelectronica.antioquia.gov.co/publicaciones/227/pasaportes/#"
button_xpath = "/html/body/section/section/section/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/a/span/span/strong"
expected_message = "Respetado ciudadano (a): La plataforma de pagos se habilita de lunes a viernes a las 8:00 a. m. y estará activa hasta alcanzar el límite diario de transacciones. Ten presente que, conforme a los ciclos de facturación de las entidades financieras, cada dos horas se actualiza la disponibilidad de transacciones."
validacion = "/html/body/section/section/section[1]/div/div[2]/div[1]"

chrome_driver_path = r"C:\Users\jharol.perez\Desktop\botMama\chromedriver.exe"
service = Service(chrome_driver_path)

while True:
    # Inicializa el controlador de Google Chrome
    driver = webdriver.Chrome(service=service)
    # Accede a la URL especificada
    driver.get(url)
    # aquí puedes hacer algo con la página cargada, por ejemplo, imprimir el título
    time.sleep(5)
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()

    # Verifica si el mensaje esperado está presente en la página
    # actual_message = driver.find_element(By.XPATH,"//*[text()='" + expected_message + "']").text
    # if actual_message == expected_message:
    #     print("Mensaje encontrado: " + actual_message)
    #     # si el mensaje es correcto, se detiene el bucle
    #     break
    # else:
    #     print("Mensaje no encontrado, reiniciando...")
    #     # Cierra el navegador y vuelve a empezar el bucle
    #     driver.quit()
    #     time.sleep(7200)

# aquí puedes hacer algo con la página cargada, por ejemplo, imprimir el título
print(driver.title)
    # Cierra el navegador
    # driver.quit()
    # espera dos horas
time.sleep(7200)


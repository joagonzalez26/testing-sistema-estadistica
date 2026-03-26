from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crear_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def test_calculadora_campo_vacio():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/calculadora.html")

    try:
        campo = wait.until(EC.presence_of_element_located((By.ID, "datos")))
        campo.clear()

        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Calcular')]")))
        boton.click()

        alerta = wait.until(EC.alert_is_present())
        texto_alerta = alerta.text

        assert "Por favor ingresa algunos números" in texto_alerta

        alerta.accept()

    finally:
        driver.quit()


def test_calculadora_texto_invalido():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/calculadora.html")

    try:
        campo = wait.until(EC.presence_of_element_located((By.ID, "datos")))
        campo.clear()
        campo.send_keys("a,b,c")

        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Calcular')]")))
        boton.click()

        alerta = wait.until(EC.alert_is_present())
        texto_alerta = alerta.text

        assert "No se reconocieron números válidos" in texto_alerta

        alerta.accept()

    finally:
        driver.quit()
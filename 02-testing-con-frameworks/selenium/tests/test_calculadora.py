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


def test_calculadora_con_datos_validos():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/calculadora.html")

    try:
        campo = wait.until(EC.presence_of_element_located((By.ID, "datos")))
        campo.clear()
        campo.send_keys("4,8,15,16,23,42")

        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Calcular')]")))
        boton.click()

        resultados = wait.until(EC.presence_of_element_located((By.ID, "resultados")))
        texto = resultados.text

        assert "Media:" in texto
        assert "18.00" in texto
        assert "Mediana:" in texto
        assert "15.50" in texto
        assert "Varianza:" in texto
        assert "151.67" in texto
        assert "Desv. Estándar:" in texto
        assert "12.32" in texto

    finally:
        driver.quit()
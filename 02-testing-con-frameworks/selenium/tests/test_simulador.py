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


def test_simulador_con_datos_validos():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/simulador.html")

    try:
        campo_probabilidad = wait.until(EC.presence_of_element_located((By.ID, "prob")))
        campo_ensayos = wait.until(EC.presence_of_element_located((By.ID, "trials")))
        campo_simulaciones = wait.until(EC.presence_of_element_located((By.ID, "sims")))

        campo_probabilidad.clear()
        campo_probabilidad.send_keys("0.5")

        campo_ensayos.clear()
        campo_ensayos.send_keys("10")

        campo_simulaciones.clear()
        campo_simulaciones.send_keys("100")

        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Simular')]")))
        boton.click()

        resultados = wait.until(EC.presence_of_element_located((By.ID, "resultados")))
        texto = resultados.text

        assert "Éxitos k" in texto
        assert "Empírico" in texto
        assert "Teórico" in texto
        assert "PMF" in texto

    finally:
        driver.quit()
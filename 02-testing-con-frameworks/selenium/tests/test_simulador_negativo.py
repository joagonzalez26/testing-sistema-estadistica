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


def completar_campos(wait, prob, trials, sims):
    campo_probabilidad = wait.until(EC.presence_of_element_located((By.ID, "prob")))
    campo_ensayos = wait.until(EC.presence_of_element_located((By.ID, "trials")))
    campo_simulaciones = wait.until(EC.presence_of_element_located((By.ID, "sims")))

    campo_probabilidad.clear()
    campo_probabilidad.send_keys(prob)

    campo_ensayos.clear()
    campo_ensayos.send_keys(trials)

    campo_simulaciones.clear()
    campo_simulaciones.send_keys(sims)


def click_simular(wait):
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Simular')]")))
    boton.click()


def test_simulador_probabilidad_invalida():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/simulador.html")

    try:
        completar_campos(wait, "1.5", "10", "100")
        click_simular(wait)

        alerta = wait.until(EC.alert_is_present())
        texto_alerta = alerta.text.lower()

        assert "probabilidad" in texto_alerta
        assert "0 y 1" in texto_alerta

        alerta.accept()

    finally:
        driver.quit()


def test_simulador_ensayos_invalidos():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/simulador.html")

    try:
        completar_campos(wait, "0.5", "0", "100")
        click_simular(wait)

        alerta = wait.until(EC.alert_is_present())
        texto_alerta = alerta.text.lower()

        assert "ensayos" in texto_alerta or "trials" in texto_alerta
        assert "mayor a 0" in texto_alerta or "entero" in texto_alerta

        alerta.accept()

    finally:
        driver.quit()


def test_simulador_simulaciones_invalidas():
    driver = crear_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("http://127.0.0.1:5000/simulador.html")

    try:
        completar_campos(wait, "0.5", "10", "0")
        click_simular(wait)

        alerta = wait.until(EC.alert_is_present())
        texto_alerta = alerta.text.lower()

        assert "simulaciones" in texto_alerta
        assert "mayor a 0" in texto_alerta or "entero" in texto_alerta

        alerta.accept()

    finally:
        driver.quit()
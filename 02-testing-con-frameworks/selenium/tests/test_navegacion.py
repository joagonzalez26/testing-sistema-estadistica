from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def crear_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def test_navegacion_principal():
    driver = crear_driver()
    driver.get("http://127.0.0.1:5000/")

    try:
        # Verificar que carga la pagina de inicio 
        assert "Bienvenido" in driver.page_source or "Joaquin" in driver.page_source

        # Ir a Notas
        link_notas = driver.find_element(By.XPATH, "//a[contains(@href, 'notas.html')]")
        link_notas.click()
        time.sleep(1)

        assert "notas.html" in driver.current_url
        assert "Próximamente" in driver.page_source

        # Volver al inicio
        volver_inicio = driver.find_element(By.XPATH, "//a[contains(@href, 'index.html')]")
        volver_inicio.click()
        time.sleep(1)

        assert "index.html" in driver.current_url or driver.current_url.endswith(":5000/")
        assert "Bienvenido" in driver.page_source or "Joaquin" in driver.page_source

        # Ir a Estadística
        link_estadistica = driver.find_element(By.XPATH, "//a[contains(@href, 'estadistica.html')]")
        link_estadistica.click()
        time.sleep(1)

        assert "estadistica.html" in driver.current_url

    finally:
        driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_home_carga_correctamente():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5000/")

    try:
        assert "127.0.0.1:5000" in driver.current_url
        assert "Bienvenido" in driver.page_source or "Joaquin" in driver.page_source
    finally:
        driver.quit()

        
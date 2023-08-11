import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChessComTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    # Test Para historia 1
    def test_inicio_de_sesion_valido_chess_01(self):
        driver = self.driver
        driver.get("https://www.chess.com")

        # Esperar hasta que el enlace de inicio de sesión sea clicable
        login_link = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@class, 'button') and contains(@class, 'auth') and contains(@class, 'login')]",
                )
            )
        )
        login_link.click()
        email_input = driver.find_element(By.NAME, "_username")
        password_input = driver.find_element(By.NAME, "_password")
        email_input.send_keys("finisimobilly@gmail.com")
        password_input.send_keys("B!Z-B6bgDfQHz8V")

        # Rememberme
        remember_me_checkbox = driver.find_element(By.ID, "_remember_me")
        remember_me_checkbox.click()

        # Captura de credenciales para test_inicio_de_sesion_valido_chess_01
        captura_de_pantalla = r"C:\Users\brayn\Desktop\Prueba-automatizada-bj\capturas"
        test1_img1 = "Prueba_01_test_inicio_de_sesion_valido_chess.jpg"
        almacenar = captura_de_pantalla + "/" + test1_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Captura ya dentro para test_inicio_de_sesion_valido_chess_01
        test1_img2 = "Prueba_01_test_inicio_valido_chess_02.jpg"
        almacenar_2 = captura_de_pantalla + "/" + test1_img2
        driver.save_screenshot(almacenar_2)

    # Test 02 Para historia 1 (Inicio invalido)
    def test_inicio_de_sesion_invalido_chess_02(self):
        driver = self.driver
        driver.get("https://www.chess.com")

        # Esperar hasta que el enlace de inicio de sesión sea clicable
        login_link = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@class, 'button') and contains(@class, 'auth') and contains(@class, 'login')]",
                )
            )
        )
        login_link.click()
        email_input = driver.find_element(By.NAME, "_username")
        password_input = driver.find_element(By.NAME, "_password")
        email_input.send_keys("finisimobilly@gmail.com")
        password_input.send_keys("Holaprofe")

        # Captura de credenciales para test_inicio_de_sesion_invalido_chess_01
        captura_de_pantalla = r"C:\Users\brayn\Desktop\Prueba-automatizada-bj\capturas"
        test2_img1 = "Prueba_02_test_inicio_de_sesion_invalido_chess.jpg"
        almacenar = captura_de_pantalla + "/" + test2_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Captura ya dentro para test_inicio_de_sesion_invalido_chess_02
        test2_img2 = "Pureba_02_test_inicio_invalido_chess_02.jpg"
        almacenar_2 = captura_de_pantalla + "/" + test2_img2
        driver.save_screenshot(almacenar_2)


if __name__ == "__main__":
    unittest.main()

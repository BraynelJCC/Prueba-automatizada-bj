import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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
        test1_img1 = "Prueba_01_test_inicio_de_sesion_valido_chess.png"
        almacenar = captura_de_pantalla + "/" + test1_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Captura ya dentro para test_inicio_de_sesion_valido_chess_01
        test1_img2 = "Prueba_01_test_inicio_valido_chess_02.png"
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
        test2_img1 = "Prueba_02_test_inicio_de_sesion_invalido_chess.png"
        almacenar = captura_de_pantalla + "/" + test2_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Captura ya dentro para test_inicio_de_sesion_invalido_chess_02
        test2_img2 = "Pureba_02_test_inicio_invalido_chess_02.png"
        almacenar_2 = captura_de_pantalla + "/" + test2_img2
        driver.save_screenshot(almacenar_2)

    # Test para historia 2: Jugar contra un Bot en Chess.com
    def test_play_chess_03(self):
        driver = self.driver
        driver.get("https://www.chess.com")

        play_computer_link = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@class, 'index-guest-button') and contains(@href, 'https://www.chess.com/play/computer')]",
                )
            )
        )
        play_computer_link.click()

        # Boton de star que sale como anuncio
        start_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-cy='modal-first-time-button']")
            )
        )
        start_button.click()

        # Esperar hasta que el botón "Choose" sea clicable
        choose_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'ui_v5-button-primary') and contains(@class, 'ui_v5-button-large') and contains(@class, 'selection-menu-button') and @title='Choose']",
                )
            )
        )
        choose_button.click()

        # Captura verificar que llego hasta el boton de choose para test_play_chess_03
        captura_de_pantalla = r"C:\Users\brayn\Desktop\Prueba-automatizada-bj\capturas"
        test3_img1 = "Prueba_03_test_play_chess.png"
        almacenar = captura_de_pantalla + "/" + test3_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        # Esperar hasta que el botón "random" sea clicable
        random_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@data-cy='random']",
                )
            )
        )
        random_button.click()

        # Esperar hasta que el botón "Play" sea clicable
        play_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'ui_v5-button-primary') and contains(@class, 'ui_v5-button-large') and contains(@class, 'ui_v5-button-full') and @title='Play']",
                )
            )
        )
        play_button.click()

        test3_img2 = "Prueba_03_test_play_chess_02.png"
        almacenar_2 = captura_de_pantalla + "/" + test3_img2
        driver.save_screenshot(almacenar_2)
        time.sleep(7)

    # Test para historia 3: Botón de Búsqueda Funcional Después de Iniciar Sesión en Chess.com
    def test_search_logged_in_04(self):
        driver = self.driver
        driver.get("https://www.chess.com")

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

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Esperar hasta que el icono de búsqueda sea cliclable
        search_icon = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class, 'search-tooltip-component')]")
            )
        )
        search_icon.click()

        # Esperar hasta que el campo de búsqueda sea visible y clicable
        search_input = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[@placeholder='Buscar' and @class='ui_v5-input-component']",
                )
            )
        )

        # Ingresar la palabra clave de búsqueda
        search_input.send_keys("yuca")

        # Presionar Enter para realizar la búsqueda
        search_input.send_keys(Keys.ENTER)

        captura_de_pantalla = r"C:\Users\brayn\Desktop\Prueba-automatizada-bj\capturas"
        test4_img1 = "Prueba_04_test_search_logged_in_chess.png"
        almacenar = captura_de_pantalla + "/" + test4_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        # Aumentar el tiempo de espera para los resultados de la búsqueda
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-result-component"))
        )

    # Test para historia 4:
    def test_play_with_friend_by_username_05(self):
        driver = self.driver
        driver.get("https://www.chess.com")

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
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        play_with_friend_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, '/play/online/friend')]")
            )
        )
        play_with_friend_link.click()

        # Esperar hasta que el campo de búsqueda de amigo sea visible y clicable
        friend_search_input = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[@name='play-friend-search-input' and @class='play-friend-search-input-input']",
                )
            )
        )

        # Ingresar el nombre del amigo a buscar
        friend_search_input.send_keys("kelyn")

        captura_de_pantalla = r"C:\Users\brayn\Desktop\Prueba-automatizada-bj\capturas"
        test5_img1 = "Prueba_05_test_play_with_friend_by_username_chess.png"
        almacenar = captura_de_pantalla + "/" + test5_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        # Esperar a que aparezca el resultado de búsqueda
        friend_search_result = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@class, 'user-username-link') and text()='kelyn']",
                )
            )
        )
        friend_search_result.click()
        time.sleep(7)
        test5_img2 = "Prueba_05_test_play_with_friend_by_username_chess_02.png"
        almacenar2 = captura_de_pantalla + "/" + test5_img2
        driver.save_screenshot(almacenar2)
        time.sleep(5)

    # Test para historia 5:
    def test_edit_profile_06(self):
        driver = self.driver
        driver.get("https://www.chess.com")

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
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Hacer clic en el enlace del perfil
        profile_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'home-username-link')]")
            )
        )
        profile_link.click()

        # Hacer clic en el enlace de editar perfil
        edit_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'edit-container')]")
            )
        )
        edit_link.click()

        captura_de_pantalla = r"C:\Users\brayn\Desktop\Prueba-automatizada-bj\capturas"
        test6_img1 = "Prueba_06_test_edit_profile_chess.png"
        almacenar = captura_de_pantalla + "/" + test6_img1
        driver.save_screenshot(almacenar)
        time.sleep(5)

        # Escribir en el campo de texto
        about_textarea = self.wait.until(
            EC.element_to_be_clickable((By.ID, "profile_about"))
        )
        about_textarea.send_keys("¡Hola! Soy un jugador apasionado de ajedrez.")

        # Guardar los cambios
        save_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "profile_save"))
        )
        save_button.click()

        test6_img2 = "Prueba_06_test_edit_profile_chess_02.png"
        almacenar2 = captura_de_pantalla + "/" + test6_img2
        driver.save_screenshot(almacenar2)
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.wrong_username_and_password_popup_modal = (By.XPATH, '//*[@data-test="error"]')

    def open_login_page(self, url):
        """Membuka halaman login."""
        self.driver.get(url)

    def enter_username(self, username):
        """Memasukkan username."""
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        """Memasukkan password."""
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        """Klik tombol login."""
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """Melakukan login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_pop_up_modal_text(self):
        pop_up_modal_text = self.driver.find_element(*self.wrong_username_and_password_popup_modal).text
        return pop_up_modal_text
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.title_home_page = (By.XPATH, '//*[@data-test="title"]')
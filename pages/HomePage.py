from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.title_home_page = (By.XPATH, '//*[@data-test="title"]')

    def get_text_title_home_page_get(self):
        title_home_page_textself = self.driver.find_element(*self.title_home_page).text
        return title_home_page_textself
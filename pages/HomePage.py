from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.title_home_page = (By.XPATH, '//*[@data-test="title"]')
        self.add_to_cart_backpack_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.add_to_cart_bolt_tshirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')

    def get_text_title_home_page_get(self):
        title_home_page_text = self.driver.find_element(*self.title_home_page).text
        return title_home_page_text

    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self.add_to_cart_backpack_button).click()

    def click_add_to_cart_bolt_tshirt(self):
        self.driver.find_element(*self.add_to_cart_bolt_tshirt).click()
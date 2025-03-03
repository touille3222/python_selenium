import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from selenium import webdriver

class TestLoginPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Inisialisasi WebDriver sebelum setiap test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.login_page.open_login_page("https://www.saucedemo.com/")
        yield
        """Menutup WebDriver setelah setiap test."""
        self.driver.quit()

    def test_successful_login(self):
        """Test login berhasil."""
        self.login_page.login("standard_user", "secret_sauce")
        # Tambahkan assertion untuk memverifikasi login berhasil
        assert "inventory.html" in self.driver.current_url
        assert "Products" in self.home_page.get_text_title_home_page_get()
        print(self.home_page.get_text_title_home_page_get())
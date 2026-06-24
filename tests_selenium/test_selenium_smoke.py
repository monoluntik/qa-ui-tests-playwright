"""
Selenium smoke-тесты для saucedemo.com.
Дублируют ключевые сценарии логина и корзины для демонстрации
знания Selenium наряду с Playwright.
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


def _login(driver, username=VALID_USER, password=VALID_PASS):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


@pytest.mark.selenium
def test_selenium_login_success(driver):
    _login(driver)
    assert "/inventory.html" in driver.current_url


@pytest.mark.selenium
def test_selenium_login_locked_user_shows_error(driver):
    _login(driver, username="locked_out_user")
    wait = WebDriverWait(driver, 5)
    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "locked out" in error.text.lower()


@pytest.mark.selenium
def test_selenium_add_to_cart_updates_badge(driver):
    _login(driver)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
    )
    assert badge.text == "1"

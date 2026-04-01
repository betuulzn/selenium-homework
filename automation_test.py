import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestAutomationExercise(unittest.TestCase):

    URL = "https://automationexercise.com/"

    HOME_LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    ALL_PRODUCTS_TEXT = (By.XPATH, "//h2[contains(text(),'All Products')]")

    FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")

    FIRST_ADD_TO_CART = (By.XPATH, "(//a[@data-product-id='1'])")
    SECOND_ADD_TO_CART = (By.XPATH, "(//a[@data-product-id='2'])")

    CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")
    VIEW_CART = (By.XPATH, "//u[text()='View Cart']")

    CART_PRODUCTS = (By.XPATH, "//tr[contains(@id,'product')]")
    PRODUCT_PRICES = (By.XPATH, "//td[@class='cart_price']")
    PRODUCT_QUANTITY = (By.XPATH, "//td[@class='cart_quantity']")
    PRODUCT_TOTAL = (By.XPATH, "//td[@class='cart_total']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)

    # 🔥 HER SEFERİNDE REKLAMI TEMİZLE
    def remove_ads(self):
        self.driver.execute_script("""
            document.querySelectorAll("iframe").forEach(el => el.remove());
        """)

    def test_add_products_to_cart(self):
        driver = self.driver
        actions = ActionChains(driver)

        time.sleep(3)
        self.remove_ads()

        # Ana sayfa
        self.assertTrue(driver.find_element(*self.HOME_LOGO).is_displayed())

        # Products
        self.remove_ads()
        driver.execute_script("arguments[0].click();", driver.find_element(*self.PRODUCTS_BUTTON))
        time.sleep(2)

        self.assertTrue(driver.find_element(*self.ALL_PRODUCTS_TEXT).is_displayed())

        # 1. ürün
        self.remove_ads()
        first_product = driver.find_element(*self.FIRST_PRODUCT)
        actions.move_to_element(first_product).perform()
        time.sleep(1)

        self.remove_ads()
        driver.execute_script("arguments[0].click();", driver.find_element(*self.FIRST_ADD_TO_CART))

        time.sleep(2)
        driver.find_element(*self.CONTINUE_SHOPPING).click()

        # 2. ürün
        self.remove_ads()
        second_product = driver.find_element(*self.SECOND_PRODUCT)
        actions.move_to_element(second_product).perform()
        time.sleep(1)

        self.remove_ads()
        driver.execute_script("arguments[0].click();", driver.find_element(*self.SECOND_ADD_TO_CART))

        time.sleep(2)
        driver.find_element(*self.VIEW_CART).click()
        time.sleep(2)

        # Sepet kontrol
        cart_products = driver.find_elements(*self.CART_PRODUCTS)
        self.assertEqual(len(cart_products), 2)

        prices = driver.find_elements(*self.PRODUCT_PRICES)
        quantities = driver.find_elements(*self.PRODUCT_QUANTITY)
        totals = driver.find_elements(*self.PRODUCT_TOTAL)

        self.assertEqual(len(prices), 2)
        self.assertEqual(len(quantities), 2)
        self.assertEqual(len(totals), 2)

        for price in prices:
            self.assertIn("Rs.", price.text)

        for qty in quantities:
            self.assertTrue(qty.text.isdigit())

        for total in totals:
            self.assertIn("Rs.", total.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
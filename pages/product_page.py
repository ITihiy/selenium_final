from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'No "Add to basket" button'

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_name_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        p_name = self.browser.find_elements(By.CSS_SELECTOR, '.alertinner')[0].find_element_by_tag_name('strong').text
        assert product_name == p_name, f'Product names do not match. Expected: {product_name}, got {p_name}'

    def should_be_product_price_match(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        p_price = self.browser.find_elements(By.CSS_SELECTOR, '.alertinner')[2].find_element_by_tag_name('strong').text
        assert product_price == p_price, f'Prices do not match. Expected: {product_price}, got {p_price}'


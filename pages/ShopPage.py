from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    btn_checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def click_CheckOut(self):
        self.driver.find_element(*ShopPage.btn_checkout).click()
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    lnk_shop = (By.CSS_SELECTOR, "a[href*='shop']")
    txt_name = (By.NAME, "name")
    txt_email = (By.NAME, "email")

    def click_shopItems(self):
        self.driver.find_element(*HomePage.lnk_shop).click()

    def enter_name(self, name):
        self.driver.find_element(*HomePage.txt_name).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*HomePage.txt_email).send_keys(email)
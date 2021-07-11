import time

import pytest

from datatest.AccountData import AccountData
from pages.BasePage import BasePage
from pages.HomePage import HomePage
from pages.ShopPage import ShopPage


class TestFirst(BasePage):

    @pytest.mark.smoke_all
    def test_01(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        print(self.driver.title)
        print(self.driver.current_url)

        homePage = HomePage(self.driver)
        time.sleep(3)
        homePage.enter_name("khuong")
        homePage.enter_email("khuong.truong@gmail.com")
        time.sleep(3)
        homePage.click_shopItems()

    @pytest.mark.regression_all
    def test_02(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        print(self.driver.title)
        print(self.driver.current_url)

        homePage = HomePage(self.driver)
        shopPage = ShopPage(self.driver)
        time.sleep(3)
        homePage.enter_name("khuong")
        homePage.enter_email("khuong.truong@gmail.com")
        time.sleep(3)
        homePage.click_shopItems()
        shopPage.click_CheckOut()
        time.sleep(3)

    @pytest.mark.dataset
    def test_03(self, getAccoutData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        print(self.driver.title)
        print(self.driver.current_url)

        homePage = HomePage(self.driver)
        shopPage = ShopPage(self.driver)
        time.sleep(3)
        homePage.enter_name(getAccoutData["name"])
        homePage.enter_email(getAccoutData["email"])
        time.sleep(3)
        homePage.click_shopItems()
        shopPage.click_CheckOut()
        time.sleep(3)

    @pytest.fixture(params=AccountData.Account_Data)
    def getAccoutData(self, request):
        return request.param
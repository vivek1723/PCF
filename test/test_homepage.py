from unittest import TestCase

import pytest

from pageodjects.pom_homepage import PageHome


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestHome(TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hm = PageHome(self.driver)

    # Actual tests
    # sample test case which will run, THIS WILL RUN SUCCESSFULLY
    def test_logout_works(self):
        self.hm.get_browser()
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.click_logout()

    # test case from here onwards will not run and fail as the required feature is not available yet, they can be comment out
    # Valid user name, invalid password
    def test_login1(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login('validUser', 'invalidPswd', 'Please check login credentials')

    # Invalid user name, Valid password
    def test_login2(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login('invalidUser', 'validPswd', 'Please check login credentials')

    # invalid user name, invalid password
    def test_login3(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login('invalidUser', 'invalidPswd', 'Please check login credentials')

    # empty user name and password
    def test_login4(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login(' ', ' ', 'Please check login credentials')

    # empty user name and valid password
    def test_login5(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login(' ', 'validPswd', 'Please check login credentials')

    # valid user name and emptypassword
    def test_login6(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login('validUser', ' ', 'Please check login credentials')

    # Valid user name, Valid password
    def test_login7(self):
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login('validUser', 'validPswd')

    # test log out feature
    def test_logout(self):
        self.hm.get_browser()
        self.hm.wait_for_page()
        self.hm.click_ham_menu()
        self.hm.test_login('validUser', 'validPswd')
        self.hm.click_logout()

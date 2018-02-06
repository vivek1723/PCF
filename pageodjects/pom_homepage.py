from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from base.basepage import BasePage
from config import config


class PageHome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Selector value
    _sign_in = "[id='my-id']>div>ul>li"  # css
    _log_out = "div.message-row.text-right > span > div"  # css
    _bot_initializaion = '#chat > div.conversation > div.message-row.button-row'  # css
    _ham_menu = 'a.c-hamburger.c-hamburger--htx'  # css
    _menu_options = "[id='my-id']>div>ul>li"  # css
    _ele_lgn = 'id'  # id
    _ele_pswd = 'pswd'  # id
    _ele_sbt = 'btnsubmit'  # id
    _err_msg = '.msg'  # css

    # waits for a chat-bot initialization
    def wait_for_page(self):
        '''waits for a chat-bot initialization'''
        try:
            WebDriverWait(self.driver, config.driver_wait).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, self._bot_initializaion)))
            # return True
        except Exception as e:
            print("Bot isn't initialized", e)

    # clicks on the hamburger menu
    def click_ham_menu(self):
        '''clicks on the hamburger menu'''
        try:
            WebDriverWait(self.driver, config.driver_wait).until(
                ec.visibility_of(self.driver.find_element_by_css_selector(self._ham_menu)))
            print('Found hamburger menu')
            ele_hmenu = self.driver.find_element_by_css_selector(self._ham_menu)
            ele_hmenu.click()
        except Exception as e:
            print('Hamburger menu not found', e)

    def click_logout(self):
        '''This method clicks on the logout option'''
        try:
            WebDriverWait(self.driver, config.driver_wait).until(
                ec.visibility_of(self.driver.find_element_by_css_selector(self._menu_options)))
            print('Menu options found')
            ele_options = self.driver.find_elements_by_css_selector(self._menu_options)
            for ele in ele_options:
                print(ele)
                option = ele.text
                print(option)
                if option == 'Log Out':
                    ele.click()
                    break
            WebDriverWait(self.driver, config.driver_wait).until(
                ec.presence_of_element_located(By.CSS_SELECTOR(self._log_out)))
            user_text = self.driver.find_elements_by_xpath(self._log_out)
            for text in user_text:
                if text.text == '//logout':
                    print('Logout test passed')
                else:
                    print('Logout test failed')
        except Exception as e:
            print('Menu options not found', e)

    # method to test login, since login feature is not available I've assumed all the elements here
    def test_login(self, user_name, password, err_msg=''):
        '''This method takes 3 arguments, username, password and optional error message'''
        # clicks on the login option
        try:
            WebDriverWait(self.driver, config.driver_wait).until(
                ec.visibility_of(self.driver.find_element_by_css_selector(self._sign_in)))
            ele_options = self.driver.find_elements_by_css_selector(self._sign_in)
            for ele in ele_options:
                option = ele.text
                if option == 'Sign in':
                    print('Sign-in option found and clicking it')
                    # it will click on the sign in option and hamburger menu will close
                    ele.click()
                    break
        except Exception as e:
            print('Sign-in option not found', e)

        # waits for the sign-in options/page to load
        WebDriverWait(self.driver, config.driver_wait).until(ec.presence_of_element_located(By.ID(self._ele_lgn)))
        ele_lgn = self.driver.find_element_by_id(self._ele_lgn)
        ele_pswd = self.driver.find_element_by_id(self._ele_pswd)
        ele_sbt = self.driver.find_element_by_id(self._ele_sbt)
        ele_lgn.clear()
        ele_lgn.send_keys(user_name)
        ele_pswd.clear()
        ele_pswd.send_keys(password)
        ele_sbt.submit()

        # user will land on dashboard upon successful login, soft assert to check browser title

        if self.driver.title == 'User Dashboard':  # assumed dashboard title
            print('Test pass')
        else:
            # wait for message to be visible to user
            WebDriverWait(self.driver, config.driver_wait).until(
                ec.visibility_of(self.driver.find_element_by_css_selector(self._err_msg)))
            ele_login = self.driver.find_element_by_css_selector(self._err_msg)
            err_login = ele_login.text
            # comparing if the actual and expected messages are same
            if err_msg == err_login:
                print('Test pass')
            else:
                print('Test fail')

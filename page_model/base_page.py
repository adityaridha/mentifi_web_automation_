from connection_setup import Connection
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pytest

class BasePage():

    driver = Connection.driver

    def __init__(self):
        pass

    def find_mode(self, element, mode = None):
        if mode == "visibility": condition = ec.visibility_of_element_located(element)
        elif mode == "invisibility": condition = ec.invisibility_of_element_located(element)
        else: condition = ec.presence_of_element_located(element)
        return condition

    def find_element(self, element, time_out=5, mode=None):
        condition = self.find_mode(element, mode)
        try:
            result = WebDriverWait(self.driver, time_out).until(condition)
            return result
        except TimeoutException:
            pytest.fail(msg="This element couldn't be found : {} ".format(element))

    def find_elements(self, element, time_out=5):
        try:
            result = WebDriverWait(self.driver, time_out).until(ec.presence_of_all_elements_located(element))
            return result
        except TimeoutException:
            pytest.fail(msg="This element couldn't be found : {} ".format(element))

    def verify_elements(self, elements):
        for element in elements:
            result = self.find_element(element, time_out=10)
            if result != False:
                print("element found : {} ".format(element))



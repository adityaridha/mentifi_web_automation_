from page_model import BasePage
from selenium.webdriver.common.by import By
import time


class Messages(BasePage):

    loc_compose_messages = (By.XPATH, "//a[@onclick='composeNewMessage()']")
    loc_receiver_textbox = (By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']")
    receiver = (By.XPATH, "//span[contains(text(),'Dan Ega')]")

    def __init__(self):
        super().__init__()

    def click_compose_messages(self):
        self.find_element(self.loc_compose_messages).click()

    def input_message_receiver(self):
        self.find_element(self.loc_receiver_textbox, mode="visibility").click()
        self.find_element(element=self.receiver, mode="visibility").click()

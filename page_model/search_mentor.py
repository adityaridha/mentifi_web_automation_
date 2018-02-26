from page_model import BasePage
from selenium.webdriver.common.by import By

class SearchMentor(BasePage):

    loc_search_mentor = (By.NAME, 'sc')
    loc_available_connections = (By.XPATH, "//h3[@class='business-name business-flipcard-truncate']")
    loc_candidate_connection = (By.XPATH, )

    def __init__(self):
        super().__init__()

    def input_search_mentor(self):
        self.find_element(self.loc_search_mentor).send_keys("Nama")

    def get_available_connections(self):
        mentor_name = self.find_elements(self.loc_available_connections)
        print("there is {} available connections".format(len(goals_name)))
        for name in mentor_name:
            print(name.text)

    def get_one_connection_name(self):
        mentor_name = self.find_elements(self.loc_available_connections)
        name = mentor_name[1].text
        print("Choose this mentor for new connection {}".format(name))
        return name

    def click_connect_button(self):
        mentor = self.get_one_connection_name()
        self.find_element("//a[@class='connect-mentor btn btn-warning btn-sm btn-connect' and @data-name='{}']".format(mentor)).click()




import time
from page_model import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Dashboard(BasePage):

    loc_home_label = (By.CSS_SELECTOR, "div.page-title")
    loc_company_name = (By.XPATH, "//span[@class='company-name']")

    '''warning popup'''
    loc_user_name = (By.CSS_SELECTOR, "div.name")
    loc_warning_pop_up = (By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']")
    loc_update_later_button = (By.XPATH, "//button[@class='cancel' and contains(text(),'Update later')]")

    '''release notes'''
    loc_release_notes = (By.XPATH, "//div[@class='article-release-note']")
    loc_close_relase_note = (By.XPATH, "//span[@class='k-icon k-i-close']")

    '''mentee menu'''
    loc_goals_title = (By.XPATH, "//h2[contains(text(), 'Goals')]")
    loc_WH_title = (By.XPATH, "//h2[contains(text(), 'Happening')]")
    loc_tasks_title = (By.XPATH, "//h2[contains(text(), 'Tasks')]")
    loc_projects_title = (By.XPATH, "//h2[contains(text(), 'Projects')]")
    loc_goal_expander = (By.XPATH, "//h2[@class='widget-header' and contains(text(),'Goals')]/a")
    loc_tasks_expander = (By.XPATH, "//h2[@class='widget-header' and contains(text(),'Tasks')]/a")
    loc_search_mentor = (By.XPATH, "//span[contains(text(),'Search Mentor')]")

    '''mentor menu'''
    loc_my_mentee_label = (By.XPATH, "//h2[contains(text(), 'My Mentee')]")
    loc_goals_and_tasks_title = (By.XPATH, "//h2[contains(text(), 'Goals & Tasks')]")
    loc_goals_and_tasks_expander = (By.XPATH, "//h2[contains(text(), 'Goals & Tasks')]/a")

    '''menu'''
    loc_messages_menu = (By.ID, "21")



    def __init__(self):
        super().__init__()

    def verify_information_pop_up(self):
        try:
            warn_popup = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.loc_warning_pop_up))
            print("[DASHBOARD PAGE] there is warning pop up containing messages :\n{}".format(warn_popup.text))
            WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='overlay']")))
            self.find_element(self.loc_update_later_button).click()
        except TimeoutException:
            print("[DASHBOARD PAGE] No pop up warning messages")

    def verify_release_notes_pop_up(self):
        try:
            close_release_note = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.loc_release_notes))
            print("[DASHBOARD PAGE] Release note content : \n{}".format(close_release_note.text))
            WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='overlay']")))
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()
        except TimeoutException:
            print("[DASHBOARD PAGE] No release note pop up")

    def get_logged_user_name(self):
        user_name = self.find_element(self.loc_user_name).text
        print("[DASHBOARD PAGE]user name displayed: {}".format(user_name))

    def verify_dashboard_elements(self):
        home = self.find_element(self.loc_home_label)
        assert home.text == "Home"

        company_name = self.find_element(self.loc_company_name)
        print("[DASHBOARD PAGE] Company Name label, actual value = {}".format(company_name.text))
        assert company_name.text == "Mentifi"

    def verify_mentor_dashboard(self):
        self.verify_dashboard_elements()
        mentor_menu = [self.loc_my_mentee_label]
        self.verify_elements(mentor_menu)

    def verify_mentee_dashboard(self):
        self.verify_dashboard_elements()
        mentee_menu = [self.loc_goals_title, self.loc_tasks_title, self.loc_WH_title, self.loc_projects_title]
        self.verify_elements(mentee_menu)

    def click_goals_expander(self):
        self.find_element(self.loc_goal_expander).click()

    def click_tasks_expander(self):
        self.find_element(self.loc_tasks_expander).click()

    def click_search_mentor(self):
        self.find_element(self.loc_search_mentor).click()

    def click_messages_menu(self):
        self.find_element(self.loc_messages_menu).click()




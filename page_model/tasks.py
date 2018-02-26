from page_model import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time


class Tasks(BasePage):

    loc_add_new_task = (By.ID, "add-new-task")
    loc_task_connection_drop_down = (By.XPATH, "//span[@class='k-input']")
    loc_list_tasks_view_options = (By.XPATH, "//li[@class='k-item' and contains(text(),'')]")
    loc_show_completed_task = (By.XPATH, "//span[contains(text(),'Show')]")

    ''' add task '''
    loc_task_title = (By.ID, "task")
    loc_due_date = (By.ID, "dueDate")
    loc_assigned_to = (By.XPATH, "//span[@class='k-input' and contains(text(),'Unassigned')]")
    loc_priority_medium = (By.XPATH, "//label[@class='k-radio-label' and @for='radio-priority_2']")
    loc_is_private = (By.XPATH, "//label[@class='k-checkbox-label lighter' and contains(text(),'private')]")
    loc_is_completed = (By.XPATH, "//label[@class='k-checkbox-label lighter' and contains(text(),'completed')]")
    loc_button_save = (By.XPATH, "//a[@onclick='saveTaskForm()']")

    def __init__(self):
        super().__init__()

    def verify_all_tasks_element_is_displayed(self):
        task_elements = [self.loc_task_connection_drop_down, self.loc_show_completed_task]
        self.verify_elements(task_elements)

    def verify_all_add_task_elements_is_displayed(self):
        add_task_elements = [self.loc_task_title,
                             self.loc_due_date,
                             self.loc_assigned_to,
                             self.loc_priority_medium,
                             self.loc_is_private,
                             self.loc_is_completed]

        self.verify_elements(add_task_elements)

    def click_add_new_task(self):
        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='overlay']")))
        self.find_element(self.loc_add_new_task).click()

    def click_dropdown_show_task_for(self, connection_name):
        # click dropdown
        selected = self.find_element(self.loc_task_connection_drop_down)
        print("currently selected : {}".format(selected.text))
        selected.click()

        # get connection name
        connections = self.find_elements(self.loc_list_tasks_view_options)
        print("list conenction available:")
        for con in connections:
            print(con.text)

        self.find_element((By.XPATH, "//li[@class='k-item' and contains(text(),'{}')]".format(connection_name))).click()

    def input_task_title(self):
        self.verify_all_add_task_elements_is_displayed()
        self.find_element(self.loc_task_title).send_keys("Dari Python")

    def input_due_date(self):
        self.find_element(self.loc_due_date).send_keys("Dari Python")

    def select_assignee(self, assignee):
        self.find_element(self.loc_assigned_to).click()
        loc_assignee = (By.XPATH, "//li[@class='k-item' and contains(text(),'{}')]".format(assignee))
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(loc_assignee)).click()

    def click_priority_medium(self):
        WebDriverWait(self.driver, 10).until(
            ec.invisibility_of_element_located((By.XPATH, "//div[@class='k-animation-container']")))
        self.find_element(self.loc_priority_medium).click()

    def set_is_complete_true(self):
        self.find_element(self.loc_is_completed).click()

    def set_is_private_true(self):
        self.find_element(self.loc_is_private).click()

    def click_save_button(self):
        self.find_element(self.loc_button_save).click()

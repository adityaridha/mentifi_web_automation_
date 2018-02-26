from page_model import BasePage
from selenium.webdriver.common.by import By
from utility import ScreenCapture

screen_capture = ScreenCapture()

class Goals(BasePage):

    loc_add_new_goals_button = (By.ID, "add-new-goal")
    loc_goal_options_button = (By.XPATH,"//i[@class='fa fa-ellipsis-h']")
    loc_edit_goal = (By.XPATH,"//ul[@class='dropdown-menu widget-goal-menu']/li/a[contains(text(),'Edit')]")
    loc_edit_add_progress = (By.XPATH,"//a[contains(text(),'Add Progress')]")
    loc_edit_progress_log = (By.XPATH, "//a[contains(text(),'Progress Log')]")
    loc_edit_remove_goal = (By.XPATH, "//a[contains(text(),'Remove Goal')]")
    loc_list_goal_name = (By.XPATH, "//div[@id='listview-goals']/div/div/div[@class='col-xs-7']" )
    loc_list_probability = (By.XPATH, "//div[@class='col-xs-1']/img")

    ''' add goal '''
    loc_goal_title = (By.ID, "GoalDescription")
    loc_probability = (By.XPATH, "//label[@for='radio-goal-probability_2']")
    loc_save_goal_button = (By.ID, "button-mentifi-goal-save")
    loc_goal_added_text = (By.XPATH, "//p[contains(text(),'Goal added')]")

    ''' delete goal '''
    loc_delete_confirmation_popup = (By.XPATH, "//span[@class='noty_text' and contains(text(),'Are you sure you want to delete this goal?')]")
    loc_ok_button = (By.XPATH, "//button[@class='btn btn-primary' and contains(text(),'Ok')]")
    loc_cancel_button = (By.XPATH, "//button[@class='btn btn-danger' and contains(text(),'Cancel')]")


    def __init__(self):
        super().__init__()

    def get_list_goals(self):
        goals_name = self.find_elements(self.loc_list_goal_name)
        print("there is {} goals already created".format(len(goals_name)))
        for index, name in enumerate(goals_name):
            print("Goals title {} : {}".format(index, name.text))

    def click_add_new_goal(self):
        self.find_element(self.loc_add_new_goals_button).click()

    def click_goal_options_button(self):
        self.find_element(self.loc_goal_options_button).click()

    def click_edit_goal_button(self):
        self.find_element(self.loc_edit_goal).click()

    def input_goal_title(self):
        self.find_element(self.loc_goal_title).send_keys("Goal title dari Python")

    def select_probability(self):
        self.find_element(self.loc_probability).click()

    def click_save_goal_button(self):
        self.find_element(self.loc_save_goal_button).click()

    def verify_goal_successfully_added(self):
        success_message = self.find_element(self.loc_goal_added_text)
        screen_capture.capture_successfull_test("success_add_goal.png")
        print("pop up messages : {}".format(success_message.text))







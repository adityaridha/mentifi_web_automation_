import page_model

login = page_model.Login()
dashboard = page_model.Dashboard()
goals = page_model.Goals()

class TestGoals():

    def test_create_goal(self):
        login.input_email_address("garrynilson@mailinator.com")
        login.input_password("ZXasqw12")
        login.click_login_button()
        dashboard.verify_information_pop_up()
        dashboard.verify_release_notes_pop_up()
        dashboard.verify_mentee_dashboard()
        dashboard.get_logged_user_name()
        dashboard.click_goals_expander()
        goals.get_list_goals()
        goals.click_add_new_goal()
        goals.input_goal_title()
        goals.select_probability()
        goals.click_save_goal_button()
        goals.verify_goal_successfully_added()








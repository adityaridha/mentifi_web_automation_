import page_model
import pytest

login = page_model.Login()
dashboard = page_model.Dashboard()
tasks = page_model.Tasks()

class TestTasks():

    def test_create_tasks(self):
        login.input_email_address("garrynilson@mailinator.com")
        login.input_password("ZXasqw12")
        login.click_login_button()
        dashboard.verify_information_pop_up()
        dashboard.verify_release_notes_pop_up()
        dashboard.verify_mentee_dashboard()
        dashboard.get_logged_user_name()
        dashboard.click_tasks_expander()
        tasks.click_dropdown_show_task_for("Dan Egan")
        tasks.click_add_new_task()
        tasks.input_task_title()
        tasks.select_assignee("Dan Egan")
        tasks.click_priority_medium()
        tasks.set_is_complete_true()
        tasks.click_save_button()





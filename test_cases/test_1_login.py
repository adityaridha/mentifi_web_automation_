import page_model

login = page_model.Login()
dashboard = page_model.Dashboard()


class TestLogin():

    def test_all_page_element_is_loaded(self):
        login.verify_login_page_elements()

    def test_mentee_login_with_valid_credentials(self):
        login.input_email_address("bezita@mailinator.com")
        login.input_password("ZXasqw12")
        login.click_login_button()
        dashboard.verify_information_pop_up()
        dashboard.verify_release_notes_pop_up()
        dashboard.verify_mentee_dashboard()
        dashboard.get_logged_user_name()

    def test_mentor_login_with_valid_credentials(self):
        login.input_email_address("amberheard@mailinator.com")
        login.input_password("ZXCasdqwe123")
        login.click_login_button()
        dashboard.verify_mentor_dashboard()
        dashboard.get_logged_user_name()


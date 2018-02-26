import page_model

login = page_model.Login()
dashboard = page_model.Dashboard()


class TestConnections():

    def test_all_page_element_is_loaded(self):
        login.verify_login_page_elements()



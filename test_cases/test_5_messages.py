from page_model import Login, Dashboard, Messages

login = Login()
dashboard = Dashboard()
messages = Messages()

class TestMessages():

    def test_go_to_messages_menu(self):
        login.login_as_mentee(name="garrynilson@mailinator.com",password="ZXasqw12")
        dashboard.verify_information_pop_up()
        dashboard.verify_release_notes_pop_up()
        dashboard.click_messages_menu()
        messages.click_compose_messages()
        messages.input_message_receiver()



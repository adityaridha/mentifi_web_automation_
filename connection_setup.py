from selenium import webdriver

class Connection(object):

        LOGIN_URL = "https://test-edu-tvc49e7wfo.hub3c.com/"
        OPTIONS = webdriver.ChromeOptions()
        OPTIONS.add_argument("--start-maximized")
        OPTIONS.add_argument("--disable-infobars")
        OPTIONS.add_argument("--disable-extensions")
        OPTIONS.add_experimental_option(
                "prefs", {
                        "profile.default_content_setting_values.media_stream_mic": 1,
                        "profile.default_content_setting_values.media_stream_camera": 1,
                        "profile.default_content_setting_values.geolocation": 1,
                        "profile.default_content_setting_values.notifications": 1 })

        print("\nSETUP CONNECTION WITH CHROME BROWSER...")
        driver = webdriver.Chrome(chrome_options=OPTIONS)
        driver.get(LOGIN_URL)



from connection_setup import Connection
from pathlib import Path
from datetime import datetime

class ScreenCapture():

    root = str(Path(__file__).parents[1])
    driver = Connection.driver
    current_date = str(datetime.now())

    def __init__(self):
        pass

    def capture_successfull_test(self, file_name):
        self.driver.get_screenshot_as_file(self.root + "\\test_report\\{}".format(file_name))

    def capture_failed_test(self, file_name):
        self.driver.get_screenshot_as_file(self.root + "\\test_report\\failed_test\\{}".format(file_name))

if __name__ == '__main__':
    sc = ScreenCapture()
    print(sc.root)
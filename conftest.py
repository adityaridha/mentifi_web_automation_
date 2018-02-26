import pytest
from connection_setup import Connection
from utility import ScreenCapture

driver = Connection.driver
screen_capture = ScreenCapture()

@pytest.fixture(autouse=True)
def setup_teardown_test_cases():

    print("\n#################### set up test case session")
    yield
    print("\n#################### tear down test case session")
    # whether test is success or failed this code will still executed
    driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/SignOut")

@pytest.fixture(scope='session', autouse=True)
def teardown_session():
    yield
    print("\n#################### tear down session")
    # driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport():

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            file_name = file_name.replace("/","_")
            screen_capture.capture_failed_test(file_name)




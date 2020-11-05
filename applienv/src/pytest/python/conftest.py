import pytest
from applitools.selenium import Eyes, Target, BatchInfo, ClassicRunner, VisualGridRunner,BrowserType,DeviceName
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--eyes-mode',action="store", default="local", help="modes: grid or local")
    
@pytest.fixture(scope="module")
def batch_info():
    return BatchInfo("FZ UI Verification cases")


@pytest.fixture(name="driver", scope="function")
def driver_setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.flydubai.com/en/")
    yield driver
    driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup(request):
    if request.config.getoption("--eyes-mode")=='fast':
        runner= VisualGridRunner(1)
    else:
        runner = ClassicRunner()
    yield runner
    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)


@pytest.fixture(name="eyes", scope="function")
def eyes_setup(runner, batch_info,request):
    eyes = Eyes(runner)
    eyes.configure.set_api_key("lqtaza1033ohKy9w9owjrKp3e2DkqJW0g75gqGJPZh107Qs110")
    eyes.configure.batch = batch_info
    if request.config.getoption("--eyes-mode")=='fast':
        (
        eyes.configure.add_browser(1600, 1200, BrowserType.CHROME)
        .add_browser(1600, 1200, BrowserType.FIREFOX)
        .add_browser(1600, 1200, BrowserType.IE_11)
        .add_browser(1600, 1200, BrowserType.EDGE_LEGACY)
        .add_browser(1600, 1200, BrowserType.SAFARI)
        )
    #eyes.configure.set_force_full_page_screenshot(True)
    yield eyes
    eyes.abort_if_not_closed()
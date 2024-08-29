from selene import browser
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'http://demoqa.com'

    options = Options()
    options.add_argument("--headless")

    browser.config.timeout = 10

    browser.config.driver_options = options
    browser.config.window_width = 1280
    browser.config.window_height = 720


    yield

    browser.quit()
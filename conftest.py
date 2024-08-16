from selene import browser
from components.demoqa import should_be_open_elements_page
import pytest


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
 browser.config.base_url = 'http://demoqa.com'
 browser.config.window_width = 1280
 browser.config.window_height = 720

 @pytest.mark.parametrize('url',["https://demoqa.com/elements"])
def test_open_elements_page(url):
    should_be_open_elements_page()


 yield

 browser.quit()
import pytestfrom selene
import browser, support


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
 browser.config.base_url = 'http://demoqa.com'
 browser.config.window_width = 1280
 browser.config.window_height = 720

 yield

 browser.quit()
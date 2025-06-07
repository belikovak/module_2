import pytest

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

path_to_driver = 'C:/chrome-win32/chrome.exe'

@pytest.fixture()
def set_up_browser():

    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
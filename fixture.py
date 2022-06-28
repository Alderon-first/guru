from selene.support.shared import browser
from selene import be, have
import pytest

url='https://www.google.com'

@pytest.fixture()
def setup():
    print('подготовка к прогону')
    browser.open(url)
    yield
    print('прогон завершен')


@pytest.fixture()
def config(setup):
    browser.driver.set_window_size(width=1920, height=1080)

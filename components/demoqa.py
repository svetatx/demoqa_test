from selene import browser, be, have
from selene.support.shared.jquery_style import s
import pytest

def open_elements_page():
    browser.open("https://demoqa.com/")

def get_button():
    return s("#button")

def should_be_open_elements_page():
    browser.should(have.url("https://demoqa.com/elements"))
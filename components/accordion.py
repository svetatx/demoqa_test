from selene import browser, by, have
from selene.support.shared.jquery_style import s

def visit():
    browser.open("/elements")

def close_section_with_name():
    return s(by.xpath("//*[text()='Elements']")).click()

def should_be_open_elements_page():
    browser.should(have.url("/elements"))
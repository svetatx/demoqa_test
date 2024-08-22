from selene import browser, have, be
from selene.support.shared.jquery_style import s



def visit():
    browser.open("/elements")

def expand_all():
    s(".rct-collapse-btn").click()

def get_elements_form():
    #  Возвращает элемент с текстом 'Elements'
    return s("div.card-body").element(have.text("Elements"))

def should_be_open_elements_page():
  #Проверяет, что страница элементов открыта.
    browser.should(have.url("/elements"))
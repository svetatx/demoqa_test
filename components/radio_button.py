from selene import browser, have, be
from selene.support.shared.jquery_style import s



def visit_radio_button_page():
    browser.open("/radio-button")

def select_radio_button():
    s("#yesRadio").click()

def should_have_selected_radio_button():
    s("#yesRadio").should(be.selected)
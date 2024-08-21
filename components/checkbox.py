from selene import browser, have, be
from selene.support.shared.jquery_style import s


def visit():
    browser.open("/checkbox")

def expand_all():
    s(".rct-collapse-btn").click()

def get_checkbox():
    return s(".rct-node [for='tree-node-Home']")

def should_be_selected():
    get_checkbox().should(be.selected)

def should_display_selected_text():
    s('#result').should(have.text("Home"))



from selene import browser, by, have, be
from selene.support.shared.jquery_style import s


def visit():
    browser.open("/checkbox")

def expand_all():
    s(".rct-collapse-btn").click()

def desktop():
    return s(by.xpath("//*[@id='tree-node-desktop']/../span[@class='rct-checkbox']"))


def desktop_should_be_selected():
    desktop().should(be.selected)

def should_display_selected_text():
    s("#result").should(have.text("Desktop"))



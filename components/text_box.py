from selene import browser, have, be
from selene.support.shared.jquery_style import s


def visit():
    browser.open("/text-box")

def fullname_field_type(fullname):
    s("#userName").type('fullname')

def email_field_type(email):
    s("#userEmail").type('email')

def current_address_field_type(current_address):
    s("#currentAddress").type('current_address')

def permanent_address_field_type(permanent_address):
    s("#permanentAddress").type('permanent_address')

def submit_button():
    return s("#submit")

def output_should_be_visible():
    s("#output").should(be.visible)


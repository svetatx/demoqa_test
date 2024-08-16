from selene import browser, be, have
from selene.support.shared.jquery_style import s
import pytest

def open():
    browser.open("https://demoqa.com/text-box")

def fullname_field(fullname):
    s("#fullname").type('fullname')

def email_field(email):
    s("#email").type('email')

def current_address_field(current_address):
    s("#current_address").type('address')

def permanent_address_field(permanent_address):
    s("#permanent_address").type('address')

def submit_button():
    return s("#submit")



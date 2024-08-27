from selene import browser, have, be
from selene.support.shared.jquery_style import s,ss



def visit():
    browser.open("/webtables")

def add_new_record():
    s("#addnewRecordButton").click()

def fill_form(first_name, last_name, email, age, salary, department):
    s("#firstName").type(first_name)
    ("#lastName").type(last_name)
    s("#userEmail").type(email)
    s("#age").type(age)
    s("#salary").type(salary)
    s("#department").type(department)
    s("#submit").click()

def should_have_record_with_text(text):
    #ss(".rt-tbody .rt-tr-group").filtered_by(have.text(text)).should(condition.size_greater_than(0))
    ss(".rt-tbody .rt-tr-group").filtered_by(have.text(text)).first.should(be.present)


def delete_record(text):
    record_row = s(".rt-tbody .rt-tr-group").filtered_by(have.text(text))
    record_row.s(".action-buttons span[title='Delete']").click()
    record_row.should_not(be.present)
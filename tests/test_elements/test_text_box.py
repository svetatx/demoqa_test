from selene import browser, be, have
import pytest


def test_submit_text_box_form():
    # Открываем страницу с формой Text Box
    browser.open('https://demoqa.com/text-box')

    # Заполняем поля формы
    browser.element(by.id('userName')).type('Svetlana Zubrilina')
    browser.element(by.id('userEmail')).type('lana.zubrilina@gmail.com')
    browser.element(by.id('currentAddress')).type('123 Main St')
    browser.element(by.id('permanentAddress')).type('123 Another St')

    # Нажимаем на кнопку Submit
    browser.element(by.id('submit')).click()

    # Проверяем, что введенные данные отобразились на странице
    browser.element(by.id('name')).should(have.text('Name:Svetlana Zubrilina'))
    browser.element(by.id('email')).should(have.text('Email:lana.zubrilina@gmail.com'))
    browser.element(by.id('currentAddress')).should(have.text('Current Address :123 Main St'))
    browser.element(by.id('permanentAddress')).should(have.text('Permananet Address :123 Another St'))
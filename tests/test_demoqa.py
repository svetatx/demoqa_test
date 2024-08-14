from selene import browser, have, be




def test_navigation_to_elements_section():
    # Открываем сайт
    browser.open_url('https://demoqa.com/')

    # Переходим в раздел Elements
    browser.element('div.category-cards').element('[href="/elements"]').click()

    # Проверяем, что перешли на страницу элементов
    browser.element('').should(have.text('Elements'))
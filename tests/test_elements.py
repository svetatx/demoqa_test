from components import elements
from selene import be

def test_open_elements_page():
    elements.visit()  # Открыть страницу элементов
    elements.get_elements_form()  # Найти элемент с текстом 'Elements'
    elements.should(be.visible)  # Убедиться, что элемент видим
    elements.click()  # Кликнуть по элементу
    elements.should_be_open_elements_page()  # Проверить, что страница элементов открыта
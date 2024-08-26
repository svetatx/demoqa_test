from components import checkbox

def test_select_desktop_checkbox():
    checkbox.visit()
    checkbox.expand_all()
    checkbox.desktop().click()
    checkbox.desktop_should_be_selected()
    checkbox.should_display_selected_text()

from components import demoqa


def test_open_elements_page():
    demoqa.open()
    demoqa.get_button().click()
    demoqa.should_be_open_elements_page()
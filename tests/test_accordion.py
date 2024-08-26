from components import accordion


def test_close_elements():
    accordion.visit()
    accordion.close_section_with_name()
    accordion.should_be_open_elements_page()
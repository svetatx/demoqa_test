from components import radio_button


def test_radio_button_form():
    radio_button.visit_radio_button_page()
    radio_button.select_radio_button("Yes")
    radio_button.should_have_selected_radio_button("Yes")
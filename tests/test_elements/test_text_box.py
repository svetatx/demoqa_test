from components import text_box




def test_text_box_form():
    text_box.visit()
    text_box.fullname_field_type("Svetlana Zubrilina")
    text_box.email_field_type("lana.zubrilina@gmail.com")
    text_box.current_address_field_type("123 Main St")
    text_box.permanent_address_field_type("123 Another St")
    text_box.submit_button().click()
    text_box.output_should_be_visible()

from components import text_box




def test_text_box_form():
    text_box.open('https://demoqa.com/text-box')
    text_box.fullname_field('Svetlana Zubrilina')
    text_box.email_field('lana.zubrilina@gmail.com')
    text_box.current_address('123 Main St')
    text_box.permanent_adress('123 Another St')
    text_box.submit_buton().click()

def submit_form():
    text_box.open('https://demoqa.com/text-box')
    text_box.fullname_field('Svetlana Zubrilina')
    text_box.email_field('lana.zubrilina@gmail.com')
    text_box.current_address('123 Main St')
    text_box.permanent_adress('123 Another St')
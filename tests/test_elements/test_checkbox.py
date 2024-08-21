from components import checkbox

def test_select_home_checkbox():
    checkbox.visit()
    checkbox.expand_all()
    checkbox.get_checkbox('Home').click()
    checkbox.should_be_selected('Home')
    checkbox.should_display_selected_text('Home')

def test_select_desktop_checkbox():
    checkbox.visit()
    checkbox.expand_all()
    checkbox.get_checkbox('Desktop').click()
    checkbox.should_be_selected('Desktop')
    checkbox.should_display_selected_text('Desktop')

def test_select_documents_checkbox():
    checkbox.visit()
    checkbox.expand_all()
    checkbox.get_checkbox('Documents').click()
    checkbox.should_be_selected('Documents')
    checkbox.should_display_selected_text('Documents')

def test_select_downloads_checkbox():
    checkbox.visit()
    checkbox.expand_all()
    checkbox.get_checkbox('Downloads').click()
    checkbox.should_be_selected('Downloads')
    checkbox.should_display_selected_text('Downloads')
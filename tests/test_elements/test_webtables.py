from components import webtables

def test_add_new_record():
    webtables.visit()
    webtables.add_new_record()
    webtables.fill_form("John", "Doe", "john.doe@example.com", "30", "5000", "Engineering")
    webtables.should_have_record_with_text("John Doe")

def test_delete_record():
    webtables.visit()
    webtables.should_have_record_with_text("John Doe")
    webtables.delete_record("John Doe")
    s(".rt-tbody .rt-tr-group").filtered_by(have.text("John Doe")).should(be.empty)

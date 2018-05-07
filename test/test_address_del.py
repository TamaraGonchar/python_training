from model.contact import CONTACT

def test_delete_first_contact(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(name="Anna", middlename="Ivanovna", lastname="Petrova"))
    old_addnews = app.addnew.get_addnew_list()
    app.addnew.delete_first_contact()
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) - 1 == len(new_addnews)
    old_addnews[0:1] = []
    assert old_addnews == new_addnews

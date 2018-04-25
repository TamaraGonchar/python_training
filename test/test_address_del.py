from model.contact import CONTACT

def test_delete_first_contact(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(name="Anna", middlename="Ivanovna", lastname="Petrova"))
    app.addnew.delete_first_contact()

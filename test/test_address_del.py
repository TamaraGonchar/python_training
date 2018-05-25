from model.contact import CONTACT
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_addnew_list()) == 0:
        app.addnew.createnew(CONTACT(name="Anna", middlename="Ivanovna", lastname="Petrova"))
    old_addnews = db.get_addnew_list()
    contact = random.choice(old_addnews)
    app.addnew.delete_contact_by_id(contact.id)
    new_addnews = db.get_addnew_list()
    assert len(old_addnews) - 1 == len(new_addnews)
    old_addnews.remove(contact)
    assert old_addnews == new_addnews
    if check_ui:
        assert sorted(new_addnews, key=CONTACT.id_or_max) == sorted(app.addnew.get_addnew_list(), key=CONTACT.id_or_max)





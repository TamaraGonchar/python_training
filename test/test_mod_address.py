from model.contact import CONTACT
import random


def test_mod_contact_name(app, db, check_ui):
    if len(db.get_addnew_list()) == 0:
        app.addnew.createnew(CONTACT(name="Alisa"))
    old_addnews = db.get_addnew_list()
    mod_addnew = random.choice(old_addnews)
    new_addnew = CONTACT(name="Klavdiya")
    new_addnew.id = mod_addnew.id
    if new_addnew.name is None:
        new_addnew.name = mod_addnew.name
    if new_addnew.lastname is None:
        new_addnew.lastname = mod_addnew.lastname
    id = new_addnew.id
    app.addnew.mod_contact_by_id(mod_addnew.id, new_addnew)
    new_addnews = db.get_addnew_list()
    old_addnews.remove(mod_addnew)
    old_addnews.append(new_addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)
    if check_ui:
        assert sorted(new_addnews, key=CONTACT.id_or_max) == sorted(app.addnew.get_addnew_list(), key=CONTACT.id_or_max)




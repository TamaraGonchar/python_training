from model.contact import CONTACT
import random


def test_mod_contact_name(app, orm, check_ui):
    if len(orm.get_addnew_list()) == 0:
        app.addnew.createnew(CONTACT(name="Alisa"))
    old_addnews = orm.get_addnew_list()
    new_addnew = CONTACT(name="Klavdiya")
    mod_addnew = random.choice(old_addnews)
    new_addnew.id = mod_addnew.id
    if new_addnew.name is None:
        new_addnew.name = mod_addnew.name
    if new_addnew.lastname is None:
        new_addnew.lastname = mod_addnew.lastname
    app.addnew.mod_contact_by_id(mod_addnew.id, new_addnew)
    new_addnews = orm.get_addnew_list()
    old_addnews.remove(mod_addnew)
    old_addnews.append(new_addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)
    if check_ui:
        assert sorted(new_addnews, key=CONTACT.id_or_max) == sorted(app.addnew.get_addnew_list(), key=CONTACT.id_or_max)




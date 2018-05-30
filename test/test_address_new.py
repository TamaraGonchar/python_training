# -*- coding: utf-8 -*-
from model.contact import CONTACT


def test_address_new(app, orm, json_contacts, check_ui):
    addnew = json_contacts
    old_addnews = orm.get_addnew_list()
    app.addnew.createnew(addnew)
    new_addnew = orm.get_addnew_list()
    old_addnews.append(addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(old_addnews, key=CONTACT.id_or_max)
    if check_ui:
        print("проверка")
        assert sorted(new_addnew, key=CONTACT.id_or_max) == sorted(app.addnew.get_addnew_list(), key=CONTACT.id_or_max)



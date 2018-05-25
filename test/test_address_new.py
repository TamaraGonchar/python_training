# -*- coding: utf-8 -*-
from model.contact import CONTACT


def test_address_new(app, db, json_contacts):
    addnew = json_contacts
    old_addnews = db.get_addnew_list()
    app.addnew.createnew(addnew)
    new_addnews = db.get_addnew_list()
    old_addnews.append(addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)



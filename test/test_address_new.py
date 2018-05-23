# -*- coding: utf-8 -*-
from model.contact import CONTACT


def test_address_new(app, json_contacts):
    addnew = json_contacts
    old_addnews = app.addnew.get_addnew_list()
    app.addnew.createnew(addnew)
    assert len(old_addnews) + 1 == app.addnew.count()
    new_addnews = app.addnew.get_addnew_list()
    old_addnews.append(addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)



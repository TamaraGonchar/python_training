# -*- coding: utf-8 -*-
from model.contact import CONTACT



def test_address_new(app):
    old_addnews = app.addnew.get_addnew_list()
    addnew = CONTACT(
                          name="Anna", middlename="Ivanovna", lastname="Petrova", nickname="AnPet",
                          title="ZAO", company="Romashka", address="Moscow",
                          home="84951234567", mobile="89161234567", work="88001234567", fax="88000000000",
                          email="an@an.ru", email2="anp@an.ru", email3="aniv@an.ru", homepage="annaivanova.ru",
                          byear="1990", ayear="2010",
                          address2="Lenina street", phone2="83", notes="16")
    app.addnew.createnew(addnew)
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) + 1 == len(new_addnews)
    old_addnews.append(addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)


def test_empty_address_new(app):
    old_addnews = app.addnew.get_addnew_list()
    addnew = CONTACT(
                          name="", middlename="", lastname="", nickname="",
                          title="", company="", address="",
                          home="", mobile="", work="", fax="",
                          email="", email2="", email3="", homepage="",
                          byear="", ayear="",
                          address2="", phone2="", notes="")
    app.addnew.createnew(addnew)
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) + 1 == len(new_addnews)
    old_addnews.append(addnew)
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)




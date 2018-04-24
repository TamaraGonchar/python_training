# -*- coding: utf-8 -*-
from model.contact import CONTACT



def test_address_new(app):
    app.addnew.createnew(CONTACT(
                          name="Anna", middlename="Ivanovna", lastname="Petrova", nickname="AnPet",
                          title="ZAO", company="Romashka", adrdress="Moscow",
                          home="84951234567", mobile="89161234567", work="88001234567", fax="88000000000",
                          email="an@an.ru", email2="anp@an.ru", email3="aniv@an.ru", homapage="annaivanova.ru",
                          byear="1990", ayear="2010",
                          address2="Lenina street", phone2="83", notes="16"))


def test_empty_address_new(app):
    app.addnew.createnew(CONTACT(
                          name="", middlename="", lastname="", nickname="",
                          title="", company="", adrdress="",
                          home="", mobile="", work="", fax="",
                          email="", email2="", email3="", homapage="",
                          byear="", ayear="",
                          address2="", phone2="", notes=""))


    #DZ5

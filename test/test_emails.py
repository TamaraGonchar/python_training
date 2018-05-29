import re
from model.contact import CONTACT

def test_emails_on_home_page(app, db):
    if len(db.get_addnew_list()) == 0:
        app.addnew.create_new(CONTACT(name="Anna", middlename="Ivanovna", lastname="Petrova", nickname="AnPet",
                           title="ZAO", company="Romashka", address="Moscow",
                           home="84951234567", mobile="89161234567", work="88001234567", fax="88000000000",
                           email="an@an.ru", email2="anp@an.ru", email3="aniv@an.ru",
                           address2="Lenina street", phone2="83", notes="16"))

        addnews_ui = sorted(app.addnew.get_addnew_list(), key=CONTACT.id_or_max)
        addnews_db = sorted(db.get_addnew_list(), key=CONTACT.id_or_max)
        assert len(addnews_ui) == len(addnews_db)
        for i in range(len(addnews_ui)):
            assert addnews_ui[i].name == addnews_db[i].name
            assert addnews_ui[i].lastname == addnews_db[i].lastname
            assert addnews_ui[i].address == addnews_db[i].address
            assert clear(addnews_ui[i].all_emails_from_home_page) == merge_emails_like_on_home_page(addnews_db[i])
            assert clear(addnews_ui[i].all_phones_from_home_page) == merge_phones_like_on_home_page(addnews_db[i])




def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(mail):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [mail.email, mail.email2, mail.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))



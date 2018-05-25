from model.group import Group
from model.contact import CONTACT
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False  # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    print(timeit(lambda: app.addnew.get_addnew_list(), number=1))

    def clean(contact):
        return CONTACT(id=contact.id, name=contact.name.strip())
    print(timeit(lambda: map(clean, db.get_addnew_list()), number=1000))
    assert False  # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


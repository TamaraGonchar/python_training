from model.contact import CONTACT
from model.group import Group
import random

def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="MOYA GROUP"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_addnews_not_in_groups(group)) == 0:
        app.addnew.createnew(CONTACT(name="LOLA", middlename="MARTINOVA", lastname="IZOTOVA"))
    addnew = random.choice(orm.get_addnews_not_in_groups(group))
    app.addnew.add_to_group(addnew.id, group.id)
    assert addnew in orm.get_addnews_in_groups(group)


def test_remove_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="MOYA GROUP"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_addnew_list()) == 0:
        app.addnew.createnew(CONTACT(name="LOLA", middlename="MARTINOVA", lastname="IZOTOVA"))
    if len(orm.get_addnews_in_groups(group)) == 0:
        addnew = random.choice(orm.get_addnew_list())
        app.addnew.add_to_group(addnew.id, group.id)
    else:
        addnew = random.choice(orm.get_addnews_in_group(group))
    app.addnew.remove_from_group(addnew.id, group.id)
    assert addnew in orm.get_addnews_not_in_groups(group)

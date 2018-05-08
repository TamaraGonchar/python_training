from model.group import Group
from random import randrange


def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="NEW NAME")
    group.id = old_groups[index].id
    app.group.mod_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_mod_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
   # old_groups = app.group.get_group_list()
    #app.group.mod_first_group(Group(header="NEW HEADER"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

    #DZ 7
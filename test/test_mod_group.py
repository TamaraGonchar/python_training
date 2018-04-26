from model.group import Group

def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.mod_first_group(Group(name="NEW NAME"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_mod_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.mod_first_group(Group(header="NEW HEADER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

    #DZ 7
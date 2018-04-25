from model.group import Group

def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(name="NEW NAME"))


def test_mod_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(header="NEW HEADER"))

    #DZ 7
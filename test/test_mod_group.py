from model.group import Group

def test_mod_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="NEW NAME"))
    app.session.logout()


def test_mod_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(header="NEW HEADER"))
    app.session.logout()

    #DZ 7
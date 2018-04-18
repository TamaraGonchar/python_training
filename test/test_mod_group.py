from model.group import Group

def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group()
    app.group.create(Group(name="LOLO", header="KOKO", footer="AYAYAY"))
    app.session.logout()

    #DZ 7
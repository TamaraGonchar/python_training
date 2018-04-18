from model.addnew import Addnew


def test_mod_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.addnew.mod_first_contact()
    app.addnew.createnew(Addnew(
                          name="Vanya", middlename="Petrov", lastname="Ivanich", nickname="VAVA",
                          title="OOO", company="FanFan", adrdress="WWW",
                          home="84997654321", mobile="89107654321", work="88007654321", fax="88001111111",
                          email="va@va.ru", email2="Vap@Van.ru", email3="Vaniv@van.ru", homapage="Vannaivanova.ru",
                          byear="1990", ayear="2010",
                          address2="Mira street", phone2="20", notes="100"))
    app.session.logout()

    #DZ 7
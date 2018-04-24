from model.contact import CONTACT


def test_mod_first_contact(app):
    app.addnew.mod_first_contact()
    app.addnew.createnew(CONTACT(
                          name="Vanya", middlename="Petrov", lastname="Ivanich", nickname="VAVA",
                          title="OOO", company="FanFan", adrdress="WWW",
                          home="84997654321", mobile="89107654321", work="88007654321", fax="88001111111",
                          email="va@va.ru", email2="Vap@Van.ru", email3="Vaniv@van.ru", homapage="Vannaivanova.ru",
                          byear="1990", ayear="2010",
                          address2="Mira street", phone2="20", notes="100"))

    #DZ 7
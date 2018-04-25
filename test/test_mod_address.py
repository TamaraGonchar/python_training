from model.contact import CONTACT


def test_mod_contact_name(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(name="Alisa"))
    app.addnew.mod_first_contact(CONTACT(name="Klavdiya"))



def test_mod_contact_middlename(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(middlename="Lykoshkina"))
    app.addnew.mod_first_contact(CONTACT(middlename="Pyshinina"))

    #DZ 7
from model.contact import CONTACT


def test_mod_contact_name(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(name="Alisa"))
    old_addnews = app.addnew.get_addnew_list()
    app.addnew.mod_first_contact(CONTACT(name="Klavdiya"))
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) == len(new_addnews)



def test_mod_contact_middlename(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(middlename="Lykoshkina"))
    old_addnews = app.addnew.get_addnew_list()
    app.addnew.mod_first_contact(CONTACT(middlename="Pyshinina"))
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) == len(new_addnews)

    #DZ 7
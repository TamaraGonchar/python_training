from model.contact import CONTACT


def test_mod_contact_name(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(name="Alisa"))
    old_addnews = app.addnew.get_addnew_list()
    addnew = CONTACT(name="Klavdiya")
    addnew.id = old_addnews[0].id
    if addnew.name is None:
        addnew.name = old_addnews[0].name
    if addnew.lastname is None:
        addnew.lastname = old_addnews[0].lastname
    app.addnew.mod_first_contact(addnew)
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) == len(new_addnews)
    old_addnews[0] = addnew
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)




#def test_mod_contact_middlename(app):
#    if app.addnew.count() == 0:
#        app.addnew.createnew(CONTACT(middlename="Lykoshkina"))
#    old_addnews = app.addnew.get_addnew_list()
#    app.addnew.mod_first_contact(CONTACT(middlename="Pyshinina"))
#    new_addnews = app.addnew.get_addnew_list()
#    assert len(old_addnews) == len(new_addnews)

    #DZ 7
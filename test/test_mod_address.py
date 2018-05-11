from model.contact import CONTACT
from random import randrange



def test_mod_contact_name(app):
    if app.addnew.count() == 0:
        app.addnew.createnew(CONTACT(name="Alisa"))
    old_addnews = app.addnew.get_addnew_list()
    index = randrange(len(old_addnews))
    addnew = CONTACT(name="Klavdiya")
    addnew.id = old_addnews[index].id
    if addnew.name is None:
        addnew.name = old_addnews[index].name
    if addnew.lastname is None:
        addnew.lastname = old_addnews[index].lastname
    app.addnew.mod_contact_by_index(index, addnew)
    new_addnews = app.addnew.get_addnew_list()
    assert len(old_addnews) == app.addnew.count()
    old_addnews[index] = addnew
    assert sorted(old_addnews, key=CONTACT.id_or_max) == sorted(new_addnews, key=CONTACT.id_or_max)




#def test_mod_contact_middlename(app):
#    if app.addnew.count() == 0:
#        app.addnew.createnew(CONTACT(middlename="Lykoshkina"))
#    old_addnews = app.addnew.get_addnew_list()
#    app.addnew.mod_first_contact(CONTACT(middlename="Pyshinina"))
#    new_addnews = app.addnew.get_addnew_list()
#    assert len(old_addnews) == len(new_addnews)

    #DZ 7
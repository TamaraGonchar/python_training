import re

def test_phones_on_home_page(app):
    addnew_from_home_page = app.addnew.get_addnew_list()[0]
    addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
    assert addnew_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(addnew_from_edit_page)



def test_phones_on_contact_view_page(app):
    addnew_from_view_page = app.addnew.get_addnew_from_view_page(0)
    addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
    assert addnew_from_view_page.home == addnew_from_edit_page.home
    assert addnew_from_view_page.mobile == addnew_from_edit_page.mobile
    assert addnew_from_view_page.work == addnew_from_edit_page.work
    assert addnew_from_view_page.phone2 == addnew_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))



    #addnew_from_home_page = app.addnew.get_addnew_list()[0]
    #addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
    #assert addnew_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(addnew_from_edit_page)
    #assert addnew_from_home_page.name == addnew_from_edit_page.name
    #assert addnew_from_home_page.lastname == addnew_from_edit_page.lastname
    #assert addnew_from_home_page.address == addnew_from_edit_page.address

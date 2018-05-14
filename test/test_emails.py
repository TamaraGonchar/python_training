import re


def test_emails_on_home_page(app):
    addnew_from_home_page = app.addnew.get_addnew_list()[0]
    addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
    assert addnew_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(addnew_from_edit_page)


#def test_emails_on_contact_view_page(app):
#    addnew_from_view_page = app.addnew.get_addnew_from_view_page(0)
#    addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
#    assert addnew_from_view_page.email == addnew_from_edit_page.email
#    assert addnew_from_view_page.email2 == addnew_from_edit_page.email2
#    assert addnew_from_view_page.email3 == addnew_from_edit_page.email3


def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(mail):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [mail.email, mail.email2, mail.email3]))))

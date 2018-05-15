import re


def test_emails_on_home_page(app):
    addnew_from_home_page = app.addnew.get_addnew_list()[0]
    addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
    assert addnew_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(addnew_from_edit_page)
    assert addnew_from_home_page.name == addnew_from_edit_page.name
    assert addnew_from_home_page.lastname == addnew_from_edit_page.lastname
    assert addnew_from_home_page.address == addnew_from_edit_page.address



def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(mail):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [mail.email, mail.email2, mail.email3]))))

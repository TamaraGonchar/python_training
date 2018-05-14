import re


def test_names_on_home_page(app):
    addnew_from_home_page = app.addnew.get_addnew_list()[0]
    addnew_from_edit_page = app.addnew.get_addnew_info_from_edit_page(0)
    assert addnew_from_home_page.all_emails_from_home_page == merge_names_like_on_home_page(addnew_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_names_like_on_home_page(name):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [name.name, name.lastname, name.firstname]))))
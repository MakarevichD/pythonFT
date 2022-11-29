import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_main_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.work_num == contact_from_edit_page.work_num
    assert contact_from_view_page.mobile_num == contact_from_edit_page.mobile_num
    assert contact_from_view_page.home_num == contact_from_edit_page.home_num
    assert contact_from_view_page.fax_num == contact_from_edit_page.fax_num


def test_all_contact_fields(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.contact_name == contact_from_edit_page.contact_name
    assert contact_from_home_page.contact_surname == contact_from_edit_page.contact_surname
    assert contact_from_home_page.contact_address == contact_from_edit_page.contact_address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_main_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_main_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_main_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_num, contact.mobile_num, contact.work_num]))))

def merge_emails_like_on_main_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.contact_email, contact.contact_email_2])))
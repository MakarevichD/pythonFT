import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.work_num == clear(contact_from_edit_page.work_num)
    assert contact_from_home_page.mobile_num == clear(contact_from_edit_page.mobile_num)
    assert contact_from_home_page.home_num == clear(contact_from_edit_page.home_num)
    #assert contact_from_home_page.fax_num == contact_from_edit_page.fax_num


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.work_num == contact_from_edit_page.work_num
    assert contact_from_view_page.mobile_num == contact_from_edit_page.mobile_num
    assert contact_from_view_page.home_num == contact_from_edit_page.home_num
    assert contact_from_view_page.fax_num == contact_from_edit_page.fax_num


def clear(s):
    return re.sub("[() -]", "", s)

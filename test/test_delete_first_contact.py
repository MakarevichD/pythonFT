from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.contacts_count() == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

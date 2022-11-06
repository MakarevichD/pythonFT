from model.contact import Contact


def test_contact_editor(app):
    if app.contact.contacts_count() == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(contact_name="Kolya", contact_surname="Petrov", mobile_num="8098912", work_num="1099000")
    contact.id = old_contacts[0].id
    app.contact.edit_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts [0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
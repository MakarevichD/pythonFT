from model.contact import Contact


def test_new_contact_adding(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(contact_name="Gena", contact_surname="Babkov", work_num="432 4432", mobile_num="34 99800 ", second_num="2313", home_num="23232")
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.contacts_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

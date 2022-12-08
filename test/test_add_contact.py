from model.contact import Contact


def test_new_contact_adding(app, database, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = database.get_contact_list()
    app.contact.add_new_contact(contact)
    new_contacts = database.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

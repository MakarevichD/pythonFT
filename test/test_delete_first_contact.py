import random
from model.contact import Contact


def test_delete_some_contact(app, database, check_ui):
    if len(database.get_group_list()) == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900",fax_num="2313", home_num="23232",
                                            contact_address="Curupa 15", contact_email="ew@mail.ru", contact_email_2="pocavoca@fwk.com",
                                            contact_middle="Ivanovich", contact_title="director", contact_nickname="poc", contact_company="colase"))
    old_contacts = database.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = database.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max)


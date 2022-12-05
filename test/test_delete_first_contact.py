from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.contacts_count() == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900",fax_num="2313", home_num="23232",
                                            contact_address="Curupa 15", contact_email="ew@mail.ru", contact_email_2="pocavoca@fwk.com",
                                            contact_middle="Ivanovich", contact_title="director", contact_nickname="poc", contact_company="colase"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

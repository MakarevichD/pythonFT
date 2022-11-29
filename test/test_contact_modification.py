from model.contact import Contact
from random import randrange


def test_contact_editor(app):
    if app.contact.contacts_count() == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900",fax_num="2313", home_num="23232",
                                            contact_address="Curupa 15", contact_email="ew@mail.ru", contact_email_2="pocavoca@fwk.com",
                                            contact_middle="Ivanovich", contact_title="director", contact_nickname="poc", contact_company="colase"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(contact_name="Kolya", contact_surname="Petrov", mobile_num="8098912", work_num="1099000",
                      fax_num="2313", home_num="23232", contact_address="polocas 15", contact_email="qwe@mail.ru",contact_email_2="weas@fwk.com",
                      contact_middle="Igorevich", contact_title="noobas", contact_nickname="poc", contact_company="dssq")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

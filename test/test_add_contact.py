from model.contact import Contact


def test_new_contact_adding(app):
    app.contact.add_new_contact(Contact(contact_name="Gena", contact_surname="Babkov", work_num="432 4432", mobile_num="34 99800 "))

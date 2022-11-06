from model.contact import Contact


def test_contact_editor(app):
    if app.contact.contacts_count() == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900"))
    app.contact.edit_contact(Contact(contact_name="Kolya", contact_surname="Petrov", mobile_num="8098912", work_num="1099000"))
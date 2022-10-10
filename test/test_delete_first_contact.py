from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.contacts_count() == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900"))
    app.contact.delete_first_contact()

from model.contact import Contact


def test_contact_editor(app):
    app.session.login(username="admin", password="secret")
    app.contact.contact_modificate(Contact(contact_name="Igorek", contact_surname="Bambucha", mobile_num="221112321113333", work_num="33221"))
    app.session.logout()

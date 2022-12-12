import random
from model.group import Group
from model.contact import Contact


def test_adding_contact_to_group(app, database):
    if len(database.get_group_list()) == 0:
        app.group.creation(Group(name="new one", header="lolo", footer="fpdef"))
    if len(database.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(contact_surname="valerkin", contact_name="ignat",
                                            mobile_num="22123456789", work_num="900900", fax_num="2313",
                                            home_num="23232", contact_address="Curupa 15", contact_email="ew@mail.ru",
                                            contact_email_2="pocavoca@fwk.com", contact_middle="Ivanovich",
                                            contact_title="director", contact_nickname="poc", contact_company="colase"))
    contact_list = app.contact.get_contact_list()
    group_list = app.group.get_group_list()
    contact = random.choice(contact_list)
    group = random.choice(group_list)
    app.contact.add_selected_contact_to_group_by_id(contact.id, group.id)



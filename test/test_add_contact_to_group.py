import random
from model.group import Group
from model.contact import Contact


import random
from selenium.webdriver.support.select import Select
from model.group import Group
from model.contact import Contact


def test_adding_contact_to_group(app, database, orm):
    contact_list = orm.get_contact_list()
    if len(contact_list) == 0:
        app.contact.add_new_contact(
            Contact(contact_name="Kolya", contact_surname="Petrov", mobile_num="8098912", work_num="1099000",
                    fax_num="2313", home_num="23232", contact_address="polocas 15", contact_email="qwe@mail.ru",
                    contact_email_2="weas@fwk.com", contact_middle="Igorevich", contact_title="noobas",
                    contact_nickname="poc", contact_company="dssq"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    app.wd.implicitly_wait(10)
    old_contacts = orm.get_contacts_in_groups(group)
    if len(old_contacts) == 0:
        app.contact.create_contact_for_group(Contact(contact_name='Vasya', contact_surname='Petrov'), group)
        old_contacts = orm.get_contacts_in_groups(group)
    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_selected_contact_to_group(contact, group)
    old_contacts.append(contact)
    new_contacts = orm.get_contacts_in_groups(group)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)


def test_del_contact_from_group(app, database, orm):
    contact_list = orm.get_contact_list()
    if len(contact_list) == 0:
        app.contact.add(
            Contact(contact_name="Kolya", contact_surname="Petrov", mobile_num="8098912", work_num="1099000",
                    fax_num="2313", home_num="23232", contact_address="polocas 15", contact_email="qwe@mail.ru",
                    contact_email_2="weas@fwk.com", contact_middle="Igorevich", contact_title="noobas",
                    contact_nickname="poc", contact_company="dssq"))
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.creation(Group(name='onetwo', header='twoone', footer='oneone'))
    groups = orm.get_group_list()
    group = random.choice(groups)
    Select(app.wd.find_element_by_name('group')).select_by_value(group.id)
    contacts = orm.get_contacts_in_groups(group)
    if len(contacts) == 0:
        app.contact.create_contact_for_group(Contact(contact_name='igor', contact_surname='poleer'), group)
        contacts = orm.get_contacts_in_groups(group)
    contact = random.choice(contacts)
    app.contact.delete_contact_from_group(contact, group)
    contacts.remove(contact)
    new_contacts = orm.get_contacts_in_group(group)
    assert len(contacts) == len(new_contacts)
    assert sorted(contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

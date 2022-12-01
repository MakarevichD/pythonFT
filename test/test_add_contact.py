from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)]),


def random_phones(prefix, maxlen):
    numbers = string.digits + " " * 10
    return prefix + "".join([random.choice(numbers) for i in range(maxlen)])


def random_email(self, maxlen):
    email_dom = ['@gmail.com', '@yandex.ru', '@mail.ru', '@list.com']
    index = random.randrange(len(email_dom))
    name = ''.join(random.choice(string.ascii_letters) for _ in range(maxlen))
    email = name + email_dom[index]
    return email


testdata = [Contact(
    contact_name=random_string("contact_name", 6),
    contact_surname=random_string("contact_surname", 8),
    contact_middle=random_string("contact_middle", 8),
    contact_nickname=random_string("contact_nickname", 5),
    home_num=random_phones("+", 10),
    mobile_num=random_phones("+", 10),
    work_num=random_phones("+", 10),
    fax_num=random_phones("+", 10),
    contact_address=random_string("contact_address", 7),
    contact_company=random_string("contact_company", 6),
    contact_title=random_string("contact_title", 7),
    contact_email=random_email("contact_email", 6),
    contact_email_2=random_email("contact_email_2", 4))

    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact_adding(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.contacts_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

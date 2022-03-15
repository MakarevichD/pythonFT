import pytest
from contact import Contact
from dew.contact import ContactWriter


@pytest.fixture()
def cont(request):
    fixture = ContactWriter()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact_adding(cont):
    cont.login( username="admin", password="secret")
    cont.add_new_contact( Contact(contact_name="Gena", contact_surname="Babkov", work_num="432 4432", mobile_num="34 99800 "))
    cont.logout()

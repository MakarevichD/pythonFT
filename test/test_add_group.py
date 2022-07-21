from model.group import Group



def test_add_group(app):
    app.session.login(username ="admin", password ="secret")
    app.group.creation(Group(name ="efefef", header ="lolo", footer ="fpdef"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.creation(Group(name="", header="", footer=""))
    app.session.logout()

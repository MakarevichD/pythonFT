from model.group import Group


def test_group_modificate(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="lapki",header="pushistie",footer="kotikov"))
    app.session.logout()
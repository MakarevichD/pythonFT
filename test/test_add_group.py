from model.group import Group


def test_add_group(app):
    app.group.creation(Group(name="efefef", header="lolo", footer="fpdef"))


def test_add_empty_group(app):
    app.group.creation(Group(name="", header="", footer=""))

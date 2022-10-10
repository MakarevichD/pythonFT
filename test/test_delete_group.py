from model.group import Group


def test_delete_first_group(app):
    if app.group.group_count() == 0:
        app.group.creation(Group(name="new one", header="lolo", footer="fpdef"))
    app.group.delete_first_group()
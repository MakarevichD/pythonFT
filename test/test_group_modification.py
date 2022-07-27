from model.group import Group


def test_group_modificate_name(app):
    app.group.modify_first_group(Group(name="New group"))

def test_group_modificate_header(app):
    app.group.modify_first_group(Group(header="New header"))
from model.group import Group
from random import randrange


def test_group_modify(app, database, check_ui):
    if len(database.get_group_list()) == 0:
        app.group.creation(Group(name="new one", header="lolo", footer="fpdef"))
    old_groups = database.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified_name",  header="modified_header", footer="modified_footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = database.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_group_modificate_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


# def test_group_modificate_footer(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="New footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

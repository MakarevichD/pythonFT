from model.group import Group


def test_add_group(app, database, json_groups):
    group = json_groups
    old_groups = database.get_group_list()
    app.group.creation(group)
    new_groups = database.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

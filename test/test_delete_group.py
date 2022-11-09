from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.group_count() == 0:
        app.group.creation(Group(name="new one", header="lolo", footer="fpdef"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups

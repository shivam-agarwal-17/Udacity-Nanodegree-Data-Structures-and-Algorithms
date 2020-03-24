class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def _is_user_in_group_helper(user, current_group, explored_groups):
    """
    Recursively search for user in current_group and it's sub-groups

    Args:
        user(str): user name/id
        current_group(class:Group): group to check membership against
        explored_groups(set): set of groups already explored

    """
    explored_groups.add(current_group.get_name())
    for usr in current_group.get_users():
        if usr == user:
            return True
      
    found = False
    for grp in current_group.get_groups():
        if grp.get_name() not in explored_groups:
            found = _is_user_in_group_helper(user, grp, explored_groups)
            if found:
                break

    return found

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    return _is_user_in_group_helper(user, group, set())

def test_active_directory():

    print("\nTest case 1: user's sub-group has single parent group")
    
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, sub_child))
    # True
    print(is_user_in_group(sub_child_user, child))
    # True
    print(is_user_in_group(sub_child_user, parent))
    # True

    print("\nTest case 2: user's sub-group has multiple parent groups")
    A = Group('A')
    B = Group('B')
    C = Group('C')
    D = Group('D')
    E = Group('E')

    new_user = "new_user"
    C.add_user(new_user)

    A.add_group(B)
    A.add_group(C)
    D.add_group(C)
    D.add_group(E)

    print(is_user_in_group(new_user, A))
    # True
    print(is_user_in_group(new_user, B))
    # False
    print(is_user_in_group(new_user, C))
    # True
    print(is_user_in_group(new_user, D))
    # True
    print(is_user_in_group(new_user, E))
    # False

    print("\nTest case 3: user's sub-group does not have a parent group")
    A = Group('A')
    B = Group('B')
    C = Group('C')
    D = Group('D')

    new_user = "new_user"
    D.add_user(new_user)

    A.add_group(B)
    A.add_group(C)

    print(is_user_in_group(new_user, A))
    # False
    print(is_user_in_group(new_user, B))
    # False
    print(is_user_in_group(new_user, C))
    # False
    print(is_user_in_group(new_user, D))
    # True

if __name__ == "__main__":
    test_active_directory()



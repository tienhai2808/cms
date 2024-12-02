def in_group(user):
  return user.groups.filter(name__in=['Contributor', 'Approver', 'Editor']).exists()

def is_approver(user):
  return user.groups.filter(name='Approver').exists()

def is_editor(user):
  return user.groups.filter(name__in=['Approver', 'Editor']).exists()

def is_contributor(user):
  return user.groups.filter(name__in=['Approver', 'Contributor']).exists()
# Permissions and Groups Setup

This project implements Django custom permissions and user groups.

## Custom Permissions (in Book model)
- can_view
- can_create
- can_edit
- can_delete

## Groups Created via Admin:
### Viewers:
- can_view

### Editors:
- can_view
- can_create
- can_edit

### Admins:
- All permissions

## Permission Enforcement in Views:
Views use @permission_required decorators to restrict actions.

Example:
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request):
    ...

from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "you must have permission to make any changes on this obj"
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            if request.user==obj.user:
                return True
            else:
                return False

class IsOwnerOrSuperUserOrReadOnly(BasePermission):
    """
    The sole purpose of this class is to see to make sure that the user trying to make changes to an object is
    either a super user or the owner of the object itself.
    """
    def has_object_permission(self, request,view, object):
        safe_methods = ["GET","HEAD"]
        if request.method in safe_methods: #assigning permission for requests that does not create things
            return True
        else:
            if request.user.is_superuser: #Trying to check if the user is either a super user is an owner of the object
                self.message = "You have the permissions to make changes this object as a super user"
                return True
            elif request.user == object.user.user:
                return True
            else:
                self.message = "You do not have the permission to changes to this object"
                return False

from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj

class PostPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        print(request.user,obj.author)
        return request.user.is_superuser or request.user == obj.author



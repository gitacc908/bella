from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from apps.users.models import Bookmark


class CustomUserAdmin(UserAdmin):
    """
        Creating own admin and customise it to our own works
    """
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    list_display = ('phone', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',)


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Bookmark)

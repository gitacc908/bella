from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """
        Creating own admin and customise it to our own works
    """
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (
            _('Персональная Информация'), {
                'fields': ('first_name', 'last_name',)
            }
        ),
        (
            _('Избранные'), {'fields': ('favorite_products',)}
        ),
        (
            _('Права доступа'), {
                'fields': ('is_active', 'is_staff', 'is_superuser',
                           'groups', 'user_permissions')
            }
        ),
        (_('Важные даты'), {'fields': ('last_login', 'date_joined')},),
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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']

    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _("Permissions"),
            {'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )}
        ),
        (_('Important Dates'), {'fields': ('last_login', )}),
    )

    readonly_fields = ['last_login',]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',

            ),
        }),
    )


admin.site.register(models.User, UserAdmin)



# class UserAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(User, UserAdmin)


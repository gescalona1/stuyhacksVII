from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import MemberCreationForm, MemberChangeForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class MemberAdmin(UserAdmin):
    form = MemberChangeForm
    add_form = MemberCreationForm
    list_display = [
        'email',
        'username',
        'date_of_birth',
    ]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', )}),
        ('Permissions', {'fields': ('user_permissions', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'password')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(get_user_model(), MemberAdmin)
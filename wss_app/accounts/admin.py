from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from wss_app.accounts.forms import WssUserCreationForm, WssChangeForm
from wss_app.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = WssUserCreationForm
    form = WssChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'profile_picture']
    list_display_links = ['user', 'full_name']
    list_per_page = 50
    search_fields = ['user__email', 'first_name', 'last_name']
    search_help_text = 'Search by User Email, First Name or Last Name'

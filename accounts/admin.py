from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# this will overwrite the current user model that django give to us. This is a custom user model


# This will allow to modify and see the values of the user in another way
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'phone_number', 'is_active')
    list_display_links = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () # read only password 

admin.site.register(Account, AccountAdmin)


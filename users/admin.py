from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'email', 'amount_of_money')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('BuyerInfo', {'fields': ('amount_of_money',)})
    )
    add_fieldsets = (
        ('Basic', {'fields': ('username', 'password', 'amount_of_money')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

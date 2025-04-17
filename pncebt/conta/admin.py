from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from conta.models import Conta
from django.contrib.auth.models import User

class ContaInLine(admin.StackedInline):
    model = Conta
    can_delete = False
    verbose_name_plural = 'Contas'

class CustomizedUserAdmin(UserAdmin):
    inlines = (ContaInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Conta)
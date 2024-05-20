from django.contrib import admin
from myfolder.models import *


# Register your models here.


class AdminType(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Type, AdminType)


class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id', 'Name', 'turi', 'rasm', 'dare']


admin.site.register(Portfolio, AdminPortfolio)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Team, AdminTeam)


class AdminServices(admin.ModelAdmin):
    list_display = ['id', 'ism']


admin.site.register(Services, AdminServices)


class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'Ism']


admin.site.register(Contact, AdminContact)


class AdminSubscribe(admin.ModelAdmin):
    list_display = ['id', 'Email']


admin.site.register(Subscribe, AdminSubscribe)

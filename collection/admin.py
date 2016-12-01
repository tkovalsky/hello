from django.contrib import admin
from collection.models import Thing, Social

# Register your models here.
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'user', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ['network', 'username',]


admin.site.register(Thing, ThingAdmin)
admin.site.register(Social, SocialAdmin)

from django.contrib import admin
from .models import Profiles

class ProfilesAdmin(admin.ModelAdmin):
    class Meta:
        model = Profiles

admin.site.register(Profiles, ProfilesAdmin)


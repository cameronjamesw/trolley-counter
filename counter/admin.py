from django.contrib import admin
from .models import Trolley, FrontLabel, BackLabel

# Register your models here.

admin.site.register(Trolley)

admin.site.register(FrontLabel)

admin.site.register(BackLabel)
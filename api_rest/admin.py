from django.contrib import admin
from api_rest import models

admin.site.register(models.Client)
admin.site.register(models.Vehicle)
admin.site.register(models.Rent)
from django.contrib import admin
from .models import Item
from .models import job_post, Cv

admin.site.register(Item)
admin.site.register(job_post)
admin.site.register(Cv)


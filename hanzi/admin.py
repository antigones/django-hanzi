from django.contrib import admin

# Register your models here.
from .models import Hanzi
from .models import Test

admin.site.register(Hanzi)
admin.site.register(Test)
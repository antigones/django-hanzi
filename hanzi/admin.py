from django.contrib import admin

# Register your models here.
from .models import Hanzi
from .models import Radical
from .models import Test

admin.site.register(Hanzi)
admin.site.register(Radical)
admin.site.register(Test)
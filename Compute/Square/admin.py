
from django.contrib import admin

from .models import SquareTest

class SquareTestDetail(admin.ModelAdmin):
    list_display=('Number','SquareNumber')
admin.site.register(SquareTest,SquareTestDetail)

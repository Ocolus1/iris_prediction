from django.contrib import admin
from .models import PredResults

class PredResultsAdmin(admin.ModelAdmin):
    list_display = ("sepal_length", "sepal_width", "petal_length","petal_width","classification" )
    list_display_links = ("sepal_length", "sepal_width", "petal_length","petal_width","classification" )


admin.site.register(PredResults, PredResultsAdmin)

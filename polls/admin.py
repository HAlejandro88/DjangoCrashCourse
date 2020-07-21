from django.contrib import admin

from .models import Question, Choise


admin.site.site_header = "Polister Admin"
admin.site.title = "Polister Admin Area"
admin.site.index_title = " Welcome to the Polister admin"

class ChoiseInline(admin.TabularInline):
    model = Choise
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), 
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiseInline]

""" admin.site.register(Question)
admin.site.register(Choise) """

admin.site.register(Question, QuestionAdmin)
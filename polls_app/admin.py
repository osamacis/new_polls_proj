from django.contrib import admin
# Register your models here.

from .models import Question , Choice , Teacher, Student, Club, Country, Company, Proxy_company
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text'] # fields
    fieldsets = [('Question field',{'fields':['question_text'],'description':'this is question field :'}), #fieldsets
             ('Data information',{'fields':['pub_date']})
    ]
    list_display = ['id','question_text','pub_date']
    search_fields = ['question_text']
    list_filter = ['pub_date']

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Club)
admin.site.register(Country)
admin.site.register(Company)
admin.site.register(Proxy_company)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)


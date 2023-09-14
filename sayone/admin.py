from django.contrib import admin
# from django.contrib.auth.models import Group # for the use of Group
# Register your models here.
from .models import Category ,Details ,Book, User, User_post

admin.site.register(User_post)
# admin.site.register(Group_user)

class  CategoryAdmin(admin.ModelAdmin):
    pass

class  DetailsAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','pages','category_id','is_published']
    actions = ['make_published']
    @admin.action(description='Mark selected book as published')
    def make_published(self,request,queryset):
        queryset.update(is_published='published')

class DetailsInline(admin.StackedInline):
    model = Details


admin.site.register(Category, CategoryAdmin)
admin.site.register(Details,DetailsAdmin)
admin.site.register(Book)
# admin.site.unregister(Group) #to unregister Group from the admin 
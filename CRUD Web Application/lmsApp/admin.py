from django.contrib import admin
from lmsApp import models
from .models import Category,SubCategory,Books,Students,Borrow
# Register your models here.
# admin.site.register(models.Groups)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Books)
admin.site.register(Students)
admin.site.register(Borrow)

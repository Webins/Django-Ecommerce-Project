from django.contrib import admin
from .models import Category 

# Django web applications access and manage data through Python objects referred to as models.
# Models define the structure of stored data, including the field types and possibly also their maximum size, default values, 
# selection list options, help text for documentation, label text for forms, etc

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'description', 'image')


admin.site.register(Category, CategoryAdmin)

# when the model is registered, we need to make the migrations
# py manage.py makemigrations
# then we commit the migrations with the next command py manage.py migrate

# for the django admin panel, we need to create a superuser with the next command py manage.py createsuperuser (winpty py manage.py createsuperuser)
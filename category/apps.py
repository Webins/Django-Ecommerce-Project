
# A Django application is a Python package that is specifically 
# intended for use in a Django project. An application may use common Django conventions, 
# such as having models , tests , urls , and views submodules.

# to create an app, we run the command py manage.py startapp 'app name' 

# we need to register the app (in this case, category) in the settings of the project (installed apps).

from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'

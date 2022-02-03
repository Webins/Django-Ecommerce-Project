from .models import Category

# this function allow the data requested to be accesed by all the templates of your app
# remember that this function has to be added to the TEMPLATES located in the settings.py file

def menu_links(request):
    links = {
        'links': Category.objects.all(),
    }

    return links

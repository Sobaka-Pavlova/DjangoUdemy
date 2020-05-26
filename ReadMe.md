
// This is how to do simplest backend for your new .html page

//0. Create a separate app for pages/listings/etc, as well as a separate folder for templates for all apps

//1. Create a base.html file with !+Enter, make {% block content %} and {% endblock %} in the body

//2. Create new.html file and add {% extends 'base.html' %} on top to use layout from base.html

""" 3. Define a new method in views.py i.e 

// def new(request):
//  return render(request, 'appname_e.g._pages/new.html')

"""

"""4. Define path (Add a urlpattern) i.e. in urls.py


// from django.urls import path

// from . import views

// urlpatterns = [
//  path('new', views.new, name='new'),


"""

// Don't forget to let django know you have new folder for templates

// 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        




        <!--  Как прикрутить Header, Footer and Navigation   -->
В Templates запихнуть folder with header, footer, navigation etc
В {% %} прописать include 'folder_with_header_etc/filename.html'
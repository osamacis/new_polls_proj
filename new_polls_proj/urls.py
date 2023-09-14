"""
URL configuration for new_polls_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sayone import views
# below the other imports
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# #...
# urlpatterns = []
# urlpatterns +=staticfiles_urlpatterns()
# urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'New_Polls_Project_Admin'
# admin.site.site_title = 'Django_proj'
admin.site.index_title = 'Anurag_projects'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("polls_app/", include("polls_app.urls")),
    path('sayone/',include('sayone.urls')),
    path('booksystem/',include('booksystem.urls')),
    # path('',views.login_user.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
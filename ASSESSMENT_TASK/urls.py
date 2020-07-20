"""ASSESSMENT_TASK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ASSESSMENT_TASK import settings
from BANKING_MODEL import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.User_login_page.as_view(), name ='User_login_page'),
    path('user_details_data/',views.User_details_data.as_view(),name='user_details_data'),
    path('save_user_details/',views.User_details_data.as_view(),name='save_user_details'),
    path('admin_page/',views.Admin_Page.as_view(), name='admin_page'),
    path('pending_status/',views.pending_status, name = 'pending_status'),
    path('approve_status/',views.approve_status, name ='approve_status'),
    path('reject_status/',views.reject_status,name='reject_status'),
    path('see_all_data/',views.see_all_data,name='see_all_data'),
    # path('search/',views.search, name = 'search')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

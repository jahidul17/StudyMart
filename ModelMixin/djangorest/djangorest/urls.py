"""
URL configuration for djangorest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    # path('ailist/',views.AiquestList.as_view(),name='ailist'),
    # path('aiquestcreate/',views.AiquestCreate.as_view(),name='aiquestcreate'),
    path('aiquest_list_create/',views.Aiquest_List_Create.as_view(),name='aiquest_list_create'),
     
    
    # path('aiquestretrive/<int:pk>',views.AiquestRetrive.as_view(),name='aiquestretrive'),
    # path('aiquestupdate/<int:pk>',views.AiquestUpdate.as_view(),name='aiquestupdate'),
    # path('aiquestdelete/<int:pk>',views.AiquestDestroy.as_view(),name='aiquestdelete'),
    
    path('aiquest_retrive_update_destroy/<int:pk>',views.Aiquest_Retrive_Update_Destroy.as_view(),name='aiquest_retrive_update_destroy'),
    
    
    # path('aicreate/',views.AiquestCreate.as_view(),name='aicreate'),
    # path('aicreate/<int:pk>',views.AiquestCreate.as_view(),name='aicreate'),
]

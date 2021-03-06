from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import debug_toolbar
from info import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('', views.home, name='name'),
    path('admin/', admin.site.urls),
    path('minerals/', include('info.urls')),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('group/<group_name>/', views.search_by_group, name='group'),
    path('letter/<letter>/', views.search_by_letter, name='letter'),
    path('search/', views.search_by_keyword, name='keyword'),
    path('__debug__/', include(debug_toolbar.urls)),
]


urlpatterns += staticfiles_urlpatterns()
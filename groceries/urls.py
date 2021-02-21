from django.urls import path
from . import views
from .views import GroceryItemListView
urlpatterns = [

    path('', views.home, name='home'),
    path('api/', views.show_list,name = 'api'),
    path('api1/', GroceryItemListView.as_view(), name = 'api1')
]
#define URL route for index() view
from django.urls import path
from . import views
from .views import bookingview

urlpatterns = [

    path('', views.index, name='index'),
    path('booking/', bookingview.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
]

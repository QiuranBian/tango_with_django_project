from django.urls import path
from DjProject import views
app_name = 'DjProject'
urlpatterns = [
    path('', views.index, name='index'),
]
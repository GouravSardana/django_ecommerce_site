from django.urls import path
from . import views
from .views import Post_ad

app_name = 'home'

urlpatterns = [
    path('' , views.home , name='home') ,
    path('post-ad.html/',Post_ad.as_view(), name = 'post-ad')

]
from django.urls import path
from .views import test_function, home, post_by_id

app_name = 'blog'

urlpatterns = [
    path('', test_function, name='test'),
    path('home/', home, name='home'),
    path('home/post/<int:pk>', post_by_id, name='post_by_id')
]

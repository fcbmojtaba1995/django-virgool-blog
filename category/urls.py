from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('all_categories/', views.all_categories, name='all_categories'),
    path('<int:category_id>/<str:category_name>/', views.posts_in_category, name='posts_in_category')
]

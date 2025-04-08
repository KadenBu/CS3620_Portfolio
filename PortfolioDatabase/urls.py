from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.index, name="Index"),
    path('hobbies/', views.hobbies, name="Hobbies"),
    path('portfolio/', views.portfolio, name="Portfolio"),
    path('contact/', views.contact, name="Contact"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="HobbyDetails"),
    path('portfolio/<int:project_id>', views.project_detail, name="ProjectDetails"),
]
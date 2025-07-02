from django.urls import path

from blog import views

app_name = 'pages'

urlpatterns = [
    path('pages/about/', views.about, name='about'),
    path('pages/rules/', views.rules, name='rules'),
]
